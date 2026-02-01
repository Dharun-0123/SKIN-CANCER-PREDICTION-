"""
EfficientNetB3 Training Script for ISIC 2019 Dataset
Complete training pipeline with evaluation, visualization, and model export
"""

# ============================================================================
# CELL 1: Environment Setup & Imports
# ============================================================================

# Install required packages (uncomment if needed in Kaggle)
# !pip install -q tensorflow scikit-learn matplotlib seaborn opencv-python

import os
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import cv2
import json
from datetime import datetime

# TensorFlow and Keras
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models, optimizers, callbacks
from tensorflow.keras.applications import EfficientNetB3
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import to_categorical

# Scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report, confusion_matrix, 
    roc_curve, auc, precision_recall_curve,
    roc_auc_score
)
from sklearn.preprocessing import label_binarize
from sklearn.utils.class_weight import compute_class_weight

print(f"TensorFlow version: {tf.__version__}")
print(f"Keras version: {keras.__version__}")

# ============================================================================
# CELL 2: Reproducibility & Hardware Detection
# ============================================================================

def set_seeds(seed=42):
    """Set seeds for reproducibility"""
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)
    
set_seeds(42)

# Hardware detection
print("GPU Available:", tf.config.list_physical_devices('GPU'))
print("Number of GPUs:", len(tf.config.list_physical_devices('GPU')))

# Enable mixed precision (optional - for faster training on modern GPUs)
# tf.keras.mixed_precision.set_global_policy('mixed_float16')

# ============================================================================
# CELL 3: Configuration
# ============================================================================

class Config:
    # Paths
    DATA_ROOT = '/kaggle/input/isic-2019'  # Update this path
    OUTPUT_DIR = 'output'
    MODEL_SAVE_PATH = 'webapp/models/efficientnetb3_isic.h5'
    
    # Model parameters
    IMG_SIZE = (300, 300)
    BATCH_SIZE = 32
    EPOCHS = 50
    LEARNING_RATE = 1e-4
    
    # Class names (ISIC 2019)
    CLASS_NAMES = [
        'MEL',   # Melanoma
        'NV',    # Melanocytic nevus  
        'BCC',   # Basal cell carcinoma
        'AK',    # Actinic keratosis
        'BKL',   # Benign keratosis
        'DF',    # Dermatofibroma
        'VASC',  # Vascular lesion
        'SCC'    # Squamous cell carcinoma
    ]
    
    NUM_CLASSES = len(CLASS_NAMES)
    
    # Training parameters
    VALIDATION_SPLIT = 0.2
    EARLY_STOPPING_PATIENCE = 10
    REDUCE_LR_PATIENCE = 5
    
    # Augmentation parameters
    ROTATION_RANGE = 30
    WIDTH_SHIFT_RANGE = 0.2
    HEIGHT_SHIFT_RANGE = 0.2
    ZOOM_RANGE = 0.2
    BRIGHTNESS_RANGE = [0.8, 1.2]
    
config = Config()

# Create output directories
os.makedirs(config.OUTPUT_DIR, exist_ok=True)
os.makedirs(os.path.dirname(config.MODEL_SAVE_PATH), exist_ok=True)

print(f"Configuration loaded:")
print(f"  Image size: {config.IMG_SIZE}")
print(f"  Batch size: {config.BATCH_SIZE}")
print(f"  Epochs: {config.EPOCHS}")
print(f"  Number of classes: {config.NUM_CLASSES}")


# ============================================================================
# CELL 4: Data Loading Functions
# ============================================================================

def load_data_from_folders(data_root, img_size=(300, 300)):
    """
    Load images from folder structure: data_root/class_name/*.jpg
    Returns: images, labels, file_paths
    """
    images = []
    labels = []
    file_paths = []
    
    print(f"Loading data from: {data_root}")
    
    for class_idx, class_name in enumerate(config.CLASS_NAMES):
        class_dir = os.path.join(data_root, class_name)
        
        if not os.path.exists(class_dir):
            print(f"Warning: Directory not found: {class_dir}")
            continue
            
        image_files = list(Path(class_dir).glob('*.jpg')) + \
                     list(Path(class_dir).glob('*.jpeg')) + \
                     list(Path(class_dir).glob('*.png'))
        
        print(f"  {class_name}: {len(image_files)} images")
        
        for img_path in image_files:
            try:
                # Load and resize image
                img = cv2.imread(str(img_path))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img = cv2.resize(img, img_size)
                
                images.append(img)
                labels.append(class_idx)
                file_paths.append(str(img_path))
            except Exception as e:
                print(f"Error loading {img_path}: {e}")
    
    images = np.array(images, dtype=np.float32)
    labels = np.array(labels)
    
    print(f"\nTotal images loaded: {len(images)}")
    print(f"Image shape: {images.shape}")
    print(f"Labels shape: {labels.shape}")
    
    return images, labels, file_paths


def load_data_from_csv(csv_path, image_dir, img_size=(300, 300)):
    """
    Alternative: Load data from CSV file
    CSV should have columns: 'image_name', 'label'
    """
    df = pd.read_csv(csv_path)
    
    images = []
    labels = []
    
    print(f"Loading {len(df)} images from CSV...")
    
    for idx, row in df.iterrows():
        img_path = os.path.join(image_dir, row['image_name'])
        
        try:
            img = cv2.imread(img_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, img_size)
            
            images.append(img)
            
            # Convert label name to index
            label_idx = config.CLASS_NAMES.index(row['label'])
            labels.append(label_idx)
            
        except Exception as e:
            print(f"Error loading {img_path}: {e}")
    
    return np.array(images, dtype=np.float32), np.array(labels)

# ============================================================================
# CELL 5: Load and Split Data
# ============================================================================

# Load data (choose one method)
X, y, file_paths = load_data_from_folders(config.DATA_ROOT, config.IMG_SIZE)

# Normalize images to [0, 1]
X = X / 255.0

# Stratified train/validation split
X_train, X_val, y_train, y_val = train_test_split(
    X, y, 
    test_size=config.VALIDATION_SPLIT,
    stratify=y,
    random_state=42
)

print(f"\nData split:")
print(f"  Training set: {X_train.shape[0]} images")
print(f"  Validation set: {X_val.shape[0]} images")

# Class distribution
print(f"\nTraining set class distribution:")
unique, counts = np.unique(y_train, return_counts=True)
for class_idx, count in zip(unique, counts):
    print(f"  {config.CLASS_NAMES[class_idx]}: {count} ({count/len(y_train)*100:.1f}%)")

# Convert labels to categorical
y_train_cat = to_categorical(y_train, config.NUM_CLASSES)
y_val_cat = to_categorical(y_val, config.NUM_CLASSES)


# ============================================================================
# CELL 6: Data Augmentation
# ============================================================================

# Create data generators with augmentation
train_datagen = ImageDataGenerator(
    rotation_range=config.ROTATION_RANGE,
    width_shift_range=config.WIDTH_SHIFT_RANGE,
    height_shift_range=config.HEIGHT_SHIFT_RANGE,
    zoom_range=config.ZOOM_RANGE,
    brightness_range=config.BRIGHTNESS_RANGE,
    horizontal_flip=True,
    vertical_flip=True,
    fill_mode='nearest'
)

# Validation data generator (no augmentation)
val_datagen = ImageDataGenerator()

# Create generators
train_generator = train_datagen.flow(
    X_train, y_train_cat,
    batch_size=config.BATCH_SIZE,
    shuffle=True
)

val_generator = val_datagen.flow(
    X_val, y_val_cat,
    batch_size=config.BATCH_SIZE,
    shuffle=False
)

print(f"Data generators created:")
print(f"  Training batches per epoch: {len(train_generator)}")
print(f"  Validation batches per epoch: {len(val_generator)}")

# ============================================================================
# CELL 7: Visualize Augmented Images
# ============================================================================

def show_augmented_images(generator, num_images=9):
    """Display augmented images"""
    fig, axes = plt.subplots(3, 3, figsize=(12, 12))
    axes = axes.ravel()
    
    # Get one batch
    batch_x, batch_y = next(generator)
    
    for i in range(min(num_images, len(batch_x))):
        axes[i].imshow(batch_x[i])
        class_idx = np.argmax(batch_y[i])
        axes[i].set_title(f"{config.CLASS_NAMES[class_idx]}")
        axes[i].axis('off')
    
    plt.tight_layout()
    plt.savefig(f'{config.OUTPUT_DIR}/augmented_samples.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("Augmented samples saved to output/augmented_samples.png")

# Show augmented examples
show_augmented_images(train_generator)

# ============================================================================
# CELL 8: Compute Class Weights
# ============================================================================

# Compute class weights to handle imbalance
class_weights = compute_class_weight(
    class_weight='balanced',
    classes=np.unique(y_train),
    y=y_train
)

class_weight_dict = dict(enumerate(class_weights))

print("Class weights (for handling imbalance):")
for class_idx, weight in class_weight_dict.items():
    print(f"  {config.CLASS_NAMES[class_idx]}: {weight:.3f}")


# ============================================================================
# CELL 9: Build EfficientNetB3 Model
# ============================================================================

def build_efficientnetb3_model(
    input_shape=(300, 300, 3),
    num_classes=8,
    dropout_rate=0.3,
    use_imagenet_weights=True
):
    """
    Build EfficientNetB3 model with custom classifier
    """
    # Load pre-trained EfficientNetB3 (without top layers)
    base_model = EfficientNetB3(
        include_top=False,
        weights='imagenet' if use_imagenet_weights else None,
        input_shape=input_shape,
        pooling=None
    )
    
    # Freeze base model initially (for transfer learning)
    base_model.trainable = False
    
    # Build model
    inputs = layers.Input(shape=input_shape)
    
    # Base model
    x = base_model(inputs, training=False)
    
    # Custom classifier head
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(dropout_rate)(x)
    x = layers.Dense(512, activation='relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(dropout_rate / 2)(x)
    outputs = layers.Dense(num_classes, activation='softmax')(x)
    
    model = models.Model(inputs, outputs)
    
    return model, base_model


# Build model
model, base_model = build_efficientnetb3_model(
    input_shape=(*config.IMG_SIZE, 3),
    num_classes=config.NUM_CLASSES,
    dropout_rate=0.3
)

# Compile model
model.compile(
    optimizer=optimizers.Adam(learning_rate=config.LEARNING_RATE),
    loss='categorical_crossentropy',
    metrics=['accuracy', tf.keras.metrics.AUC(name='auc')]
)

# Model summary
print("\nModel Summary:")
print(f"Total parameters: {model.count_params():,}")
print(f"Trainable parameters: {sum([tf.size(w).numpy() for w in model.trainable_weights]):,}")
print(f"Non-trainable parameters: {sum([tf.size(w).numpy() for w in model.non_trainable_weights]):,}")

model.summary()

# ============================================================================
# CELL 10: Training Callbacks
# ============================================================================

# Create callbacks
checkpoint_callback = callbacks.ModelCheckpoint(
    filepath=config.MODEL_SAVE_PATH,
    monitor='val_accuracy',
    save_best_only=True,
    save_weights_only=False,
    mode='max',
    verbose=1
)

early_stopping = callbacks.EarlyStopping(
    monitor='val_loss',
    patience=config.EARLY_STOPPING_PATIENCE,
    restore_best_weights=True,
    verbose=1
)

reduce_lr = callbacks.ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.5,
    patience=config.REDUCE_LR_PATIENCE,
    min_lr=1e-7,
    verbose=1
)

tensorboard_callback = callbacks.TensorBoard(
    log_dir=f'{config.OUTPUT_DIR}/logs',
    histogram_freq=1,
    write_graph=True
)

csv_logger = callbacks.CSVLogger(
    f'{config.OUTPUT_DIR}/training_log.csv',
    append=False
)

callback_list = [
    checkpoint_callback,
    early_stopping,
    reduce_lr,
    tensorboard_callback,
    csv_logger
]

print("Callbacks configured:")
for cb in callback_list:
    print(f"  - {cb.__class__.__name__}")


# ============================================================================
# CELL 11: Phase 1 Training - Frozen Base Model
# ============================================================================

print("\n" + "="*80)
print("PHASE 1: Training with frozen base model (transfer learning)")
print("="*80)

# Train with frozen base
history_phase1 = model.fit(
    train_generator,
    epochs=15,  # Initial training epochs
    validation_data=val_generator,
    class_weight=class_weight_dict,
    callbacks=callback_list,
    verbose=1
)

print("\nPhase 1 training completed!")

# ============================================================================
# CELL 12: Phase 2 Training - Fine-tuning
# ============================================================================

print("\n" + "="*80)
print("PHASE 2: Fine-tuning - Unfreezing last layers")
print("="*80)

# Unfreeze the last N layers of base model for fine-tuning
base_model.trainable = True

# Freeze all layers except the last 30
for layer in base_model.layers[:-30]:
    layer.trainable = False

print(f"Trainable layers: {sum([1 for layer in model.layers if layer.trainable])}")
print(f"Total trainable parameters: {sum([tf.size(w).numpy() for w in model.trainable_weights]):,}")

# Recompile with lower learning rate for fine-tuning
model.compile(
    optimizer=optimizers.Adam(learning_rate=config.LEARNING_RATE / 10),
    loss='categorical_crossentropy',
    metrics=['accuracy', tf.keras.metrics.AUC(name='auc')]
)

# Continue training
history_phase2 = model.fit(
    train_generator,
    epochs=config.EPOCHS,
    initial_epoch=len(history_phase1.history['loss']),
    validation_data=val_generator,
    class_weight=class_weight_dict,
    callbacks=callback_list,
    verbose=1
)

print("\nPhase 2 training completed!")

# ============================================================================
# CELL 13: Plot Training History
# ============================================================================

def plot_training_history(history1, history2=None):
    """Plot training and validation metrics"""
    
    # Combine histories if phase 2 exists
    if history2:
        history_dict = {
            'loss': history1.history['loss'] + history2.history['loss'],
            'val_loss': history1.history['val_loss'] + history2.history['val_loss'],
            'accuracy': history1.history['accuracy'] + history2.history['accuracy'],
            'val_accuracy': history1.history['val_accuracy'] + history2.history['val_accuracy'],
        }
        phase1_epochs = len(history1.history['loss'])
    else:
        history_dict = history1.history
        phase1_epochs = None
    
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    
    # Plot loss
    axes[0].plot(history_dict['loss'], label='Training Loss', linewidth=2)
    axes[0].plot(history_dict['val_loss'], label='Validation Loss', linewidth=2)
    if phase1_epochs:
        axes[0].axvline(x=phase1_epochs, color='red', linestyle='--', 
                       label='Fine-tuning starts', linewidth=2)
    axes[0].set_xlabel('Epoch', fontsize=12)
    axes[0].set_ylabel('Loss', fontsize=12)
    axes[0].set_title('Model Loss', fontsize=14, fontweight='bold')
    axes[0].legend(fontsize=10)
    axes[0].grid(True, alpha=0.3)
    
    # Plot accuracy
    axes[1].plot(history_dict['accuracy'], label='Training Accuracy', linewidth=2)
    axes[1].plot(history_dict['val_accuracy'], label='Validation Accuracy', linewidth=2)
    if phase1_epochs:
        axes[1].axvline(x=phase1_epochs, color='red', linestyle='--',
                       label='Fine-tuning starts', linewidth=2)
    axes[1].set_xlabel('Epoch', fontsize=12)
    axes[1].set_ylabel('Accuracy', fontsize=12)
    axes[1].set_title('Model Accuracy', fontsize=14, fontweight='bold')
    axes[1].legend(fontsize=10)
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'{config.OUTPUT_DIR}/training_history.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"Training history plot saved to {config.OUTPUT_DIR}/training_history.png")

# Plot combined training history
plot_training_history(history_phase1, history_phase2)


# ============================================================================
# CELL 14: Load Best Model and Evaluate
# ============================================================================

# Load the best model
best_model = keras.models.load_model(config.MODEL_SAVE_PATH)
print(f"Best model loaded from: {config.MODEL_SAVE_PATH}")

# Make predictions on validation set
y_pred_probs = best_model.predict(X_val, batch_size=config.BATCH_SIZE, verbose=1)
y_pred = np.argmax(y_pred_probs, axis=1)

# Calculate metrics
val_accuracy = np.mean(y_pred == y_val)
print(f"\nValidation Accuracy: {val_accuracy:.4f} ({val_accuracy*100:.2f}%)")

# ============================================================================
# CELL 15: Confusion Matrix
# ============================================================================

def plot_confusion_matrix(y_true, y_pred, class_names, normalize=False):
    """Plot confusion matrix"""
    cm = confusion_matrix(y_true, y_pred)
    
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        fmt = '.2f'
        title = 'Normalized Confusion Matrix'
    else:
        fmt = 'd'
        title = 'Confusion Matrix'
    
    plt.figure(figsize=(12, 10))
    sns.heatmap(cm, annot=True, fmt=fmt, cmap='Blues',
                xticklabels=class_names, yticklabels=class_names,
                cbar_kws={'label': 'Count' if not normalize else 'Proportion'})
    plt.title(title, fontsize=16, fontweight='bold', pad=20)
    plt.ylabel('True Label', fontsize=12)
    plt.xlabel('Predicted Label', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    
    filename = f'{config.OUTPUT_DIR}/confusion_matrix{"_normalized" if normalize else ""}.png'
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.show()
    print(f"Confusion matrix saved to {filename}")

# Plot both regular and normalized confusion matrices
plot_confusion_matrix(y_val, y_pred, config.CLASS_NAMES, normalize=False)
plot_confusion_matrix(y_val, y_pred, config.CLASS_NAMES, normalize=True)

# ============================================================================
# CELL 16: Classification Report
# ============================================================================

# Generate classification report
report = classification_report(
    y_val, y_pred,
    target_names=config.CLASS_NAMES,
    digits=4
)

print("\nClassification Report:")
print("="*80)
print(report)

# Save report to file
with open(f'{config.OUTPUT_DIR}/classification_report.txt', 'w') as f:
    f.write("Classification Report\n")
    f.write("="*80 + "\n")
    f.write(report)

# Create detailed report DataFrame
report_dict = classification_report(
    y_val, y_pred,
    target_names=config.CLASS_NAMES,
    output_dict=True
)

report_df = pd.DataFrame(report_dict).transpose()
report_df.to_csv(f'{config.OUTPUT_DIR}/classification_report.csv')
print(f"\nClassification report saved to {config.OUTPUT_DIR}/classification_report.csv")


# ============================================================================
# CELL 17: ROC Curves and AUC
# ============================================================================

def plot_roc_curves(y_true, y_pred_probs, class_names):
    """Plot ROC curves for all classes"""
    
    # Binarize labels
    y_true_bin = label_binarize(y_true, classes=range(len(class_names)))
    
    # Compute ROC curve and AUC for each class
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    
    for i in range(len(class_names)):
        fpr[i], tpr[i], _ = roc_curve(y_true_bin[:, i], y_pred_probs[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])
    
    # Compute micro-average ROC curve and AUC
    fpr["micro"], tpr["micro"], _ = roc_curve(y_true_bin.ravel(), y_pred_probs.ravel())
    roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])
    
    # Compute macro-average ROC curve and AUC
    all_fpr = np.unique(np.concatenate([fpr[i] for i in range(len(class_names))]))
    mean_tpr = np.zeros_like(all_fpr)
    for i in range(len(class_names)):
        mean_tpr += np.interp(all_fpr, fpr[i], tpr[i])
    mean_tpr /= len(class_names)
    fpr["macro"] = all_fpr
    tpr["macro"] = mean_tpr
    roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])
    
    # Plot all ROC curves
    plt.figure(figsize=(12, 10))
    
    # Plot micro and macro averages
    plt.plot(fpr["micro"], tpr["micro"],
             label=f'Micro-average (AUC = {roc_auc["micro"]:.3f})',
             color='deeppink', linestyle=':', linewidth=3)
    
    plt.plot(fpr["macro"], tpr["macro"],
             label=f'Macro-average (AUC = {roc_auc["macro"]:.3f})',
             color='navy', linestyle=':', linewidth=3)
    
    # Plot ROC curve for each class
    colors = plt.cm.Set3(np.linspace(0, 1, len(class_names)))
    for i, color in zip(range(len(class_names)), colors):
        plt.plot(fpr[i], tpr[i], color=color, linewidth=2,
                label=f'{class_names[i]} (AUC = {roc_auc[i]:.3f})')
    
    plt.plot([0, 1], [0, 1], 'k--', linewidth=2, label='Random Classifier')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=12)
    plt.ylabel('True Positive Rate', fontsize=12)
    plt.title('ROC Curves - Multi-class Classification', fontsize=14, fontweight='bold')
    plt.legend(loc="lower right", fontsize=9)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'{config.OUTPUT_DIR}/roc_curves.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"ROC curves saved to {config.OUTPUT_DIR}/roc_curves.png")
    print(f"\nAUC Scores:")
    print(f"  Micro-average: {roc_auc['micro']:.4f}")
    print(f"  Macro-average: {roc_auc['macro']:.4f}")
    for i, class_name in enumerate(class_names):
        print(f"  {class_name}: {roc_auc[i]:.4f}")
    
    return roc_auc

# Plot ROC curves
roc_auc_scores = plot_roc_curves(y_val, y_pred_probs, config.CLASS_NAMES)

# ============================================================================
# CELL 18: Precision-Recall Curves
# ============================================================================

def plot_precision_recall_curves(y_true, y_pred_probs, class_names):
    """Plot precision-recall curves for all classes"""
    
    # Binarize labels
    y_true_bin = label_binarize(y_true, classes=range(len(class_names)))
    
    plt.figure(figsize=(12, 10))
    
    colors = plt.cm.Set3(np.linspace(0, 1, len(class_names)))
    
    for i, color in zip(range(len(class_names)), colors):
        precision, recall, _ = precision_recall_curve(y_true_bin[:, i], y_pred_probs[:, i])
        pr_auc = auc(recall, precision)
        
        plt.plot(recall, precision, color=color, linewidth=2,
                label=f'{class_names[i]} (AUC = {pr_auc:.3f})')
    
    plt.xlabel('Recall', fontsize=12)
    plt.ylabel('Precision', fontsize=12)
    plt.title('Precision-Recall Curves', fontsize=14, fontweight='bold')
    plt.legend(loc="best", fontsize=9)
    plt.grid(True, alpha=0.3)
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.tight_layout()
    plt.savefig(f'{config.OUTPUT_DIR}/precision_recall_curves.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"Precision-recall curves saved to {config.OUTPUT_DIR}/precision_recall_curves.png")

# Plot precision-recall curves
plot_precision_recall_curves(y_val, y_pred_probs, config.CLASS_NAMES)


# ============================================================================
# CELL 19: Grad-CAM Implementation
# ============================================================================

def make_gradcam_heatmap(img_array, model, last_conv_layer_name, pred_index=None):
    """
    Generate Grad-CAM heatmap for a given image
    """
    # Create a model that maps the input image to the activations
    # of the last conv layer as well as the output predictions
    grad_model = tf.keras.models.Model(
        [model.inputs],
        [model.get_layer(last_conv_layer_name).output, model.output]
    )
    
    # Compute the gradient of the top predicted class for our input image
    # with respect to the activations of the last conv layer
    with tf.GradientTape() as tape:
        last_conv_layer_output, preds = grad_model(img_array)
        if pred_index is None:
            pred_index = tf.argmax(preds[0])
        class_channel = preds[:, pred_index]
    
    # Gradient of the output neuron with regard to the output feature map
    grads = tape.gradient(class_channel, last_conv_layer_output)
    
    # Vector of mean intensity of the gradient over a specific feature map channel
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
    
    # Multiply each channel in the feature map array
    # by "how important this channel is" with regard to the top predicted class
    last_conv_layer_output = last_conv_layer_output[0]
    heatmap = last_conv_layer_output @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)
    
    # Normalize the heatmap between 0 & 1
    heatmap = tf.maximum(heatmap, 0) / tf.math.reduce_max(heatmap)
    return heatmap.numpy()


def save_and_display_gradcam(img, heatmap, cam_path, alpha=0.4):
    """
    Overlay Grad-CAM heatmap on original image
    """
    # Rescale heatmap to a range 0-255
    heatmap = np.uint8(255 * heatmap)
    
    # Use jet colormap to colorize heatmap
    jet = plt.cm.get_cmap("jet")
    jet_colors = jet(np.arange(256))[:, :3]
    jet_heatmap = jet_colors[heatmap]
    
    # Create an image with RGB colorized heatmap
    jet_heatmap = tf.keras.preprocessing.image.array_to_img(jet_heatmap)
    jet_heatmap = jet_heatmap.resize((img.shape[1], img.shape[0]))
    jet_heatmap = tf.keras.preprocessing.image.img_to_array(jet_heatmap)
    
    # Superimpose the heatmap on original image
    superimposed_img = jet_heatmap * alpha + img * 255
    superimposed_img = tf.keras.preprocessing.image.array_to_img(superimposed_img)
    
    # Save the superimposed image
    superimposed_img.save(cam_path)
    
    return superimposed_img


def visualize_gradcam_samples(model, X_samples, y_samples, num_samples=6):
    """
    Visualize Grad-CAM for multiple samples
    """
    # Find the last convolutional layer
    last_conv_layer_name = None
    for layer in reversed(model.layers):
        if 'conv' in layer.name.lower():
            last_conv_layer_name = layer.name
            break
    
    if last_conv_layer_name is None:
        print("No convolutional layer found!")
        return
    
    print(f"Using layer: {last_conv_layer_name} for Grad-CAM")
    
    fig, axes = plt.subplots(num_samples, 3, figsize=(12, num_samples * 3))
    
    for i in range(min(num_samples, len(X_samples))):
        img = X_samples[i]
        true_label = y_samples[i]
        
        # Prepare image for model
        img_array = np.expand_dims(img, axis=0)
        
        # Make prediction
        preds = model.predict(img_array, verbose=0)
        pred_label = np.argmax(preds[0])
        confidence = np.max(preds[0])
        
        # Generate Grad-CAM heatmap
        heatmap = make_gradcam_heatmap(img_array, model, last_conv_layer_name)
        
        # Save and get overlay
        cam_path = f'{config.OUTPUT_DIR}/gradcam_sample_{i}.jpg'
        overlay = save_and_display_gradcam(img, heatmap, cam_path)
        
        # Plot original image
        axes[i, 0].imshow(img)
        axes[i, 0].set_title(f'Original\nTrue: {config.CLASS_NAMES[true_label]}', fontsize=10)
        axes[i, 0].axis('off')
        
        # Plot heatmap
        axes[i, 1].imshow(heatmap, cmap='jet')
        axes[i, 1].set_title(f'Grad-CAM Heatmap', fontsize=10)
        axes[i, 1].axis('off')
        
        # Plot overlay
        axes[i, 2].imshow(overlay)
        axes[i, 2].set_title(f'Overlay\nPred: {config.CLASS_NAMES[pred_label]}\nConf: {confidence:.2f}', 
                            fontsize=10)
        axes[i, 2].axis('off')
    
    plt.tight_layout()
    plt.savefig(f'{config.OUTPUT_DIR}/gradcam_visualization.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"Grad-CAM visualizations saved to {config.OUTPUT_DIR}/")

# Select random samples for Grad-CAM visualization
sample_indices = np.random.choice(len(X_val), size=6, replace=False)
X_samples = X_val[sample_indices]
y_samples = y_val[sample_indices]

# Visualize Grad-CAM
visualize_gradcam_samples(best_model, X_samples, y_samples, num_samples=6)


# ============================================================================
# CELL 20: Save Predictions
# ============================================================================

# Create predictions DataFrame
predictions_df = pd.DataFrame({
    'true_label': [config.CLASS_NAMES[i] for i in y_val],
    'predicted_label': [config.CLASS_NAMES[i] for i in y_pred],
    'correct': y_val == y_pred,
    'confidence': np.max(y_pred_probs, axis=1)
})

# Add probability for each class
for i, class_name in enumerate(config.CLASS_NAMES):
    predictions_df[f'prob_{class_name}'] = y_pred_probs[:, i]

# Save predictions
predictions_df.to_csv(f'{config.OUTPUT_DIR}/predictions.csv', index=False)
print(f"Predictions saved to {config.OUTPUT_DIR}/predictions.csv")

# Show sample predictions
print("\nSample predictions:")
print(predictions_df.head(10))

# ============================================================================
# CELL 21: Test-Time Augmentation (TTA)
# ============================================================================

def predict_with_tta(model, image, num_augmentations=10):
    """
    Perform test-time augmentation for more robust predictions
    """
    predictions = []
    
    # Original prediction
    img_array = np.expand_dims(image, axis=0)
    pred = model.predict(img_array, verbose=0)
    predictions.append(pred[0])
    
    # Augmented predictions
    datagen = ImageDataGenerator(
        rotation_range=15,
        width_shift_range=0.1,
        height_shift_range=0.1,
        zoom_range=0.1,
        horizontal_flip=True,
        vertical_flip=True
    )
    
    for _ in range(num_augmentations - 1):
        # Generate augmented image
        aug_iter = datagen.flow(img_array, batch_size=1)
        aug_img = next(aug_iter)
        
        # Predict
        pred = model.predict(aug_img, verbose=0)
        predictions.append(pred[0])
    
    # Average predictions
    avg_prediction = np.mean(predictions, axis=0)
    
    return avg_prediction


# Example TTA usage
print("\nTest-Time Augmentation Example:")
print("="*80)

sample_img = X_val[0]
true_label = y_val[0]

# Regular prediction
regular_pred = best_model.predict(np.expand_dims(sample_img, axis=0), verbose=0)[0]
regular_class = np.argmax(regular_pred)
regular_conf = np.max(regular_pred)

# TTA prediction
tta_pred = predict_with_tta(best_model, sample_img, num_augmentations=10)
tta_class = np.argmax(tta_pred)
tta_conf = np.max(tta_pred)

print(f"True label: {config.CLASS_NAMES[true_label]}")
print(f"\nRegular prediction: {config.CLASS_NAMES[regular_class]} (confidence: {regular_conf:.4f})")
print(f"TTA prediction: {config.CLASS_NAMES[tta_class]} (confidence: {tta_conf:.4f})")


# ============================================================================
# CELL 22: Single Image Inference Example
# ============================================================================

def predict_single_image(model, image_path, img_size=(300, 300)):
    """
    Load and predict a single image
    """
    # Load image
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img, img_size)
    img_normalized = img_resized / 255.0
    
    # Predict
    img_array = np.expand_dims(img_normalized, axis=0)
    predictions = model.predict(img_array, verbose=0)[0]
    
    # Get top prediction
    pred_class_idx = np.argmax(predictions)
    pred_class = config.CLASS_NAMES[pred_class_idx]
    confidence = predictions[pred_class_idx]
    
    # Display results
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Show image
    axes[0].imshow(img_resized)
    axes[0].set_title(f'Input Image\nPrediction: {pred_class}\nConfidence: {confidence:.2%}',
                     fontsize=12, fontweight='bold')
    axes[0].axis('off')
    
    # Show probability distribution
    axes[1].barh(config.CLASS_NAMES, predictions, color='skyblue')
    axes[1].set_xlabel('Probability', fontsize=12)
    axes[1].set_title('Class Probabilities', fontsize=12, fontweight='bold')
    axes[1].set_xlim([0, 1])
    
    # Highlight top prediction
    axes[1].barh(pred_class, confidence, color='orange')
    
    plt.tight_layout()
    plt.savefig(f'{config.OUTPUT_DIR}/single_prediction_example.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    # Print detailed results
    print("\nPrediction Results:")
    print("="*80)
    print(f"Predicted Class: {pred_class}")
    print(f"Confidence: {confidence:.4f} ({confidence*100:.2f}%)")
    print("\nAll class probabilities:")
    for i, (class_name, prob) in enumerate(zip(config.CLASS_NAMES, predictions)):
        print(f"  {class_name:10s}: {prob:.4f} ({prob*100:.2f}%)")
    
    return pred_class, confidence, predictions


# Example: Predict on a validation image
if len(X_val) > 0:
    print("\nSingle Image Inference Example:")
    print("="*80)
    
    # Use a random validation image
    sample_idx = np.random.randint(0, len(X_val))
    sample_img = X_val[sample_idx]
    true_label = y_val[sample_idx]
    
    # Save sample image temporarily
    temp_img_path = f'{config.OUTPUT_DIR}/temp_sample.jpg'
    cv2.imwrite(temp_img_path, cv2.cvtColor((sample_img * 255).astype(np.uint8), cv2.COLOR_RGB2BGR))
    
    # Predict
    pred_class, confidence, probs = predict_single_image(best_model, temp_img_path)
    
    print(f"\nTrue Label: {config.CLASS_NAMES[true_label]}")
    print(f"Prediction Correct: {pred_class == config.CLASS_NAMES[true_label]}")

# ============================================================================
# CELL 23: Model Summary and Export Information
# ============================================================================

print("\n" + "="*80)
print("TRAINING COMPLETE - MODEL SUMMARY")
print("="*80)

print(f"\nModel saved to: {config.MODEL_SAVE_PATH}")
print(f"Model size: {os.path.getsize(config.MODEL_SAVE_PATH) / (1024*1024):.2f} MB")

print(f"\nFinal Metrics:")
print(f"  Validation Accuracy: {val_accuracy:.4f} ({val_accuracy*100:.2f}%)")
print(f"  Macro-average AUC: {roc_auc_scores['macro']:.4f}")
print(f"  Micro-average AUC: {roc_auc_scores['micro']:.4f}")

print(f"\nPer-class AUC scores:")
for i, class_name in enumerate(config.CLASS_NAMES):
    print(f"  {class_name:10s}: {roc_auc_scores[i]:.4f}")

print(f"\nOutput files saved to: {config.OUTPUT_DIR}/")
print("  - training_history.png")
print("  - confusion_matrix.png")
print("  - confusion_matrix_normalized.png")
print("  - roc_curves.png")
print("  - precision_recall_curves.png")
print("  - gradcam_visualization.png")
print("  - classification_report.csv")
print("  - predictions.csv")
print("  - training_log.csv")

print("\n" + "="*80)
print("Model is ready for deployment!")
print("="*80)

# ============================================================================
# CELL 24: Additional Tips and Improvements
# ============================================================================

print("\n" + "="*80)
print("TIPS FOR IMPROVING MODEL ACCURACY")
print("="*80)

tips = """
1. TRANSFER LEARNING STRATEGY:
   - Start with frozen base model (done ✓)
   - Gradually unfreeze layers from top to bottom
   - Use progressive unfreezing: unfreeze 10 layers, train, unfreeze 10 more, etc.

2. LOSS FUNCTIONS FOR IMBALANCED DATA:
   - Focal Loss: Focuses on hard examples
   - Label Smoothing: Prevents overconfidence
   - Class-weighted loss (already implemented ✓)

3. DATA AUGMENTATION:
   - Add more aggressive augmentation for minority classes
   - Use mixup or cutmix augmentation
   - Apply domain-specific augmentations (hair removal, color normalization)

4. ENSEMBLE METHODS:
   - Train multiple models with different seeds
   - Use different architectures (EfficientNetB4, B5, ResNet, etc.)
   - Average predictions from multiple models

5. HYPERPARAMETER TUNING:
   - Learning rate scheduling (cosine annealing, warm restarts)
   - Experiment with different optimizers (AdamW, SGD with momentum)
   - Adjust dropout rates and regularization

6. DATA PREPROCESSING:
   - Apply hair removal algorithms
   - Normalize images using dataset statistics
   - Use advanced preprocessing (CLAHE, color constancy)

7. TEST-TIME AUGMENTATION:
   - Use TTA for final predictions (implemented above ✓)
   - Average predictions from multiple augmented versions

8. MODEL ARCHITECTURE:
   - Try larger EfficientNet variants (B4, B5, B6)
   - Experiment with attention mechanisms
   - Use multi-scale feature fusion
"""

print(tips)

print("\n" + "="*80)
print("END OF TRAINING SCRIPT")
print("="*80)
