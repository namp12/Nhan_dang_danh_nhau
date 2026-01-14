import cv2
from .camera import Camera

class RTSPCamera(Camera):
    """RTSP camera stream implementation"""
    
    def __init__(self, rtsp_url, username=None, password=None):
        """
        Initialize RTSP camera
        
        Args:
            rtsp_url: RTSP stream URL
            username: Optional authentication username
            password: Optional authentication password
        """
        if username and password:
            # Insert credentials into RTSP URL
            rtsp_url = rtsp_url.replace('rtsp://', f'rtsp://{username}:{password}@')
        
        super().__init__(rtsp_url)
        self.username = username
        self.password = password
    
    def connect(self):
        """Connect to RTSP stream"""
        self.cap = cv2.VideoCapture(self.source)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # Reduce buffer to minimize lag
        return self.is_opened()
    
    def reconnect(self):
        """Reconnect to RTSP stream if connection is lost"""
        self.stop()
        time.sleep(1)
        return self.connect()
