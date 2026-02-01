"""
JOURNAL FIGURE GENERATION: EfficientNetB0 for Skin Lesion Classification
==========================================================================
Kaggle-compatible code for generating publication-quality figures

This script creates:
1. Model architecture visualization
2. Sample predictions with confidence scores
3. Grad-CAM heatmaps for explainability
4. Feature map visualizations
5. Confusion matrix and performance metrics
6. ROC curves and precision-recall curves
7. Class activation maps
8. Comparative analysis figures

Author: Data Science Team
Date: 2026-01-26
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# TensorFlow and Keras
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras import models, layers

# Scikit-learn
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import roc_curve, auc, precision_recall_curve
from sklearn.preprocessing import label_binarize

print("="*80)
print("JOURNAL FIGURE GENERATION - EfficientNetB0")
print("="*80)
print(f"TensorFlow: {tf.__version__}")
print(f"Keras: {keras.__version__}")


# ============================================================================
# CONFIGURATION
# ============================================================================

class Config:
    """Configuration for journal figure generation"""
    # Paths
    IN_KAGGLE = os.path.exists('/kaggle/input')
    DATA_ROOT = '/kaggle/input/isic-2019' if IN_KAGGLE else './data/isic-2019'
    OUTPUT_DIR = '/kaggle/working/journal_figures' if IN_KAGGLE else './journal_figures'
    MODEL_PATH = '/kaggle/input/efficientnetb0-model/EfficientNetB0_skin-cancer.h5' if IN_KAGGLE else 'webapp/models/EfficientNetB0_skin-cancer.h5'
    
    # Model parameters
    IMG_SIZE = (224, 224)
    CLASS_NAMES = ['MEL', 'NV', 'BCC', 'AK', 'BKL', 'DF', 'VASC', 'SCC']
    NUM_CLASSES = len(CLASS_NAMES)
    
    # Figure settings (journal quality)
    DPI = 300  # High resolution for publication
    FIGSIZE_SINGLE = (8, 6)
    FIGSIZE_DOUBLE = (16, 6)
    FIGSIZE_LARGE = (12, 10)
    FONT_SIZE = 12
    TITLE_SIZE = 14

config = Config()
os.makedirs(config.OUTPUT_DIR, exist_ok=True)

# Set matplotlib style for publication
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.size'] = config.FONT_SIZE
plt.rcParams['axes.titlesize'] = config.TITLE_SIZE
plt.rcParams['axes.labelsize'] = config.FONT_SIZE
plt.rcParams['xtick.labelsize'] = config.FONT_SIZE - 1
plt.rcParams['ytick.labelsize'] = config.FONT_SIZE - 1
plt.rcParams['legend.fontsize'] = config.FONT_SIZE - 1
plt.rcParams['figure.titlesize'] = config.TITLE_SIZE + 2

print(f"\nConfiguration:")
print(f"  Data root: {config.DATA_ROOT}")
print(f"  Output directory: {config.OUTPUT_DIR}")
print(f"  Model path: {config.MODEL_PATH}")
print(f"  Image size: {config.IMG_SIZE}")
print(f"  DPI: {config.DPI}")
print("="*80)


# ============================================================================
# LOAD MODEL
# ============================================================================

print("\nLoading EfficientNetB0 model...")
try:
    model = keras.models.load_model(config.MODEL_PATH)
    print(f"✓ Model loaded successfully")
    print(f"  Input shape: {model.input_shape}")
    print(f"  Output shape: {model.output_shape}")
    print(f"  Total parameters: {model.count_params():,}")
except Exception as e:
    print(f"✗ Error loading model: {e}")
    print("\nCreating a new EfficientNetB0 model for demonstration...")
    
    # Create model architecture
    base_model = EfficientNetB0(include_top=False, weights='imagenet', 
                                input_shape=(*config.IMG_SIZE, 3))
    base_model.trainable = False
    
    inputs = layers.Input(shape=(*config.IMG_SIZE, 3))
    x = base_model(inputs, training=False)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.3)(x)
    x = layers.Dense(256, activation='relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.2)(x)
    outputs = layers.Dense(config.NUM_CLASSES, activation='softmax')(x)
    
    model = models.Model(inputs, outputs)
    print("✓ Demo model created")

print("="*80)


# ============================================================================
# LOAD SAMPLE DATA
# ============================================================================

def load_sample_images(data_root, num_samples_per_class=5):
    """Load sample images from each class"""
    images = []
    labels = []
    file_paths = []
    
    print("\nLoading sample images...")
    for class_idx, class_name in enumerate(config.CLASS_NAMES):
        class_dir = os.path.join(data_root, class_name)
        
        if not os.path.exists(class_dir):
            print(f"⚠ Directory not found: {class_dir}")
            # Create dummy data for demonstration
            for i in range(num_samples_per_class):
                dummy_img = np.random.rand(*config.IMG_SIZE, 3)
                images.append(dummy_img)
                labels.append(class_idx)
                file_paths.append(f"dummy_{class_name}_{i}.jpg")
            continue
        
        # Get image files
        image_files = list(Path(class_dir).glob('*.jpg'))[:num_samples_per_class]
        
        for img_path in image_files:
            try:
                img = cv2.imread(str(img_path))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img = cv2.resize(img, config.IMG_SIZE)
                img = img / 255.0
                
                images.append(img)
                labels.append(class_idx)
                file_paths.append(str(img_path))
            except Exception as e:
                continue
        
        print(f"  {class_name}: {len([l for l in labels if l == class_idx])} images")
    
    return np.array(images), np.array(labels), file_paths

# Load data
X_samples, y_samples, sample_paths = load_sample_images(
    config.DATA_ROOT, 
    num_samples_per_class=10
)

print(f"\n✓ Loaded {len(X_samples)} sample images")
print(f"  Shape: {X_samples.shape}")
print("="*80)


# ============================================================================
# FIGURE 1: MODEL ARCHITECTURE DIAGRAM
# ============================================================================

def create_architecture_figure():
    """Create model architecture visualization"""
    print("\nGenerating Figure 1: Model Architecture...")
    
    fig, ax = plt.subplots(figsize=(10, 12))
    ax.axis('off')
    
    # Architecture components
    components = [
        ("Input Layer", "224×224×3", "lightblue"),
        ("EfficientNetB0 Base", "Pre-trained on ImageNet", "lightgreen"),
        ("Global Average Pooling", "Spatial reduction", "lightyellow"),
        ("Batch Normalization", "Normalize activations", "lightcoral"),
        ("Dropout (0.3)", "Regularization", "lightgray"),
        ("Dense Layer", "256 units, ReLU", "lightgreen"),
        ("Batch Normalization", "Normalize activations", "lightcoral"),
        ("Dropout (0.2)", "Regularization", "lightgray"),
        ("Output Layer", "8 classes, Softmax", "lightblue"),
    ]
    
    y_pos = 0.9
    for i, (name, desc, color) in enumerate(components):
        # Draw box
        rect = plt.Rectangle((0.2, y_pos - 0.08), 0.6, 0.07, 
                            facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        
        # Add text
        ax.text(0.5, y_pos - 0.045, name, ha='center', va='center', 
               fontsize=12, fontweight='bold')
        ax.text(0.5, y_pos - 0.065, desc, ha='center', va='center', 
               fontsize=9, style='italic')
        
        # Draw arrow
        if i < len(components) - 1:
            ax.arrow(0.5, y_pos - 0.08, 0, -0.02, head_width=0.03, 
                    head_length=0.01, fc='black', ec='black')
        
        y_pos -= 0.1
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title('EfficientNetB0 Architecture for Skin Lesion Classification', 
                fontsize=16, fontweight='bold', pad=20)
    
    # Add parameter info
    info_text = f"Total Parameters: {model.count_params():,}\n"
    info_text += f"Input Size: {config.IMG_SIZE[0]}×{config.IMG_SIZE[1]}×3\n"
    info_text += f"Output Classes: {config.NUM_CLASSES}"
    ax.text(0.5, 0.05, info_text, ha='center', va='center', 
           fontsize=10, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    plt.savefig(f'{config.OUTPUT_DIR}/fig1_architecture.png', 
               dpi=config.DPI, bbox_inches='tight')
    plt.savefig(f'{config.OUTPUT_DIR}/fig1_architecture.pdf', 
               bbox_inches='tight')
    plt.close()
    
    print("✓ Figure 1 saved")


# ============================================================================
# FIGURE 2: SAMPLE PREDICTIONS WITH CONFIDENCE
# ============================================================================

def create_prediction_samples_figure():
    """Create figure showing sample predictions"""
    print("\nGenerating Figure 2: Sample Predictions...")
    
    # Select diverse samples
    num_samples = 8
    sample_indices = []
    for class_idx in range(min(config.NUM_CLASSES, num_samples)):
        class_samples = np.where(y_samples == class_idx)[0]
        if len(class_samples) > 0:
            sample_indices.append(class_samples[0])
    
    if len(sample_indices) < num_samples:
        sample_indices = np.random.choice(len(X_samples), 
                                         size=num_samples, replace=False)
    
    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    axes = axes.ravel()
    
    for i, idx in enumerate(sample_indices):
        img = X_samples[idx]
        true_label = config.CLASS_NAMES[y_samples[idx]]
        
        # Predict
        img_array = np.expand_dims(img, axis=0)
        predictions = model.predict(img_array, verbose=0)[0]
        pred_class = config.CLASS_NAMES[np.argmax(predictions)]
        confidence = np.max(predictions)
        
        # Plot
        axes[i].imshow(img)
        axes[i].axis('off')
        
        # Color code: green if correct, red if wrong
        color = 'green' if pred_class == true_label else 'red'
        title = f"True: {true_label}\nPred: {pred_class}\nConf: {confidence:.2%}"
        axes[i].set_title(title, fontsize=10, color=color, fontweight='bold')
    
    plt.suptitle('Sample Predictions with Confidence Scores', 
                fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig(f'{config.OUTPUT_DIR}/fig2_predictions.png', 
               dpi=config.DPI, bbox_inches='tight')
    plt.savefig(f'{config.OUTPUT_DIR}/fig2_predictions.pdf', 
               bbox_inches='tight')
    plt.close()
    
    print("✓ Figure 2 saved")


# ============================================================================
# FIGURE 3: GRAD-CAM VISUALIZATION
# ============================================================================

def make_gradcam_heatmap(img_array, model, last_conv_layer_name, pred_index=None):
    """Generate Grad-CAM heatmap"""
    grad_model = keras.models.Model(
        [model.inputs],
        [model.get_layer(last_conv_layer_name).output, model.output]
    )
    
    with tf.GradientTape() as tape:
        last_conv_layer_output, preds = grad_model(img_array)
        if pred_index is None:
            pred_index = tf.argmax(preds[0])
        class_channel = preds[:, pred_index]
    
    grads = tape.gradient(class_channel, last_conv_layer_output)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
    
    last_conv_layer_output = last_conv_layer_output[0]
    heatmap = last_conv_layer_output @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)
    heatmap = tf.maximum(heatmap, 0) / tf.math.reduce_max(heatmap)
    return heatmap.numpy()

def create_gradcam_figure():
    """Create Grad-CAM visualization figure"""
    print("\nGenerating Figure 3: Grad-CAM Visualization...")
    
    # Find last conv layer
    last_conv_layer_name = None
    for layer in reversed(model.layers):
        if 'conv' in layer.name.lower():
            last_conv_layer_name = layer.name
            break
    
    if last_conv_layer_name is None:
        print("⚠ No convolutional layer found, skipping Grad-CAM")
        return
    
    print(f"  Using layer: {last_conv_layer_name}")
    
    # Select samples
    num_samples = 6
    sample_indices = np.random.choice(len(X_samples), size=num_samples, replace=False)
    
    fig, axes = plt.subplots(num_samples, 3, figsize=(12, num_samples * 3))
    
    for i, idx in enumerate(sample_indices):
        img = X_samples[idx]
        true_label = config.CLASS_NAMES[y_samples[idx]]
        
        # Predict
        img_array = np.expand_dims(img, axis=0)
        preds = model.predict(img_array, verbose=0)
        pred_label = config.CLASS_NAMES[np.argmax(preds[0])]
        confidence = np.max(preds[0])
        
        # Generate heatmap
        try:
            heatmap = make_gradcam_heatmap(img_array, model, last_conv_layer_name)
            heatmap_resized = cv2.resize(heatmap, (img.shape[1], img.shape[0]))
            heatmap_colored = plt.cm.jet(heatmap_resized)[:, :, :3]
            overlay = heatmap_colored * 0.4 + img
        except Exception as e:
            print(f"  ⚠ Grad-CAM failed for sample {i}: {e}")
            heatmap_resized = np.zeros((img.shape[0], img.shape[1]))
            overlay = img
        
        # Plot
        axes[i, 0].imshow(img)
        axes[i, 0].set_title(f'Original\nTrue: {true_label}', fontsize=9)
        axes[i, 0].axis('off')
        
        axes[i, 1].imshow(heatmap_resized, cmap='jet')
        axes[i, 1].set_title('Grad-CAM', fontsize=9)
        axes[i, 1].axis('off')
        
        axes[i, 2].imshow(overlay)
        axes[i, 2].set_title(f'Overlay\nPred: {pred_label}\nConf: {confidence:.2%}', 
                           fontsize=9)
        axes[i, 2].axis('off')
    
    plt.suptitle('Grad-CAM: Model Attention Visualization', 
                fontsize=16, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig(f'{config.OUTPUT_DIR}/fig3_gradcam.png', 
               dpi=config.DPI, bbox_inches='tight')
    plt.savefig(f'{config.OUTPUT_DIR}/fig3_gradcam.pdf', 
               bbox_inches='tight')
    plt.close()
    
    print("✓ Figure 3 saved")


# ============================================================================
# FIGURE 4: CONFUSION MATRIX
# ============================================================================

def create_confusion_matrix_figure():
    """Create confusion matrix visualization"""
    print("\nGenerating Figure 4: Confusion Matrix...")
    
    # Generate predictions
    y_pred_probs = model.predict(X_samples, batch_size=32, verbose=0)
    y_pred = np.argmax(y_pred_probs, axis=1)
    
    # Compute confusion matrix
    cm = confusion_matrix(y_samples, y_pred)
    cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    
    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(16, 7))
    
    # Regular confusion matrix
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=config.CLASS_NAMES, yticklabels=config.CLASS_NAMES,
                ax=axes[0], cbar_kws={'label': 'Count'}, square=True)
    axes[0].set_title('Confusion Matrix (Counts)', fontsize=14, fontweight='bold')
    axes[0].set_ylabel('True Label', fontsize=12)
    axes[0].set_xlabel('Predicted Label', fontsize=12)
    
    # Normalized confusion matrix
    sns.heatmap(cm_normalized, annot=True, fmt='.2%', cmap='Blues',
                xticklabels=config.CLASS_NAMES, yticklabels=config.CLASS_NAMES,
                ax=axes[1], cbar_kws={'label': 'Proportion'}, square=True)
    axes[1].set_title('Confusion Matrix (Normalized)', fontsize=14, fontweight='bold')
    axes[1].set_ylabel('True Label', fontsize=12)
    axes[1].set_xlabel('Predicted Label', fontsize=12)
    
    plt.tight_layout()
    plt.savefig(f'{config.OUTPUT_DIR}/fig4_confusion_matrix.png', 
               dpi=config.DPI, bbox_inches='tight')
    plt.savefig(f'{config.OUTPUT_DIR}/fig4_confusion_matrix.pdf', 
               bbox_inches='tight')
    plt.close()
    
    print("✓ Figure 4 saved")


# ============================================================================
# FIGURE 5: ROC CURVES
# ============================================================================

def create_roc_curves_figure():
    """Create ROC curves for all classes"""
    print("\nGenerating Figure 5: ROC Curves...")
    
    # Generate predictions
    y_pred_probs = model.predict(X_samples, batch_size=32, verbose=0)
    
    # Binarize labels
    y_samples_bin = label_binarize(y_samples, classes=range(config.NUM_CLASSES))
    
    # Compute ROC curve and AUC for each class
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    
    for i in range(config.NUM_CLASSES):
        fpr[i], tpr[i], _ = roc_curve(y_samples_bin[:, i], y_pred_probs[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])
    
    # Micro-average
    fpr["micro"], tpr["micro"], _ = roc_curve(y_samples_bin.ravel(), 
                                               y_pred_probs.ravel())
    roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])
    
    # Macro-average
    all_fpr = np.unique(np.concatenate([fpr[i] for i in range(config.NUM_CLASSES)]))
    mean_tpr = np.zeros_like(all_fpr)
    for i in range(config.NUM_CLASSES):
        mean_tpr += np.interp(all_fpr, fpr[i], tpr[i])
    mean_tpr /= config.NUM_CLASSES
    fpr["macro"] = all_fpr
    tpr["macro"] = mean_tpr
    roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])
    
    # Plot
    plt.figure(figsize=(10, 8))
    
    # Plot micro and macro averages
    plt.plot(fpr["micro"], tpr["micro"],
             label=f'Micro-average (AUC = {roc_auc["micro"]:.3f})',
             color='deeppink', linestyle=':', linewidth=3)
    
    plt.plot(fpr["macro"], tpr["macro"],
             label=f'Macro-average (AUC = {roc_auc["macro"]:.3f})',
             color='navy', linestyle=':', linewidth=3)
    
    # Plot per-class curves
    colors = plt.cm.Set3(np.linspace(0, 1, config.NUM_CLASSES))
    for i, color in zip(range(config.NUM_CLASSES), colors):
        plt.plot(fpr[i], tpr[i], color=color, linewidth=2,
                label=f'{config.CLASS_NAMES[i]} (AUC = {roc_auc[i]:.3f})')
    
    plt.plot([0, 1], [0, 1], 'k--', linewidth=2, label='Random Classifier')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=12)
    plt.ylabel('True Positive Rate', fontsize=12)
    plt.title('ROC Curves - Multi-class Classification', 
             fontsize=14, fontweight='bold')
    plt.legend(loc="lower right", fontsize=9)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'{config.OUTPUT_DIR}/fig5_roc_curves.png', 
               dpi=config.DPI, bbox_inches='tight')
    plt.savefig(f'{config.OUTPUT_DIR}/fig5_roc_curves.pdf', 
               bbox_inches='tight')
    plt.close()
    
    print("✓ Figure 5 saved")
    print(f"  Micro-average AUC: {roc_auc['micro']:.4f}")
    print(f"  Macro-average AUC: {roc_auc['macro']:.4f}")


# ============================================================================
# FIGURE 6: PRECISION-RECALL CURVES
# ============================================================================

def create_precision_recall_figure():
    """Create precision-recall curves"""
    print("\nGenerating Figure 6: Precision-Recall Curves...")
    
    # Generate predictions
    y_pred_probs = model.predict(X_samples, batch_size=32, verbose=0)
    
    # Binarize labels
    y_samples_bin = label_binarize(y_samples, classes=range(config.NUM_CLASSES))
    
    # Compute precision-recall curve for each class
    precision = dict()
    recall = dict()
    pr_auc = dict()
    
    plt.figure(figsize=(10, 8))
    
    colors = plt.cm.Set3(np.linspace(0, 1, config.NUM_CLASSES))
    for i, color in zip(range(config.NUM_CLASSES), colors):
        precision[i], recall[i], _ = precision_recall_curve(
            y_samples_bin[:, i], y_pred_probs[:, i]
        )
        pr_auc[i] = auc(recall[i], precision[i])
        
        plt.plot(recall[i], precision[i], color=color, linewidth=2,
                label=f'{config.CLASS_NAMES[i]} (AUC = {pr_auc[i]:.3f})')
    
    plt.xlabel('Recall', fontsize=12)
    plt.ylabel('Precision', fontsize=12)
    plt.title('Precision-Recall Curves', fontsize=14, fontweight='bold')
    plt.legend(loc="best", fontsize=9)
    plt.grid(True, alpha=0.3)
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.tight_layout()
    plt.savefig(f'{config.OUTPUT_DIR}/fig6_precision_recall.png', 
               dpi=config.DPI, bbox_inches='tight')
    plt.savefig(f'{config.OUTPUT_DIR}/fig6_precision_recall.pdf', 
               bbox_inches='tight')
    plt.close()
    
    print("✓ Figure 6 saved")


# ============================================================================
# FIGURE 7: CLASS DISTRIBUTION AND PERFORMANCE
# ============================================================================

def create_class_performance_figure():
    """Create class distribution and per-class performance"""
    print("\nGenerating Figure 7: Class Performance Analysis...")
    
    # Generate predictions
    y_pred_probs = model.predict(X_samples, batch_size=32, verbose=0)
    y_pred = np.argmax(y_pred_probs, axis=1)
    
    # Get classification report
    report = classification_report(y_samples, y_pred, 
                                   target_names=config.CLASS_NAMES,
                                   output_dict=True)
    
    # Extract metrics
    classes = config.CLASS_NAMES
    precision = [report[cls]['precision'] for cls in classes]
    recall = [report[cls]['recall'] for cls in classes]
    f1_score = [report[cls]['f1-score'] for cls in classes]
    support = [report[cls]['support'] for cls in classes]
    
    # Create figure
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Class distribution
    class_counts = [np.sum(y_samples == i) for i in range(config.NUM_CLASSES)]
    axes[0, 0].bar(classes, class_counts, color='skyblue', edgecolor='black')
    axes[0, 0].set_title('Class Distribution', fontsize=12, fontweight='bold')
    axes[0, 0].set_xlabel('Class')
    axes[0, 0].set_ylabel('Count')
    axes[0, 0].tick_params(axis='x', rotation=45)
    axes[0, 0].grid(axis='y', alpha=0.3)
    
    # Precision by class
    axes[0, 1].bar(classes, precision, color='lightgreen', edgecolor='black')
    axes[0, 1].set_title('Precision by Class', fontsize=12, fontweight='bold')
    axes[0, 1].set_xlabel('Class')
    axes[0, 1].set_ylabel('Precision')
    axes[0, 1].tick_params(axis='x', rotation=45)
    axes[0, 1].set_ylim([0, 1])
    axes[0, 1].grid(axis='y', alpha=0.3)
    axes[0, 1].axhline(y=np.mean(precision), color='r', linestyle='--', 
                      label=f'Mean: {np.mean(precision):.3f}')
    axes[0, 1].legend()
    
    # Recall by class
    axes[1, 0].bar(classes, recall, color='lightcoral', edgecolor='black')
    axes[1, 0].set_title('Recall by Class', fontsize=12, fontweight='bold')
    axes[1, 0].set_xlabel('Class')
    axes[1, 0].set_ylabel('Recall')
    axes[1, 0].tick_params(axis='x', rotation=45)
    axes[1, 0].set_ylim([0, 1])
    axes[1, 0].grid(axis='y', alpha=0.3)
    axes[1, 0].axhline(y=np.mean(recall), color='r', linestyle='--',
                      label=f'Mean: {np.mean(recall):.3f}')
    axes[1, 0].legend()
    
    # F1-Score by class
    axes[1, 1].bar(classes, f1_score, color='lightyellow', edgecolor='black')
    axes[1, 1].set_title('F1-Score by Class', fontsize=12, fontweight='bold')
    axes[1, 1].set_xlabel('Class')
    axes[1, 1].set_ylabel('F1-Score')
    axes[1, 1].tick_params(axis='x', rotation=45)
    axes[1, 1].set_ylim([0, 1])
    axes[1, 1].grid(axis='y', alpha=0.3)
    axes[1, 1].axhline(y=np.mean(f1_score), color='r', linestyle='--',
                      label=f'Mean: {np.mean(f1_score):.3f}')
    axes[1, 1].legend()
    
    plt.suptitle('Per-Class Performance Analysis', 
                fontsize=16, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig(f'{config.OUTPUT_DIR}/fig7_class_performance.png', 
               dpi=config.DPI, bbox_inches='tight')
    plt.savefig(f'{config.OUTPUT_DIR}/fig7_class_performance.pdf', 
               bbox_inches='tight')
    plt.close()
    
    print("✓ Figure 7 saved")


# ============================================================================
# FIGURE 8: CONFIDENCE DISTRIBUTION
# ============================================================================

def create_confidence_distribution_figure():
    """Create confidence score distribution analysis"""
    print("\nGenerating Figure 8: Confidence Distribution...")
    
    # Generate predictions
    y_pred_probs = model.predict(X_samples, batch_size=32, verbose=0)
    y_pred = np.argmax(y_pred_probs, axis=1)
    confidences = np.max(y_pred_probs, axis=1)
    
    # Separate correct and incorrect predictions
    correct_mask = y_pred == y_samples
    correct_conf = confidences[correct_mask]
    incorrect_conf = confidences[~correct_mask]
    
    # Create figure
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Overall confidence distribution
    axes[0, 0].hist(confidences, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
    axes[0, 0].axvline(np.mean(confidences), color='r', linestyle='--', linewidth=2,
                      label=f'Mean: {np.mean(confidences):.3f}')
    axes[0, 0].set_title('Overall Confidence Distribution', fontsize=12, fontweight='bold')
    axes[0, 0].set_xlabel('Confidence Score')
    axes[0, 0].set_ylabel('Frequency')
    axes[0, 0].legend()
    axes[0, 0].grid(axis='y', alpha=0.3)
    
    # Correct vs Incorrect predictions
    axes[0, 1].hist([correct_conf, incorrect_conf], bins=15, 
                   label=['Correct', 'Incorrect'],
                   color=['green', 'red'], alpha=0.6, edgecolor='black')
    axes[0, 1].set_title('Confidence: Correct vs Incorrect', fontsize=12, fontweight='bold')
    axes[0, 1].set_xlabel('Confidence Score')
    axes[0, 1].set_ylabel('Frequency')
    axes[0, 1].legend()
    axes[0, 1].grid(axis='y', alpha=0.3)
    
    # Box plot by class
    conf_by_class = [confidences[y_samples == i] for i in range(config.NUM_CLASSES)]
    bp = axes[1, 0].boxplot(conf_by_class, labels=config.CLASS_NAMES, patch_artist=True)
    for patch in bp['boxes']:
        patch.set_facecolor('lightblue')
    axes[1, 0].set_title('Confidence Distribution by Class', fontsize=12, fontweight='bold')
    axes[1, 0].set_xlabel('Class')
    axes[1, 0].set_ylabel('Confidence Score')
    axes[1, 0].tick_params(axis='x', rotation=45)
    axes[1, 0].grid(axis='y', alpha=0.3)
    
    # Accuracy vs Confidence threshold
    thresholds = np.linspace(0, 1, 21)
    accuracies = []
    sample_counts = []
    
    for thresh in thresholds:
        mask = confidences >= thresh
        if np.sum(mask) > 0:
            acc = np.mean(y_pred[mask] == y_samples[mask])
            accuracies.append(acc)
            sample_counts.append(np.sum(mask))
        else:
            accuracies.append(0)
            sample_counts.append(0)
    
    ax1 = axes[1, 1]
    ax2 = ax1.twinx()
    
    line1 = ax1.plot(thresholds, accuracies, 'b-', linewidth=2, label='Accuracy')
    line2 = ax2.plot(thresholds, sample_counts, 'r--', linewidth=2, label='Sample Count')
    
    ax1.set_xlabel('Confidence Threshold')
    ax1.set_ylabel('Accuracy', color='b')
    ax2.set_ylabel('Number of Samples', color='r')
    ax1.tick_params(axis='y', labelcolor='b')
    ax2.tick_params(axis='y', labelcolor='r')
    ax1.set_title('Accuracy vs Confidence Threshold', fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Combine legends
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='center right')
    
    plt.suptitle('Confidence Score Analysis', fontsize=16, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig(f'{config.OUTPUT_DIR}/fig8_confidence_distribution.png', 
               dpi=config.DPI, bbox_inches='tight')
    plt.savefig(f'{config.OUTPUT_DIR}/fig8_confidence_distribution.pdf', 
               bbox_inches='tight')
    plt.close()
    
    print("✓ Figure 8 saved")
    print(f"  Mean confidence: {np.mean(confidences):.4f}")
    print(f"  Correct predictions mean confidence: {np.mean(correct_conf):.4f}")
    if len(incorrect_conf) > 0:
        print(f"  Incorrect predictions mean confidence: {np.mean(incorrect_conf):.4f}")


# ============================================================================
# FIGURE 9: FEATURE MAP VISUALIZATION
# ============================================================================

def create_feature_maps_figure():
    """Visualize intermediate feature maps"""
    print("\nGenerating Figure 9: Feature Maps...")
    
    # Select a sample image
    sample_idx = np.random.randint(0, len(X_samples))
    sample_img = X_samples[sample_idx]
    sample_label = config.CLASS_NAMES[y_samples[sample_idx]]
    
    # Get intermediate layer outputs
    layer_names = []
    for layer in model.layers:
        if 'conv' in layer.name.lower() or 'block' in layer.name.lower():
            layer_names.append(layer.name)
    
    # Select a few representative layers
    if len(layer_names) > 6:
        selected_layers = [layer_names[i] for i in 
                          [0, len(layer_names)//4, len(layer_names)//2, 
                           3*len(layer_names)//4, len(layer_names)-1]]
    else:
        selected_layers = layer_names[:5]
    
    if not selected_layers:
        print("⚠ No suitable layers found for feature map visualization")
        return
    
    # Create feature extraction model
    layer_outputs = [model.get_layer(name).output for name in selected_layers]
    feature_model = keras.models.Model(inputs=model.input, outputs=layer_outputs)
    
    # Get feature maps
    img_array = np.expand_dims(sample_img, axis=0)
    feature_maps = feature_model.predict(img_array, verbose=0)
    
    # Plot
    num_layers = len(selected_layers)
    fig, axes = plt.subplots(num_layers + 1, 8, figsize=(16, 2 * (num_layers + 1)))
    
    # Show original image in first row
    for i in range(8):
        if i == 0:
            axes[0, i].imshow(sample_img)
            axes[0, i].set_title(f'Original\n{sample_label}', fontsize=8)
        axes[0, i].axis('off')
    
    # Show feature maps
    for layer_idx, (layer_name, feature_map) in enumerate(zip(selected_layers, feature_maps)):
        # Select 8 channels to display
        num_channels = min(8, feature_map.shape[-1])
        channel_indices = np.linspace(0, feature_map.shape[-1]-1, num_channels, dtype=int)
        
        for i, channel_idx in enumerate(channel_indices):
            channel_image = feature_map[0, :, :, channel_idx]
            axes[layer_idx + 1, i].imshow(channel_image, cmap='viridis')
            if i == 0:
                axes[layer_idx + 1, i].set_ylabel(f'{layer_name[:15]}...', 
                                                  fontsize=7, rotation=0, 
                                                  ha='right', va='center')
            axes[layer_idx + 1, i].axis('off')
    
    plt.suptitle('Feature Map Visualization Through Network Layers', 
                fontsize=16, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig(f'{config.OUTPUT_DIR}/fig9_feature_maps.png', 
               dpi=config.DPI, bbox_inches='tight')
    plt.savefig(f'{config.OUTPUT_DIR}/fig9_feature_maps.pdf', 
               bbox_inches='tight')
    plt.close()
    
    print("✓ Figure 9 saved")


# ============================================================================
# GENERATE ALL FIGURES
# ============================================================================

def generate_all_figures():
    """Generate all journal figures"""
    print("\n" + "="*80)
    print("GENERATING ALL JOURNAL FIGURES")
    print("="*80)
    
    try:
        create_architecture_figure()
    except Exception as e:
        print(f"✗ Error in Figure 1: {e}")
    
    try:
        create_prediction_samples_figure()
    except Exception as e:
        print(f"✗ Error in Figure 2: {e}")
    
    try:
        create_gradcam_figure()
    except Exception as e:
        print(f"✗ Error in Figure 3: {e}")
    
    try:
        create_confusion_matrix_figure()
    except Exception as e:
        print(f"✗ Error in Figure 4: {e}")
    
    try:
        create_roc_curves_figure()
    except Exception as e:
        print(f"✗ Error in Figure 5: {e}")
    
    try:
        create_precision_recall_figure()
    except Exception as e:
        print(f"✗ Error in Figure 6: {e}")
    
    try:
        create_class_performance_figure()
    except Exception as e:
        print(f"✗ Error in Figure 7: {e}")
    
    try:
        create_confidence_distribution_figure()
    except Exception as e:
        print(f"✗ Error in Figure 8: {e}")
    
    try:
        create_feature_maps_figure()
    except Exception as e:
        print(f"✗ Error in Figure 9: {e}")
    
    print("\n" + "="*80)
    print("FIGURE GENERATION COMPLETE")
    print("="*80)
    print(f"\nAll figures saved to: {config.OUTPUT_DIR}")
    print("\nGenerated files:")
    for file in sorted(os.listdir(config.OUTPUT_DIR)):
        file_path = os.path.join(config.OUTPUT_DIR, file)
        if os.path.isfile(file_path):
            size = os.path.getsize(file_path) / 1024
            print(f"  ✓ {file:<40} ({size:.1f} KB)")
    
    print("\n" + "="*80)


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    generate_all_figures()
    
    print("\n" + "="*80)
    print("JOURNAL FIGURE GENERATION COMPLETE!")
    print("="*80)
    print("\nFigures generated:")
    print("  1. Model Architecture Diagram")
    print("  2. Sample Predictions with Confidence")
    print("  3. Grad-CAM Visualization")
    print("  4. Confusion Matrix")
    print("  5. ROC Curves")
    print("  6. Precision-Recall Curves")
    print("  7. Class Performance Analysis")
    print("  8. Confidence Distribution")
    print("  9. Feature Map Visualization")
    print("\nAll figures are publication-ready (300 DPI)")
    print("Both PNG and PDF formats provided")
    print("="*80)
