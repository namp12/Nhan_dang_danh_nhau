import os
from datetime import timedelta

class Config:
    """Application configuration"""
    
    # Flask configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///violence_detection.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Upload configuration
    UPLOAD_FOLDER = 'data/uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # Detection configuration
    VIOLENCE_DETECTION_MODEL = 'data/models/violence_detection_model.h5'
    CONFIDENCE_THRESHOLD = 0.5
    FRAME_SKIP = 5  # Process every 5th frame
    
    # Video recording
    SAVE_DETECTION_VIDEOS = True
    VIDEO_RETENTION_DAYS = 30
    
    # Camera configuration
    DEFAULT_RTSP_PORT = 554
    CAMERA_RECONNECT_DELAY = 5  # seconds
    
    # Alert configuration
    ALERT_COOLDOWN = timedelta(minutes=5)  # Minimum time between alerts
    
    # Session configuration
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    # Override with production settings
    
class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
