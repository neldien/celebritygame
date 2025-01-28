# Celebrity Game

A real-time multiplayer celebrity guessing game built with Flask and Socket.IO.

## Features
- Real-time multiplayer gameplay
- Room-based game sessions
- Interactive celebrity name guessing
- Live score tracking

## Tech Stack
- Flask
- Flask-SocketIO
- Python 3.11
- WebSocket for real-time communication
- Gunicorn with Eventlet for production deployment

## Setup

1. Clone the repository
```bash
git clone https://github.com/neldien/celebritygame.git
cd celebrity
```

2. Create a virtual environment
```bash
python -m venv venv
```

3. Activate the virtual environment
- Windows: `venv\Scripts\activate`
- Unix/MacOS: `source venv/bin/activate`

4. Install dependencies
```bash
pip install -r requirements.txt
```

5. Run the application
```bash
python app.py
```

## How to Play

1. Create a room
2. Share the room code with other players
3. Submit celebrity names
4. Start the game when everyone has joined

## Deployment

This application is deployed on Render.com. Visit [insert-your-app-url-here] to play!

## Development

To run the application in development mode:
```bash
flask run
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
