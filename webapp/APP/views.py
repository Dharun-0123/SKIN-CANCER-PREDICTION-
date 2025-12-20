from django.shortcuts import render, redirect
from . models import UserPredictModel, UserProfile
from . forms import UserPredictForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .email_utils import send_welcome_email, send_prediction_notification, send_profile_update_notification
import numpy as np

from tensorflow import keras
from PIL import Image, ImageOps
from . import forms
from django.core.files.storage import FileSystemStorage
import os
from .models import predict
import json


def convert_numpy_types(obj):
    """Convert numpy types to Python native types for JSON serialization"""
    if obj is None:
        return None
    elif isinstance(obj, dict):
        return {key: convert_numpy_types(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_numpy_types(item) for item in obj]
    elif isinstance(obj, (np.integer, np.int32, np.int64)):
        return int(obj)
    elif isinstance(obj, (np.floating, np.float32, np.float64)):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    else:
        return obj


def send_smart_analysis_notification(user, prediction, image_path):
    """Send email notification only for first analysis to preserve email quota"""
    try:
        # Ensure user has a profile
        if not hasattr(user, 'profile'):
            UserProfile.objects.create(user=user)
        
        # Check if this is the first analysis and email notifications are enabled
        if (user.profile.email_notifications and 
            not user.profile.first_analysis_email_sent):
            
            # Send the first analysis email
            from .email_utils import send_prediction_notification
            send_prediction_notification(user, prediction, image_path)
            
            # Mark that first analysis email has been sent
            user.profile.first_analysis_email_sent = True
            user.profile.save()
            
            print(f"✅ First analysis email sent to {user.email}")
        else:
            print(f"📧 Email skipped for {user.email} (quota preservation)")
            
    except Exception as e:
        print(f"❌ Email notification error: {str(e)}")



def Landing_1(request):
    return render(request, '1_Landing.html')

def test_view(request):
    return render(request, 'test.html')

def simple_test(request):
    from django.http import HttpResponse
    html = """
    <!DOCTYPE html>
    <html>
    <head><title>Simple Test</title></head>
    <body style="background: purple; color: white; padding: 50px;">
        <h1>Simple HttpResponse Test</h1>
        <p>If you see this, HttpResponse works!</p>
    </body>
    </html>
    """
    return HttpResponse(html)

def home_minimal(request):
    return render(request, 'home_minimal.html')

def Register_2(request):
    # Redirect if already logged in
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in!')
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            # Send welcome email
            send_welcome_email(user)
            
            # Send OTP for email verification
            from .otp_utils import send_otp_email
            success, message = send_otp_email(user)
            
            if success:
                messages.success(request, f'Account created for {username}! Please check your email for verification code.')
                # Store user ID in session for verification
                request.session['verify_user_id'] = user.id
                return redirect('verify_email')
            else:
                messages.warning(request, f'Account created but failed to send verification email: {message}')
                return redirect('login')
        else:
            # Show form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = UserRegisterForm()
    
    context = {'form': form}
    return render(request, '2_Register.html', context)


def Login_3(request):
    # Redirect if already logged in
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            # Redirect to next page if specified, otherwise home
            next_page = request.GET.get('next', 'home')
            return redirect(next_page)
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    context = {}
    return render(request, '3_Login.html', context)


def Admin_Login(request):
    # Redirect if already logged in as admin
    if request.user.is_authenticated:
        if request.user.is_staff or request.user.is_superuser:
            return redirect('admin_dashboard')
        else:
            messages.warning(request, 'You are logged in as a regular user. Please logout first.')
            return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Check if user is admin/staff
            if user.is_staff or user.is_superuser:
                login(request, user)
                messages.success(request, f'Welcome, Administrator {username}!')
                return redirect('admin_dashboard')
            else:
                messages.error(request, 'Access denied. This account does not have administrator privileges.')
        else:
            messages.error(request, 'Invalid admin credentials. Please try again.')

    context = {}
    return render(request, 'admin_login.html', context)

@login_required(login_url='login')
def Home_4(request):
    from django.db.models import Count
    from datetime import datetime, timedelta
    import json
    
    # Get user's prediction count
    user_predictions = UserPredictModel.objects.filter(user=request.user).count()
    
    # Get recent activity (last 7 days) for mini chart
    recent_activity = []
    for i in range(6, -1, -1):
        day = datetime.now() - timedelta(days=i)
        day_start = day.replace(hour=0, minute=0, second=0, microsecond=0)
        day_end = day.replace(hour=23, minute=59, second=59, microsecond=999999)
        count = UserPredictModel.objects.filter(
            user=request.user,
            created_at__gte=day_start,
            created_at__lte=day_end
        ).count()
        recent_activity.append(count)
    
    context = {
        'user': request.user,
        'prediction_count': user_predictions,
        'recent_activity': json.dumps(recent_activity)
    }
    return render(request, '4_Home.html', context)

def Teamates_5(request):
    return render(request,'5_Teamates.html')

def Domain_Result_6(request):
    return render(request,'6_Domain_Result.html')

def Problem_Statement_7(request):
    return render(request,'7_Problem_Statement.html')
    
@login_required(login_url='login')
def Deploy_8(request): 
    if request.method == "POST":
        try:
            print(f"🔍 DEBUG: POST data received: {request.POST}")
            form = forms.UserPredictForm(data=request.POST, files=request.FILES)
            print(f"🔍 DEBUG: Form created with data: {form.data}")
            
            if form.is_valid():
                print(f"🔍 DEBUG: Form is valid. Cleaned data: {form.cleaned_data}")
                # Save the form but don't commit to database yet
                obj = form.save(commit=False)
                # Assign the current user to the prediction
                obj.user = request.user
                print(f"🔍 DEBUG: Before save - model_preference: {obj.model_preference}")
                obj.save()
                print(f"🔍 DEBUG: After save - model_preference: {obj.model_preference}")
            else:
                print(f"🔍 DEBUG: Form is invalid. Errors: {form.errors}")
                obj = form.instance

            result1 = UserPredictModel.objects.filter(user=request.user).latest('id')
            from django.conf import settings
            
            # Get user's model preference
            user_preference = result1.model_preference
            print(f"🔍 DEBUG: User selected model preference: {user_preference}")
            print(f"🔍 DEBUG: POST data: {request.POST}")
            print(f"🔍 DEBUG: Form data saved: model_preference = {result1.model_preference}")
            
            # Load both models
            # Primary Model: EfficientNetB0 (trained on 25,331 images)
            primary_model_path = os.path.join(settings.BASE_DIR, "models", "EfficientNetB0_skin-cancer.h5")
            # Secondary Model: Original CNN (trained on 3,297 images)  
            secondary_model_path = os.path.join(settings.BASE_DIR, "models", "CNN_skin-cancer.h5")
            
            image_path = os.path.join(settings.MEDIA_ROOT, str(result1))
            image = Image.open(image_path).convert("RGB")
            
            # Model selection based on user preference
            model_used = ""
            confidence = 0.0
            
            if user_preference == 'cnn':
                # Force use CNN model
                print("🎯 User selected: CNN Model (Forced)")
                try:
                    secondary_model = keras.models.load_model(secondary_model_path, compile=False)
                    
                    # Prepare image for CNN (48x48)
                    size = (48, 48)
                    image_resized = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
                    image_array = np.asarray(image_resized)
                    normalized_image_array = (image_array.astype(np.float32) / 255.0)
                    data_secondary = np.ndarray(shape=(1, 48, 48, 3), dtype=np.float32)
                    data_secondary[0] = normalized_image_array
                    
                    # Original class names (7 classes + not_skin_cancer)
                    classes_secondary = ['Actinic keratoses','Basal cell carcinoma','Benign keratosis like lesions','Dermatofibroma','Melanoma','Melanocytic nevi','Vascular lesions',"not_skin_cancer"]
                    
                    prediction_secondary = secondary_model.predict(data_secondary)
                    confidence = np.max(prediction_secondary)
                    secondary_idx = np.argmax(prediction_secondary)
                    a = classes_secondary[secondary_idx]
                    model_used = "CNN (User Selected)"
                    
                    print(f"CNN Model Result: {a} (Confidence: {confidence:.3f})")
                    
                except Exception as e:
                    print(f"CNN model failed: {e}")
                    a = "Error loading CNN model"
                    model_used = "Error"
                    
            elif user_preference == 'efficientnet':
                # Force use EfficientNetB0 model
                print("🎯 User selected: EfficientNetB0 Model (Forced)")
                try:
                    if os.path.exists(primary_model_path):
                        primary_model = keras.models.load_model(primary_model_path, compile=False)
                        
                        # Prepare image for EfficientNetB0 (224x224)
                        size = (224, 224)
                        image_resized = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
                        image_array = np.asarray(image_resized)
                        normalized_image_array = (image_array.astype(np.float32) / 255.0)
                        data_primary = np.expand_dims(normalized_image_array, axis=0)
                        
                        # Updated class names for new model (8 classes)
                        classes = ['AK', 'BCC', 'BKL', 'DF', 'MEL', 'NV', 'SCC', 'VASC']
                        class_names_full = [
                            'Actinic keratoses', 'Basal cell carcinoma', 'Benign keratosis like lesions',
                            'Dermatofibroma', 'Melanoma', 'Melanocytic nevi', 'Squamous cell carcinoma', 'Vascular lesions'
                        ]
                        
                        prediction_primary = primary_model.predict(data_primary)
                        confidence = np.max(prediction_primary)
                        primary_idx = np.argmax(prediction_primary)
                        a = class_names_full[primary_idx]
                        model_used = "EfficientNetB0 (User Selected)"
                        
                        print(f"EfficientNetB0 Model Result: {a} (Confidence: {confidence:.3f})")
                    else:
                        raise Exception("EfficientNetB0 model not found")
                        
                except Exception as e:
                    print(f"EfficientNetB0 model failed: {e}")
                    a = "Error loading EfficientNetB0 model"
                    model_used = "Error"
                    
            else:
                # Auto mode (default intelligent selection)
                print("🎯 Auto Mode: Intelligent Model Selection")
                try:
                    if os.path.exists(primary_model_path):
                        print("Using Primary Model: EfficientNetB0 (25,331 images)")
                        # Load EfficientNetB0 with custom handling for compatibility issues
                        import tensorflow as tf
                        try:
                            primary_model = keras.models.load_model(primary_model_path, compile=False)
                        except Exception as load_error:
                            print(f"Primary model load error: {load_error}")
                            # Try with custom object scope
                            try:
                                with tf.keras.utils.custom_object_scope({}):
                                    primary_model = keras.models.load_model(primary_model_path, compile=False, custom_objects={'Cast': tf.cast})
                            except Exception as custom_error:
                                print(f"Custom load also failed: {custom_error}")
                                raise Exception("Could not load primary model")
                        
                        # Prepare image for EfficientNetB0 (224x224)
                        size = (224, 224)
                        image_resized = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
                        image_array = np.asarray(image_resized)
                        normalized_image_array = (image_array.astype(np.float32) / 255.0)
                        data_primary = np.expand_dims(normalized_image_array, axis=0)
                        
                        # Updated class names for new model (8 classes)
                        classes = ['AK', 'BCC', 'BKL', 'DF', 'MEL', 'NV', 'SCC', 'VASC']
                        class_names_full = [
                            'Actinic keratoses', 'Basal cell carcinoma', 'Benign keratosis like lesions',
                            'Dermatofibroma', 'Melanoma', 'Melanocytic nevi', 'Squamous cell carcinoma', 'Vascular lesions'
                        ]
                        
                        prediction_primary = primary_model.predict(data_primary)
                        primary_confidence = np.max(prediction_primary)
                        primary_idx = np.argmax(prediction_primary)
                        primary_result = class_names_full[primary_idx]
                        
                        print(f"Primary Model Prediction: {primary_result} (Confidence: {primary_confidence:.3f})")
                        
                        # Use primary model result if confidence is high enough
                        if primary_confidence > 0.5:  # Threshold for primary model
                            a = primary_result
                            model_used = "EfficientNetB0 (Primary)"
                            confidence = primary_confidence
                        else:
                            raise Exception("Low confidence, falling back to secondary model")
                            
                    else:
                        raise Exception("Primary model not found")
                        
                except Exception as e:
                    print(f"Primary model failed: {str(e)}, using secondary model")
                    
                    # Fallback to secondary model (Original CNN)
                    print("Using Secondary Model: CNN (3,297 images)")
                    secondary_model = keras.models.load_model(secondary_model_path, compile=False)
                    
                    # Prepare image for CNN (48x48)
                    size = (48, 48)
                    image_resized = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
                    image_array = np.asarray(image_resized)
                    normalized_image_array = (image_array.astype(np.float32) / 255.0)
                    data_secondary = np.ndarray(shape=(1, 48, 48, 3), dtype=np.float32)
                    data_secondary[0] = normalized_image_array
                    
                    # Original class names (7 classes + not_skin_cancer)
                    classes_secondary = ['Actinic keratoses','Basal cell carcinoma','Benign keratosis like lesions','Dermatofibroma','Melanoma','Melanocytic nevi','Vascular lesions',"not_skin_cancer"]
                    
                    prediction_secondary = secondary_model.predict(data_secondary)
                    secondary_confidence = np.max(prediction_secondary)
                    secondary_idx = np.argmax(prediction_secondary)
                    a = classes_secondary[secondary_idx]
                    model_used = "CNN (Secondary)"
                    confidence = secondary_confidence
                    
                    print(f"Secondary Model Prediction: {a} (Confidence: {confidence:.3f})")
            
            print(f"Final Prediction: {a} using {model_used} (Confidence: {confidence:.3f})")
            print("output_class_name+++++++++++++++++",a)
            
            # Import the legal-compliant result formatter
            from .result_formatter import format_legal_result, format_html_result
            
            # Store original prediction for database
            original_prediction = a
            
            # Generate legally-compliant result
            legal_result = format_legal_result(original_prediction, confidence, model_used)
            
            # Use legal result for display
            a = legal_result['educational_description']
            b = legal_result['prevention_info'] 
            c = legal_result['precautions']
            
            # Legacy condition handling (keeping for compatibility)
            if original_prediction.lower() == 'actinic keratoses':
                a =  'Actinic keratosis is a common precancerous skin condition often caused by sun exposure.'
                b =  'Preventions: Protect your skin from the sun by wearing protective clothing and applying sunscreen. Avoid prolonged sun exposure, especially during peak hours. Perform regular skin checks and seek medical attention for any suspicious lesions.'
                c = 'Precautions: Limit sun exposure, especially during midday hours. Use sunscreen with SPF regularly. Wear protective clothing and accessories like hats and sunglasses when outdoors. Avoid tanning beds and sunlamps.'
            elif a.lower() == 'basal cell carcinoma':          
                a = 'Basal cell carcinoma is a common type of skin cancer that typically appears as a small, shiny bump or a pinkish patch on the skin.'
                b = 'Preventions: Protect your skin from the sun by wearing sunscreen, protective clothing, and seeking shade. Avoid tanning beds and sunlamps. Perform regular skin self-examinations and seek medical attention for any new or changing lesions.'
                c = 'Precautions: Limit sun exposure, especially during peak hours. Use broad-spectrum sunscreen with a high SPF regularly. Wear protective clothing like hats and long sleeves. Avoid outdoor activities during midday when the suns rays are strongest.'
            elif a.lower() == 'dermatofibroma':
                a = 'Dermatofibroma is a benign skin growth that usually appears as a small, firm bump on the skin, often brownish or reddish in color.'
                b = 'Preventions: Since the exact cause of dermatofibroma is unknown, prevention methods focus on protecting the skin from injury or irritation. Avoiding trauma to the skin and maintaining good skincare practices may help reduce the risk of developing dermatofibromas.'
                c = 'Precautions: Handle the skin gently to prevent injuries that may lead to dermatofibroma formation. Avoid picking, scratching, or squeezing existing skin lesions. If a bump appears, monitor it for any changes and consult a dermatologist if concerned.'
            elif a.lower() == 'melanoma':
                a = 'Melanoma is a type of skin cancer that develops from melanocytes, the cells that produce pigment in the skin.'
                b = 'Preventions: Protect your skin from the sun by wearing sunscreen with a high SPF, protective clothing, and seeking shade. Avoid tanning beds and sunlamps. Perform regular skin self-examinations and seek medical attention for any suspicious moles or changes in existing moles.'
                c = 'Precautions: Limit sun exposure, especially during peak hours. Use broad-spectrum sunscreen and reapply it frequently, especially after swimming or sweating. Wear protective clothing, hats, and sunglasses. Avoid outdoor activities during midday when the suns rays are strongest. Regularly check your skin for any new or changing moles, and consult a dermatologist if you notice any abnormalities.'
            elif a.lower() == 'melanocytic nevi':
                a = 'A nevus, commonly known as a mole, is a benign growth on the skin that develops when melanocytes (pigment-producing cells) grow in clusters.'
                b = 'Preventions: While moles cannot be prevented entirely, protecting your skin from the sun can help reduce their development. This includes wearing sunscreen, protective clothing, and seeking shade.'
                c = 'Precautions: Monitor your moles for any changes in size, shape, color, or texture. Protect your skin from excessive sun exposure to prevent the development of new moles. Consult a dermatologist if you notice any suspicious changes in your moles or if you have concerns about a particular mole.'
            elif a.lower() == 'benign keratosis like lesions':
                a = 'Pigmented benign keratosis, is a common harmless skin growth that often looks like a wart with a waxy texture.'
                b = 'Preventions: While the exact cause is unclear, protecting your skin from the sun may help prevent these growths. Wear sunscreen and protective clothing when outdoors.'
                c = 'Precautions: Keep an eye on your skin for any new or changing growths. Avoid excessive sun exposure and tanning beds. If you notice anything unusual, consult a dermatologist.'
            elif a.lower() == 'not_skin_cancer':
                a = 'Non-cancerous skin conditions include various types of skin irritations, rashes, and benign growths that are not associated with cancerous growth..'
                b = 'Preventions: Protect your skin by avoiding prolonged exposure to irritants, such as harsh chemicals or allergens. Maintain good skincare practices, including gentle cleansing and moisturizing. '
                c = 'Precautions: Regularly monitor your skin for any changes or new developments. If you notice any unusual symptoms or if the condition persists or worsens, consult a dermatologist for proper evaluation and treatment.'
            elif a.lower() in ['vascular lesions', 'vascular lesion']:
                a = 'A vascular lesion is an abnormal cluster of blood vessels that can cause red or purple marks on the skin.'
                b = 'Preventions: Preventing vascular lesions may not always be possible, but protecting your skin from injury and maintaining good skin health may help.'
                c = 'Precautions: Keep an eye on any unusual marks on your skin. Protect your skin from injuries and excessive sun exposure. If you notice anything concerning, consult a dermatologist.'
            elif a.lower() in ['squamous cell carcinoma', 'scc']:
                a = 'Squamous cell carcinoma is a common type of skin cancer that develops in the squamous cells of the outer layer of skin.'
                b = 'Preventions: Protect your skin from UV radiation by wearing sunscreen, protective clothing, and seeking shade. Avoid tanning beds and excessive sun exposure. Regular skin examinations can help detect early signs.'
                c = 'Precautions: Limit sun exposure, especially during peak hours. Use broad-spectrum sunscreen with high SPF. Wear protective clothing and accessories. Avoid tanning beds. Monitor your skin for any new or changing lesions and consult a dermatologist promptly.'
            else:
                a = 'Image may not be suitable for reliable analysis'
                b = 'The image quality or content may not be optimal for our AI analysis system'
                c = 'Consider uploading a clearer, well-lit image of the skin area for better results'

            # Update the specific record we just created
            result1.label = original_prediction  # Store the actual AI prediction, not the educational description
            result1.model_used = model_used
            result1.confidence_score = confidence
            result1.save()
            
            print(f"Final Prediction: {a} using {model_used} (Confidence: {confidence:.3f})")
            
            # Send email notification only for first analysis (to preserve email quota)
            send_smart_analysis_notification(request.user, a, str(result1))
            
            # Store results in session for the results page (convert numpy types to Python types)
            request.session['analysis_results'] = {
                'prediction_id': result1.id,
                'predict': a,
                'c': c,
                'b': b,
                'legal_result': convert_numpy_types(legal_result),
                'model_used': model_used,
                'confidence': float(confidence) if confidence is not None else None,
                'user_preference': user_preference,
                'original_prediction': original_prediction
            }
            
            # Redirect to dedicated results page
            return redirect('analysis_results')
        except Exception as e:
            print(f"Error in prediction: {str(e)}")
            messages.error(request, f'Error processing image: {str(e)}')
            form = forms.UserPredictForm()
            return render(request, '8_Deploy.html',{'form':form})
    else:
        form = forms.UserPredictForm()
    return render(request, '8_Deploy.html',{'form':form})


@login_required(login_url='login')
def analysis_results(request):
    """Dedicated results page for analysis output"""
    
    # Get results from session
    results_data = request.session.get('analysis_results')
    if not results_data:
        messages.error(request, 'No analysis results found. Please run a new analysis.')
        return redirect('analyze')
    
    # Get the prediction object
    try:
        obj = UserPredictModel.objects.get(id=results_data['prediction_id'], user=request.user)
    except UserPredictModel.DoesNotExist:
        messages.error(request, 'Analysis results not found.')
        return redirect('analyze')
    
    # Import the result formatter for HTML generation
    from .result_formatter import format_html_result
    
    # Generate formatted HTML if legal_result exists
    formatted_html = None
    if results_data.get('legal_result'):
        formatted_html = format_html_result(results_data['legal_result'])
    
    context = {
        'obj': obj,
        'predict': results_data.get('predict'),
        'c': results_data.get('c'),
        'b': results_data.get('b'),
        'legal_result': results_data.get('legal_result'),
        'formatted_html': formatted_html,
        'model_used': results_data.get('model_used'),
        'confidence': results_data.get('confidence'),
        'user_preference': results_data.get('user_preference'),
        'original_prediction': results_data.get('original_prediction')
    }
    
    # Clear the session data after use
    if 'analysis_results' in request.session:
        del request.session['analysis_results']
    
    return render(request, 'analysis_results.html', context)

@login_required(login_url='login')
def Out_Database_9(request):
    # Only show predictions for the current logged-in user
    models = UserPredictModel.objects.filter(user=request.user).order_by('-created_at')
    return render(request, '9_Out_Database.html', {'models':models})


def input (request):
    return render(request,"imageUpload.html")


class_names = np.array(['Actinic keratoses','Basal cell carcinoma','Benign keratosis like lesions','Dermatofibroma','Melanoma','Melanocytic nevi','Vascular lesions',"not_skin_cancer"])


def patientResult(request):
    try:
        algo ="inc"
        img_file = request.FILES['image']
        print(img_file)
        
        # Save the uploaded image to the local disk
        fs = FileSystemStorage()
        filename = fs.save(img_file.name, img_file)
        saved_img_path = os.path.join(fs.location, filename)
        print(saved_img_path)
        print("----------------------------")
        file_parts = saved_img_path.split('\\')

        # Extract the filename from the last part of the split
        fname = file_parts[-1]
        filename ="../media/"+fname

        print("111111111",filename) 
        # Open the image file
        image = Image.open(saved_img_path)

        # Convert the image to a NumPy array
        image_array = np.array(image)

        # Call the predict function on the saved image
        out = predict(saved_img_path, algo)
        print(out)
        output = out[0].tolist()
        print(type(out))
        out = np.argmax(out)
        classes = class_names[out]
        print(classes)
        label = class_names.tolist()
        label_json = json.dumps(label)

        print('prs------------------',saved_img_path)
        print(output,'1233333333333')

        if classes.lower() == 'actinic keratoses':
            a =  'Actinic keratosis is a common precancerous skin condition often caused by sun exposure.'
            b =  'Preventions: Protect your skin from the sun by wearing protective clothing and applying sunscreen. Avoid prolonged sun exposure, especially during peak hours. Perform regular skin checks and seek medical attention for any suspicious lesions.'
            c = 'Precautions: Limit sun exposure, especially during midday hours. Use sunscreen with SPF regularly. Wear protective clothing and accessories like hats and sunglasses when outdoors. Avoid tanning beds and sunlamps.'
        elif classes.lower() == 'basal cell carcinoma':          
            a = 'Basal cell carcinoma is a common type of skin cancer that typically appears as a small, shiny bump or a pinkish patch on the skin.'
            b = 'Preventions: Protect your skin from the sun by wearing sunscreen, protective clothing, and seeking shade. Avoid tanning beds and sunlamps. Perform regular skin self-examinations and seek medical attention for any new or changing lesions.'
            c = 'Precautions: Limit sun exposure, especially during peak hours. Use broad-spectrum sunscreen with a high SPF regularly. Wear protective clothing like hats and long sleeves. Avoid outdoor activities during midday when the suns rays are strongest.'
        elif classes.lower() == 'dermatofibroma':
            a = 'Dermatofibroma is a benign skin growth that usually appears as a small, firm bump on the skin, often brownish or reddish in color.'
            b = 'Preventions: Since the exact cause of dermatofibroma is unknown, prevention methods focus on protecting the skin from injury or irritation. Avoiding trauma to the skin and maintaining good skincare practices may help reduce the risk of developing dermatofibromas.'
            c = 'Precautions: Handle the skin gently to prevent injuries that may lead to dermatofibroma formation. Avoid picking, scratching, or squeezing existing skin lesions. If a bump appears, monitor it for any changes and consult a dermatologist if concerned.'
        elif classes.lower() == 'melanoma':
            a = 'Melanoma is a type of skin cancer that develops from melanocytes, the cells that produce pigment in the skin.'
            b = 'Preventions: Protect your skin from the sun by wearing sunscreen with a high SPF, protective clothing, and seeking shade. Avoid tanning beds and sunlamps. Perform regular skin self-examinations and seek medical attention for any suspicious moles or changes in existing moles.'
            c = 'Precautions: Limit sun exposure, especially during peak hours. Use broad-spectrum sunscreen and reapply it frequently, especially after swimming or sweating. Wear protective clothing, hats, and sunglasses. Avoid outdoor activities during midday when the suns rays are strongest. Regularly check your skin for any new or changing moles, and consult a dermatologist if you notice any abnormalities.'
        elif classes.lower() == 'melanocytic nevi':
            a = 'A nevus, commonly known as a mole, is a benign growth on the skin that develops when melanocytes (pigment-producing cells) grow in clusters.'
            b = 'Preventions: While moles cannot be prevented entirely, protecting your skin from the sun can help reduce their development. This includes wearing sunscreen, protective clothing, and seeking shade.'
            c = 'Precautions: Monitor your moles for any changes in size, shape, color, or texture. Protect your skin from excessive sun exposure to prevent the development of new moles. Consult a dermatologist if you notice any suspicious changes in your moles or if you have concerns about a particular mole.'
        elif classes.lower() == 'benign keratosis like lesions':
            a = 'Pigmented benign keratosis, is a common harmless skin growth that often looks like a wart with a waxy texture.'
            b = 'Preventions: While the exact cause is unclear, protecting your skin from the sun may help prevent these growths. Wear sunscreen and protective clothing when outdoors.'
            c = 'Precautions: Keep an eye on your skin for any new or changing growths. Avoid excessive sun exposure and tanning beds. If you notice anything unusual, consult a dermatologist.'
        elif classes.lower() == 'not_skin_cancer':
            a = 'Non-cancerous skin conditions include various types of skin irritations, rashes, and benign growths that are not associated with cancerous growth..'
            b = 'Preventions: Protect your skin by avoiding prolonged exposure to irritants, such as harsh chemicals or allergens. Maintain good skincare practices, including gentle cleansing and moisturizing. '
            c = 'Precautions: Regularly monitor your skin for any changes or new developments. If you notice any unusual symptoms or if the condition persists or worsens, consult a dermatologist for proper evaluation and treatment.'
        elif classes.lower() in ['vascular lesions', 'vascular lesion']:
            a = 'A vascular lesion is an abnormal cluster of blood vessels that can cause red or purple marks on the skin.'
            b = 'Preventions: Preventing vascular lesions may not always be possible, but protecting your skin from injury and maintaining good skin health may help.'
            c = 'Precautions: Keep an eye on any unusual marks on your skin. Protect your skin from injuries and excessive sun exposure. If you notice anything concerning, consult a dermatologist.'                
        else:
            classes = 'Image may need adjustment'
            a = 'The image may not be optimal for analysis'
            b = 'Consider uploading a clearer, well-lit image of the skin area'
            c = 'Ensure the image shows the skin area clearly with good lighting'

        return render(request,"charts.html",{'chartDetails':  output,'label':label_json,'preditionImage':filename,"report":classes,"a":a,"b":b,"c":c})
    except Exception as e:
        print(f"Error in patientResult: {str(e)}")
        messages.error(request, f'Error processing image: {str(e)}')
        return redirect('input')

def charts (request):
    return render(request,"charts.html")

@login_required(login_url='login')
def Analytics(request):
    """Analytics dashboard with data visualizations"""
    from django.db.models import Count
    from django.db.models.functions import TruncMonth, TruncWeek, TruncDate
    from datetime import datetime, timedelta
    import json
    
    # Get all user predictions
    predictions = UserPredictModel.objects.filter(user=request.user)
    total_predictions = predictions.count()
    
    # This week count
    week_ago = datetime.now() - timedelta(days=7)
    this_week_count = predictions.filter(created_at__gte=week_ago).count()
    
    # This month count
    month_ago = datetime.now() - timedelta(days=30)
    this_month_count = predictions.filter(created_at__gte=month_ago).count()
    
    # Unique conditions
    unique_conditions = predictions.values('label').distinct().count()
    
    # Condition Distribution (for pie chart)
    condition_counts = predictions.values('label').annotate(
        count=Count('label')
    ).order_by('-count')
    
    condition_labels = []
    condition_values = []
    for item in condition_counts:
        if item['label'] and item['label'] != 'data':
            # Truncate long labels
            label = item['label'][:50] + '...' if len(item['label']) > 50 else item['label']
            condition_labels.append(label)
            condition_values.append(item['count'])
    
    condition_distribution = {
        'labels': condition_labels,
        'values': condition_values
    }
    
    # Monthly Trend (last 6 months)
    six_months_ago = datetime.now() - timedelta(days=180)
    monthly_data = predictions.filter(
        created_at__gte=six_months_ago
    ).annotate(
        month=TruncMonth('created_at')
    ).values('month').annotate(
        count=Count('id')
    ).order_by('month')
    
    monthly_labels = []
    monthly_values = []
    for item in monthly_data:
        monthly_labels.append(item['month'].strftime('%b %Y'))
        monthly_values.append(item['count'])
    
    monthly_trend = {
        'labels': monthly_labels,
        'values': monthly_values
    }
    
    # Top Conditions (top 5)
    top_conditions_data = condition_counts[:5]
    top_labels = []
    top_values = []
    for item in top_conditions_data:
        if item['label'] and item['label'] != 'data':
            label = item['label'][:30] + '...' if len(item['label']) > 30 else item['label']
            top_labels.append(label)
            top_values.append(item['count'])
    
    top_conditions = {
        'labels': top_labels,
        'values': top_values
    }
    
    # Weekly Activity (last 7 days)
    weekly_data = []
    for i in range(6, -1, -1):
        day = datetime.now() - timedelta(days=i)
        day_start = day.replace(hour=0, minute=0, second=0, microsecond=0)
        day_end = day.replace(hour=23, minute=59, second=59, microsecond=999999)
        count = predictions.filter(
            created_at__gte=day_start,
            created_at__lte=day_end
        ).count()
        weekly_data.append({
            'day': day.strftime('%a'),
            'count': count
        })
    
    weekly_labels = [item['day'] for item in weekly_data]
    weekly_values = [item['count'] for item in weekly_data]
    
    weekly_activity = {
        'labels': weekly_labels,
        'values': weekly_values
    }
    
    context = {
        'total_predictions': total_predictions,
        'this_week_count': this_week_count,
        'this_month_count': this_month_count,
        'unique_conditions': unique_conditions,
        'condition_distribution': json.dumps(condition_distribution),
        'monthly_trend': json.dumps(monthly_trend),
        'top_conditions': json.dumps(top_conditions),
        'weekly_activity': json.dumps(weekly_activity),
    }
    
    return render(request, 'analytics.html', context)


@login_required(login_url='login')
def Profile(request):
    """User profile view with edit functionality"""
    # Ensure user has a profile
    if not hasattr(request.user, 'profile'):
        UserProfile.objects.create(user=request.user)
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            # Send profile update notification
            send_profile_update_notification(request.user)
            
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    # Get user statistics
    total_predictions = UserPredictModel.objects.filter(user=request.user).count()
    recent_predictions = UserPredictModel.objects.filter(user=request.user).order_by('-created_at')[:5]
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'total_predictions': total_predictions,
        'recent_predictions': recent_predictions,
    }
    return render(request, 'profile.html', context)


@login_required(login_url='login')
def Compare(request):
    """Comparison page for multiple analyses"""
    predictions = UserPredictModel.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'predictions': predictions
    }
    return render(request, 'compare.html', context)


@login_required(login_url='login')
def CompareData(request):
    """API endpoint to get comparison data"""
    import json
    from django.http import JsonResponse
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            ids = data.get('ids', [])
            
            predictions = UserPredictModel.objects.filter(
                user=request.user,
                id__in=ids
            ).order_by('-created_at')
            
            result = {
                'predictions': [
                    {
                        'id': pred.id,
                        'date': pred.created_at.strftime('%B %d, %Y at %I:%M %p'),
                        'label': pred.label if pred.label != 'data' else 'Analysis in progress',
                        'image_url': pred.image.url if pred.image else ''
                    }
                    for pred in predictions
                ]
            }
            
            return JsonResponse(result)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required(login_url='login')
def ExportPDF(request):
    """Export analysis or comparison as PDF"""
    from django.http import HttpResponse
    from .pdf_utils import generate_analysis_report, generate_comparison_report
    import json
    
    if request.method == 'POST':
        try:
            ids_json = request.POST.get('ids', '[]')
            ids = json.loads(ids_json)
            
            predictions = UserPredictModel.objects.filter(
                user=request.user,
                id__in=ids
            ).order_by('-created_at')
            
            if not predictions.exists():
                messages.error(request, 'No analyses found to export.')
                return redirect('history')
            
            # Generate PDF
            if len(predictions) == 1:
                pdf = generate_analysis_report(predictions.first(), request.user)
                filename = f'analysis_report_{predictions.first().id}.pdf'
            else:
                pdf = generate_comparison_report(predictions, request.user)
                filename = f'comparison_report_{len(predictions)}_analyses.pdf'
            
            # Return PDF response
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            
            messages.success(request, 'PDF report generated successfully!')
            return response
            
        except Exception as e:
            print(f"Error generating PDF: {str(e)}")
            messages.error(request, f'Error generating PDF: {str(e)}')
            return redirect('history')
    
    return redirect('history')


@login_required(login_url='login')
def ExportSinglePDF(request, prediction_id):
    """Export a single analysis as PDF"""
    from django.http import HttpResponse
    from .pdf_utils import generate_analysis_report
    
    try:
        prediction = UserPredictModel.objects.get(id=prediction_id, user=request.user)
        
        # Generate PDF
        pdf = generate_analysis_report(prediction, request.user)
        filename = f'analysis_report_{prediction.id}.pdf'
        
        # Return PDF response
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        
        return response
        
    except UserPredictModel.DoesNotExist:
        messages.error(request, 'Analysis not found.')
        return redirect('history')
    except Exception as e:
        print(f"Error generating PDF: {str(e)}")
        messages.error(request, f'Error generating PDF: {str(e)}')
        return redirect('history')


@login_required(login_url='login')
def AdminDashboard(request):
    """Admin dashboard with system statistics and user management"""
    from django.contrib.auth.models import User
    from django.db.models import Count
    from datetime import datetime, timedelta
    import json
    
    # Check if user is admin/staff
    if not request.user.is_staff and not request.user.is_superuser:
        messages.error(request, 'You do not have permission to access the admin dashboard.')
        return redirect('home')
    
    # Total users
    total_users = User.objects.count()
    
    # New users this week
    week_ago = datetime.now() - timedelta(days=7)
    new_users_week = User.objects.filter(date_joined__gte=week_ago).count()
    
    # Total analyses
    total_analyses = UserPredictModel.objects.count()
    
    # Analyses today
    today_start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    analyses_today = UserPredictModel.objects.filter(created_at__gte=today_start).count()
    
    # Average analyses per day (last 30 days)
    thirty_days_ago = datetime.now() - timedelta(days=30)
    analyses_last_30 = UserPredictModel.objects.filter(created_at__gte=thirty_days_ago).count()
    avg_per_day = round(analyses_last_30 / 30, 1)
    
    # Active users (last 7 days)
    active_user_ids = UserPredictModel.objects.filter(
        created_at__gte=week_ago
    ).values_list('user_id', flat=True).distinct()
    active_users = len(set(active_user_ids))
    
    # Recent users with their prediction counts
    recent_users_data = []
    recent_users = User.objects.order_by('-date_joined')[:10]
    
    for user in recent_users:
        prediction_count = UserPredictModel.objects.filter(user=user).count()
        profile_picture = None
        if hasattr(user, 'profile') and user.profile.profile_picture:
            profile_picture = user.profile.profile_picture.url
        
        recent_users_data.append({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'date_joined': user.date_joined,
            'prediction_count': prediction_count,
            'is_active': user.is_active,
            'profile_picture': profile_picture
        })
    
    # Recent activity
    recent_activity = []
    
    # Recent registrations
    for user in User.objects.order_by('-date_joined')[:3]:
        recent_activity.append({
            'type': 'user',
            'icon': 'user-plus',
            'title': f'{user.username} joined',
            'time': user.date_joined.strftime('%B %d at %I:%M %p')
        })
    
    # Recent analyses
    for pred in UserPredictModel.objects.order_by('-created_at')[:3]:
        recent_activity.append({
            'type': 'analysis',
            'icon': 'microscope',
            'title': f'{pred.user.username} analyzed an image',
            'time': pred.created_at.strftime('%B %d at %I:%M %p')
        })
    
    # Sort by time (most recent first)
    recent_activity = sorted(recent_activity, key=lambda x: x['time'], reverse=True)[:10]
    
    # Usage data for chart (last 30 days)
    usage_labels = []
    usage_users = []
    usage_analyses = []
    
    for i in range(29, -1, -1):
        day = datetime.now() - timedelta(days=i)
        day_start = day.replace(hour=0, minute=0, second=0, microsecond=0)
        day_end = day.replace(hour=23, minute=59, second=59, microsecond=999999)
        
        # New users that day
        users_count = User.objects.filter(
            date_joined__gte=day_start,
            date_joined__lte=day_end
        ).count()
        
        # Analyses that day
        analyses_count = UserPredictModel.objects.filter(
            created_at__gte=day_start,
            created_at__lte=day_end
        ).count()
        
        usage_labels.append(day.strftime('%b %d'))
        usage_users.append(users_count)
        usage_analyses.append(analyses_count)
    
    usage_data = {
        'labels': usage_labels,
        'users': usage_users,
        'analyses': usage_analyses
    }
    
    context = {
        'total_users': total_users,
        'new_users_week': new_users_week,
        'total_analyses': total_analyses,
        'analyses_today': analyses_today,
        'avg_per_day': avg_per_day,
        'active_users': active_users,
        'recent_users': recent_users_data,
        'recent_activity': recent_activity,
        'usage_data': json.dumps(usage_data)
    }
    
    return render(request, 'admin_dashboard.html', context)


@login_required(login_url='login')
def DermaGenie(request):
    """DermaGenie AI Chat Assistant"""
    return render(request, 'dermagenie.html')


@login_required(login_url='login')
def DermaGenieChat(request):
    """API endpoint for DermaGenie chat"""
    from django.http import JsonResponse
    from .ai_assistant import get_dermagenie_response, save_conversation
    import json
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '').strip()
            
            if not user_message:
                return JsonResponse({
                    'success': False,
                    'message': 'Please enter a message.'
                })
            
            # Get AI response
            response = get_dermagenie_response(user_message)
            
            if response['success']:
                # Save conversation
                save_conversation(request.user, user_message, response)
                
                return JsonResponse({
                    'success': True,
                    'formatted_html': response['formatted_html'],
                    'tokens_used': response.get('tokens_used', 0)
                })
            else:
                return JsonResponse({
                    'success': False,
                    'message': response.get('message', 'An error occurred.')
                })
                
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Error: {str(e)}'
            })
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


@login_required(login_url='login')
def DermaGenieWidgetChat(request):
    """API endpoint for DermaGenie widget chat (simplified responses)"""
    from django.http import JsonResponse
    from .ai_assistant import get_dermagenie_response
    import json
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '').strip()
            
            if not user_message:
                return JsonResponse({
                    'success': False,
                    'response': 'Please enter a message.'
                })
            
            # Add context for skin-specific questions
            context_message = f"""You are DermaGenie AI, a helpful skin health assistant. 
            Keep responses concise (2-3 sentences) for the chat widget.
            Focus on skin health, dermatology, and skin cancer information.
            
            User question: {user_message}"""
            
            # Get AI response
            response = get_dermagenie_response(context_message)
            
            if response['success']:
                # Extract plain text from formatted HTML
                import re
                plain_text = re.sub('<[^<]+?>', '', response['formatted_html'])
                plain_text = plain_text.replace('&nbsp;', ' ').strip()
                
                return JsonResponse({
                    'success': True,
                    'response': plain_text
                })
            else:
                return JsonResponse({
                    'success': False,
                    'response': 'Sorry, I encountered an error. Please try again or visit the full DermaGenie page for more detailed assistance.'
                })
                
        except Exception as e:
            return JsonResponse({
                'success': False,
                'response': f'Sorry, I\'m having trouble right now. Please try again later.'
            })
    
    return JsonResponse({'success': False, 'response': 'Invalid request method.'})


def TermsAndConditions(request):
    """Terms & Conditions page"""
    return render(request, 'terms_and_conditions.html')


def Logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('landing')



# Email Verification Views
def verify_email(request):
    """View for entering OTP to verify email"""
    # Redirect if already logged in
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in and verified!')
        return redirect('home')
    
    # Get user ID from session
    user_id = request.session.get('verify_user_id')
    
    if not user_id:
        messages.error(request, 'No verification session found. Please register again.')
        return redirect('register')
    
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        messages.error(request, 'User not found.')
        return redirect('register')
    
    if request.method == 'POST':
        entered_otp = request.POST.get('otp', '').strip()
        
        if not entered_otp:
            messages.error(request, 'Please enter the OTP.')
            return render(request, 'verify_email.html', {'user': user})
        
        # Verify OTP
        from .otp_utils import verify_otp
        success, message = verify_otp(user, entered_otp)
        
        if success:
            messages.success(request, message)
            # Clear session
            if 'verify_user_id' in request.session:
                del request.session['verify_user_id']
            # Log user in
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, message)
    
    context = {'user': user}
    return render(request, 'verify_email.html', context)


def resend_otp_view(request):
    """View to resend OTP"""
    # Redirect if already logged in
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in and verified!')
        return redirect('home')
    
    user_id = request.session.get('verify_user_id')
    
    if not user_id:
        messages.error(request, 'No verification session found.')
        return redirect('register')
    
    try:
        user = User.objects.get(id=user_id)
        from .otp_utils import resend_otp
        success, message = resend_otp(user)
        
        if success:
            messages.success(request, 'OTP resent successfully! Please check your email.')
        else:
            messages.error(request, message)
    except User.DoesNotExist:
        messages.error(request, 'User not found.')
        return redirect('register')
    
    return redirect('verify_email')


# Password Reset Views
def forgot_password(request):
    """View for requesting password reset"""
    # Redirect if already logged in
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in!')
        return redirect('home')
    
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        
        if not email:
            messages.error(request, 'Please enter your email address.')
            return render(request, 'forgot_password.html')
        
        # Send password reset OTP
        from .password_reset_utils import send_password_reset_otp
        success, message, user = send_password_reset_otp(email)
        
        if success:
            messages.success(request, message)
            # Store user ID in session for password reset
            request.session['reset_user_id'] = user.id
            return redirect('verify_reset_otp')
        else:
            messages.error(request, message)
    
    return render(request, 'forgot_password.html')


def verify_reset_otp(request):
    """View for verifying password reset OTP"""
    # Redirect if already logged in
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in!')
        return redirect('home')
    
    # Get user ID from session
    user_id = request.session.get('reset_user_id')
    
    if not user_id:
        messages.error(request, 'No password reset session found. Please request a new code.')
        return redirect('forgot_password')
    
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        messages.error(request, 'User not found.')
        return redirect('forgot_password')
    
    if request.method == 'POST':
        entered_otp = request.POST.get('otp', '').strip()
        
        if not entered_otp:
            messages.error(request, 'Please enter the OTP.')
            return render(request, 'verify_reset_otp.html', {'user': user})
        
        # Verify password reset OTP
        from .password_reset_utils import verify_password_reset_otp
        success, message = verify_password_reset_otp(user, entered_otp)
        
        if success:
            messages.success(request, message)
            # Store verification status in session
            request.session['otp_verified'] = True
            return redirect('reset_password')
        else:
            messages.error(request, message)
    
    context = {'user': user}
    return render(request, 'verify_reset_otp.html', context)


def reset_password(request):
    """View for setting new password after OTP verification"""
    # Redirect if already logged in
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in!')
        return redirect('home')
    
    # Check if OTP was verified
    if not request.session.get('otp_verified'):
        messages.error(request, 'Please verify your OTP first.')
        return redirect('forgot_password')
    
    # Get user ID from session
    user_id = request.session.get('reset_user_id')
    
    if not user_id:
        messages.error(request, 'Session expired. Please request a new password reset.')
        return redirect('forgot_password')
    
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        messages.error(request, 'User not found.')
        return redirect('forgot_password')
    
    if request.method == 'POST':
        new_password = request.POST.get('new_password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()
        
        # Validation
        if not new_password or not confirm_password:
            messages.error(request, 'Please fill in all fields.')
            return render(request, 'reset_password.html', {'user': user})
        
        if new_password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'reset_password.html', {'user': user})
        
        if len(new_password) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
            return render(request, 'reset_password.html', {'user': user})
        
        # Set new password
        user.set_password(new_password)
        user.save()
        
        # Clear session
        if 'reset_user_id' in request.session:
            del request.session['reset_user_id']
        if 'otp_verified' in request.session:
            del request.session['otp_verified']
        
        messages.success(request, 'Password reset successfully! You can now login with your new password.')
        return redirect('login')
    
    context = {'user': user}
    return render(request, 'reset_password.html', context)


def resend_reset_otp(request):
    """View to resend password reset OTP"""
    # Redirect if already logged in
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in!')
        return redirect('home')
    
    user_id = request.session.get('reset_user_id')
    
    if not user_id:
        messages.error(request, 'No password reset session found.')
        return redirect('forgot_password')
    
    try:
        user = User.objects.get(id=user_id)
        from .password_reset_utils import send_password_reset_otp
        success, message, _ = send_password_reset_otp(user.email)
        
        if success:
            messages.success(request, 'Password reset code resent successfully! Please check your email.')
        else:
            messages.error(request, message)
    except User.DoesNotExist:
        messages.error(request, 'User not found.')
        return redirect('forgot_password')
    
    return redirect('verify_reset_otp')
