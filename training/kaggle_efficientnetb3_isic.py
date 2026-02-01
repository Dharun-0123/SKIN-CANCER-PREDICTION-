"""
KAGGLE NOTEBOOK: EfficientNetB3 for ISIC 2019 Skin Lesion Classification
==========================================================================
This notebook is designed to run end-to-end in Kaggle without manual edits.

SETUP INSTRUCTIONS:
1. Add ISIC 2019 dataset to your Kaggle notebook
2. Run all cells in order
3. Download the trained model from the output

Dataset: https://www.kaggle.com/datasets/salviohexia/isic-2019-skin-lesion-images-for-classification
"""

# ============================================================================
# CELL 1: Check Environment and Install Dependencies
# ============================================================================

import sys
import os

print("="*80)
print("KAGGLE ENVIRONMENT CHECK")
print("="*80)

# Check if running in Kaggle
IN_KAGGLE = os.path.exists('/kaggle/input')
print(f"Running in Kaggle: {IN_KAGGLE}")

if IN_KAGGLE:
    print("✓ Kaggle environment detected")
    # Kaggle paths
    KAGGLE_INPUT = '/kaggle/input'
    KAGGLE_WORKING = '/kaggle/working'
    print(f"Input directory: {KAGGLE_INPUT}")
    print(f"Working directory: {KAGGLE_WORKING}")
else:
    print("⚠ Not running in Kaggle - using local paths")
    KAGGLE_INPUT = './data'
    KAGGLE_WORKING = './output'

# Install any missing packages (most are pre-installed in Kaggle)
print("\nChecking dependencies...")
try:
    import tensorflow as tf
    print(f"✓ TensorFlow {tf.__version__}")
except ImportError:
    print("Installing TensorFlow...")
    !pip install -q tensorflow

try:
    import cv2
    print(f"✓ OpenCV installed")
except ImportError:
    print("Installing OpenCV...")
    !pip install -q opencv-python-headless

print("\n" + "="*80)


# ============================================================================
# CELL 2: Import Libraries
# ============================================================================

import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import cv2
import json
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

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

print("="*80)
print("LIBRARY VERSIONS")
print("="*80)
print(f"Python: {sys.version.split()[0]}")
print(f"TensorFlow: {tf.__version__}")
print(f"Keras: {keras.__version__}")
print(f"NumPy: {np.__version__}")
print(f"Pandas: {pd.__version__}")
print(f"OpenCV: {cv2.__version__}")
print("="*80)

# ============================================================================
# CELL 3: Hardware Detection and Setup
# ============================================================================

print("\n" + "="*80)
print("HARDWARE DETECTION")
print("="*80)

# Check GPU availability
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print(f"✓ GPU Available: {len(gpus)} GPU(s) detected")
    for i, gpu in enumerate(gpus):
        print(f"  GPU {i}: {gpu}")
    # Enable memory growth to avoid OOM errors
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        print("✓ GPU memory growth enabled")
    except RuntimeError as e:
        print(f"⚠ Could not enable memory growth: {e}")
else:
    print("⚠ No GPU detected - training will use CPU (slower)")

# Check TPU availability (Kaggle sometimes has TPUs)
try:
    tpu = tf.distribute.cluster_resolver.TPUClusterResolver()
    print(f"✓ TPU detected: {tpu.cluster_spec().as_dict()['worker']}")
    tf.config.experimental_connect_to_cluster(tpu)
    tf.tpu.experimental.initialize_tpu_system(tpu)
    strategy = tf.distribute.TPUStrategy(tpu)
    print("✓ Using TPU strategy")
except ValueError:
    if gpus:
        strategy = tf.distribute.MirroredStrategy()
        print("✓ Using GPU strategy")
    else:
        strategy = tf.distribute.get_strategy()
        print("✓ Using default strategy (CPU)")

print(f"Number of devices: {strategy.num_replicas_in_sync}")
print("="*80)

# ============================================================================
# CELL 4: Set Seeds for Reproducibility
# ============================================================================

def set_seeds(seed=42):
    """Set all random seeds for reproducibility"""
    os.environ['PYTHONHASHSEED'] = str(seed)
    os.environ['TF_DETERMINISTIC_OPS'] = '1'
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)
    print(f"✓ All seeds set to {seed} for reproducibility")

set_seeds(42)

