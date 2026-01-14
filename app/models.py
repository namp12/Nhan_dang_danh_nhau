from app import db
from datetime import datetime

class DetectionRecord(db.Model):
    """Model for storing violence detection records"""
    __tablename__ = 'detection_records'
    
    id = db.Column(db.Integer, primary_key=True)
    camera_id = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    violence_detected = db.Column(db.Boolean, default=False)
    confidence = db.Column(db.Float, default=0.0)
    frame_path = db.Column(db.String(255))
    video_path = db.Column(db.String(255))
    
    def __repr__(self):
        return f'<DetectionRecord {self.id} - {self.camera_id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'camera_id': self.camera_id,
            'timestamp': self.timestamp.isoformat(),
            'violence_detected': self.violence_detected,
            'confidence': self.confidence,
            'frame_path': self.frame_path,
            'video_path': self.video_path
        }

class Camera(db.Model):
    """Model for managing camera configurations"""
    __tablename__ = 'cameras'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    rtsp_url = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(200))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Camera {self.name}>'
