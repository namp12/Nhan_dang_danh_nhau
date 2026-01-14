import cv2
import numpy as np
from PIL import Image

def resize_image(image, width=None, height=None, inter=cv2.INTER_AREA):
    """
    Resize image while maintaining aspect ratio
    
    Args:
        image: Input image
        width: Target width
        height: Target height
        inter: Interpolation method
    
    Returns:
        Resized image
    """
    dim = None
    (h, w) = image.shape[:2]
    
    if width is None and height is None:
        return image
    
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    
    resized = cv2.resize(image, dim, interpolation=inter)
    return resized

def enhance_image(image, brightness=1.0, contrast=1.0):
    """
    Enhance image brightness and contrast
    
    Args:
        image: Input image
        brightness: Brightness factor
        contrast: Contrast factor
    
    Returns:
        Enhanced image
    """
    enhanced = cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)
    return enhanced

def apply_blur(image, kernel_size=5):
    """
    Apply Gaussian blur to image
    
    Args:
        image: Input image
        kernel_size: Size of blur kernel
    
    Returns:
        Blurred image
    """
    blurred = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    return blurred

def convert_to_grayscale(image):
    """Convert image to grayscale"""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def detect_edges(image, low_threshold=50, high_threshold=150):
    """
    Detect edges using Canny edge detection
    
    Args:
        image: Input image
        low_threshold: Low threshold for Canny
        high_threshold: High threshold for Canny
    
    Returns:
        Edge map
    """
    gray = convert_to_grayscale(image) if len(image.shape) == 3 else image
    edges = cv2.Canny(gray, low_threshold, high_threshold)
    return edges

def add_text_overlay(image, text, position=(10, 30), font_scale=1, color=(0, 255, 0), thickness=2):
    """
    Add text overlay to image
    
    Args:
        image: Input image
        text: Text to add
        position: Text position (x, y)
        font_scale: Font size scale
        color: Text color (BGR)
        thickness: Text thickness
    
    Returns:
        Image with text overlay
    """
    cv2.putText(image, text, position, cv2.FONT_HERSHEY_SIMPLEX, 
                font_scale, color, thickness)
    return image
