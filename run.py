"""Main application entry point"""

from app import create_app
import os

# Create Flask application
app = create_app()

if __name__ == '__main__':
    # Get configuration from environment
    debug_mode = os.environ.get('FLASK_DEBUG', 'True') == 'True'
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_PORT', 5000))
    
    print(f"Starting Violence Detection System...")
    print(f"Access the application at: http://localhost:{port}")
    
    # Run the application
    app.run(
        host=host,
        port=port,
        debug=debug_mode,
        threaded=True
    )
