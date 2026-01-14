import cv2
import threading
import time
from abc import ABC, abstractmethod

class Camera(ABC):
    """Abstract base class for camera sources"""
    
    def __init__(self, source):
        self.source = source
        self.cap = None
        self.frame = None
        self.running = False
        self.lock = threading.Lock()
    
    @abstractmethod
    def connect(self):
        """Connect to camera source"""
        pass
    
    def start(self):
        """Start capturing frames in a separate thread"""
        if not self.running:
            self.running = True
            threading.Thread(target=self._capture_loop, daemon=True).start()
    
    def stop(self):
        """Stop capturing frames"""
        self.running = False
        if self.cap is not None:
            self.cap.release()
    
    def _capture_loop(self):
        """Internal method to continuously capture frames"""
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                with self.lock:
                    self.frame = frame
            time.sleep(0.01)
    
    def get_frame(self):
        """Get the latest frame"""
        with self.lock:
            return self.frame.copy() if self.frame is not None else None
    
    def is_opened(self):
        """Check if camera is connected"""
        return self.cap is not None and self.cap.isOpened()

class WebCamera(Camera):
    """Web camera (USB camera) implementation"""
    
    def connect(self):
        """Connect to web camera"""
        self.cap = cv2.VideoCapture(int(self.source))
        return self.is_opened()
