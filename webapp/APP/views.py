from django.shortcuts import render, redirect
from . models import UserPredictModel, UserProfile
from . forms import UserPredictForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
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
            form = forms.UserPredictForm(files=request.FILES)
            if form.is_valid():
                # Save the form but don't commit to database yet
                obj = form.save(commit=False)
                # Assign the current user to the prediction
                obj.user = request.user
                obj.save()
            else:
                obj = form.instance

            result1 = UserPredictModel.objects.filter(user=request.user).latest('id')
            from django.conf import settings
            model_path = os.path.join(settings.BASE_DIR, "models", "CNN_skin-cancer.h5")
            models = keras.models.load_model(model_path, compile=False)
            data = np.ndarray(shape=(1, 48, 48, 3), dtype=np.float32)
            image_path = os.path.join(settings.MEDIA_ROOT, str(result1))
            image = Image.open(image_path).convert("RGB")
            size = (48, 48)
            image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
            image_array = np.asarray(image)
            normalized_image_array = (image_array.astype(np.float32) / 255.0)
            data[0] = normalized_image_array
            classes = ['Actinic keratoses','Basal cell carcinoma','Benign keratosis like lesions','Dermatofibroma','Melanoma','Melanocytic nevi','Vascular lesions',"not_skin_cancer"]
            prediction = models.predict(data)
            idd = np.argmax(prediction)
            a = (classes[idd])
            print("output_class_name+++++++++++++++++",a)
            if a.lower() == 'actinic keratoses':
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
            else:
                a = 'WRONG INPUT'
                b = 'Unable to classify'
                c = 'Please try again'

            data = UserPredictModel.objects.latest('id')
            data.label = a
            data.save()
            
            # Send email notification if enabled
            send_prediction_notification(request.user, a, str(result1))
            
            return render(request, '8_Deploy.html',{'form':form,'obj':obj,'predict':a, 'c':c,'b':b})
        except Exception as e:
            print(f"Error in prediction: {str(e)}")
            messages.error(request, f'Error processing image: {str(e)}')
            form = forms.UserPredictForm()
            return render(request, '8_Deploy.html',{'form':form})
    else:
        form = forms.UserPredictForm()
    return render(request, '8_Deploy.html',{'form':form})


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
            classes = 'WRONG INPUT'
            a = 'Unable to classify the image'
            b = 'Please upload a clear image of a skin lesion'
            c = 'Ensure the image is well-lit and focused'

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


def Logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('landing')



# Email Verification Views
def verify_email(request):
    """View for entering OTP to verify email"""
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
