workers = 1  # Only one worker for WebSocket support
worker_class = 'eventlet'
bind = "0.0.0.0:$PORT"  # Render will provide the PORT environment variable