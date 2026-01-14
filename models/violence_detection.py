import cv2
import numpy as np
from tensorflow.keras.models import load_model
import os

class ViolenceDetector:
    """Violence detection using deep learning model"""
    
    def __init__(self, model_path='data/models/violence_detection_model.h5'):
        """
        Initialize violence detector
        
        Args:
            model_path: Path to trained model file
        """
        self.model_path = model_path
        self.model = None
        self.img_size = (224, 224)
        self.sequence_length = 16
        self.frame_buffer = []
        
        if os.path.exists(model_path):
            self.load_model()
    
    def load_model(self):
        """Load the trained violence detection model"""
        try:
            self.model = load_model(self.model_path)
            print(f"Model loaded successfully from {self.model_path}")
        except Exception as e:
            print(f"Error loading model: {e}")
    
    def preprocess_frame(self, frame):
        """
        Preprocess frame for model input
        
        Args:
            frame: Input frame (BGR image)
        
        Returns:
            Preprocessed frame
        """
        # Resize frame
        resized = cv2.resize(frame, self.img_size)
        # Normalize pixel values
        normalized = resized / 255.0
        return normalized
    
    def predict(self, frame):
        """
        Predict violence in a single frame or sequence
        
        Args:
            frame: Input frame
        
        Returns:
            Dictionary with prediction results
        """
        if self.model is None:
            return {'violence_detected': False, 'confidence': 0.0, 'error': 'Model not loaded'}
        
        # Preprocess frame
        processed_frame = self.preprocess_frame(frame)
        self.frame_buffer.append(processed_frame)
        
        # Keep only recent frames
        if len(self.frame_buffer) > self.sequence_length:
            self.frame_buffer.pop(0)
        
        # Need enough frames for prediction
        if len(self.frame_buffer) < self.sequence_length:
            return {'violence_detected': False, 'confidence': 0.0, 'status': 'buffering'}
        
        # Prepare input
        input_data = np.array([self.frame_buffer])
        
        # Make prediction
        prediction = self.model.predict(input_data, verbose=0)[0][0]
        
        return {
            'violence_detected': prediction > 0.5,
            'confidence': float(prediction),
            'status': 'success'
        }
    
    def reset_buffer(self):
        """Reset frame buffer"""
        self.frame_buffer = []
