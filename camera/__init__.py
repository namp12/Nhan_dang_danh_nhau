"""Camera module for handling various camera sources"""

from .camera import Camera
from .rtsp import RTSPCamera
from .onvif import ONVIFCamera

__all__ = ['Camera', 'RTSPCamera', 'ONVIFCamera']
