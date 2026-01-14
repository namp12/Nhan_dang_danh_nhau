from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, SubmitField
from wtforms.validators import DataRequired, URL, NumberRange

class CameraForm(FlaskForm):
    """Form for adding/editing camera configurations"""
    name = StringField('Camera Name', validators=[DataRequired()])
    rtsp_url = StringField('RTSP URL', validators=[DataRequired(), URL()])
    location = StringField('Location')
    is_active = BooleanField('Active', default=True)
    submit = SubmitField('Save Camera')

class DetectionConfigForm(FlaskForm):
    """Form for configuring detection parameters"""
    confidence_threshold = FloatField(
        'Confidence Threshold', 
        validators=[DataRequired(), NumberRange(min=0.0, max=1.0)],
        default=0.5
    )
    frame_skip = FloatField(
        'Frame Skip',
        validators=[DataRequired(), NumberRange(min=1, max=30)],
        default=5
    )
    save_frames = BooleanField('Save Detection Frames', default=True)
    submit = SubmitField('Update Configuration')
