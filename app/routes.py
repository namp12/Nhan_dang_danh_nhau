from flask import render_template, request, jsonify, current_app
from app import db
from app.models import DetectionRecord
import cv2
import numpy as np

@current_app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')

@current_app.route('/camera')
def camera():
    """Camera monitoring page"""
    return render_template('camera.html')

@current_app.route('/history')
def history():
    """Detection history page"""
    records = DetectionRecord.query.order_by(DetectionRecord.timestamp.desc()).all()
    return render_template('history.html', records=records)

@current_app.route('/config')
def config():
    """Configuration page"""
    return render_template('config.html')

@current_app.route('/analysis')
def analysis():
    """Video analysis page"""
    return render_template('analysis.html')

@current_app.route('/api/detect', methods=['POST'])
def detect_violence():
    """API endpoint for violence detection"""
    # TODO: Implement violence detection logic
    return jsonify({'status': 'success', 'detected': False})

@current_app.route('/api/cameras', methods=['GET', 'POST'])
def manage_cameras():
    """API endpoint for camera management"""
    if request.method == 'GET':
        # TODO: Return list of cameras
        return jsonify({'cameras': []})
    else:
        # TODO: Add new camera
        return jsonify({'status': 'success'})
