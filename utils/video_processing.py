import cv2
import os
from datetime import datetime

def save_video_clip(frames, output_path, fps=30):
    """
    Save frames as video clip
    
    Args:
        frames: List of frames
        output_path: Output video file path
        fps: Frames per second
    """
    if not frames:
        return
    
    height, width = frames[0].shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    for frame in frames:
        out.write(frame)
    
    out.release()

def save_frame(frame, output_dir='data/frames', prefix='frame'):
    """
    Save single frame as image
    
    Args:
        frame: Frame to save
        output_dir: Output directory
        prefix: Filename prefix
    
    Returns:
        Path to saved frame
    """
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
    filename = f"{prefix}_{timestamp}.jpg"
    filepath = os.path.join(output_dir, filename)
    cv2.imwrite(filepath, frame)
    return filepath

def extract_frames(video_path, frame_skip=1):
    """
    Extract frames from video file
    
    Args:
        video_path: Path to video file
        frame_skip: Number of frames to skip between extractions
    
    Returns:
        List of frames
    """
    cap = cv2.VideoCapture(video_path)
    frames = []
    frame_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        if frame_count % frame_skip == 0:
            frames.append(frame)
        
        frame_count += 1
    
    cap.release()
    return frames

def get_video_info(video_path):
    """
    Get video file information
    
    Args:
        video_path: Path to video file
    
    Returns:
        Dictionary with video information
    """
    cap = cv2.VideoCapture(video_path)
    
    info = {
        'width': int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        'height': int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        'fps': cap.get(cv2.CAP_PROP_FPS),
        'frame_count': int(cap.get(cv2.CAP_PROP_FRAME_COUNT)),
        'duration': int(cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS))
    }
    
    cap.release()
    return info

def encode_frame_to_jpeg(frame, quality=90):
    """
    Encode frame to JPEG bytes
    
    Args:
        frame: Input frame
        quality: JPEG quality (0-100)
    
    Returns:
        JPEG encoded bytes
    """
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    _, buffer = cv2.imencode('.jpg', frame, encode_param)
    return buffer.tobytes()
