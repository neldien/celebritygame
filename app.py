import eventlet # type: ignore
eventlet.monkey_patch()

from flask import Flask, render_template, request, jsonify, session # type: ignore
from flask_socketio import SocketIO, emit, join_room # type: ignore
import random
import string
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key')
socketio = SocketIO(app, cors_allowed_origins="*")

# Store game rooms and their data
rooms = {}

def generate_room_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-room')
def create_room():
    room_code = generate_room_code()
    rooms[room_code] = {
        'submissions': [],
        'players': set(),
        'started': False,
        'host_sid': None,
        'submitted_players': set()
    }
    session['is_host'] = True
    session['room_code'] = room_code
    return jsonify({'room_code': room_code})

@app.route('/join/<room_code>')
def join(room_code):
    if room_code not in rooms:
        return "Room not found", 404
    session['room_code'] = room_code
    if 'is_host' not in session:
        session['is_host'] = False
    return render_template('game.html', room_code=room_code, is_host=session.get('is_host', False))

@socketio.on('join')
def on_join(data):
    room = data['room']
    is_host = data.get('is_host', False)
    
    if room in rooms:
        join_room(room)
        rooms[room]['players'].add(request.sid)
        if is_host:
            rooms[room]['host_sid'] = request.sid
        
        emit('player_count', {
            'count': len(rooms[room]['players']),
            'is_host': request.sid == rooms[room]['host_sid']
        }, to=room)

@socketio.on('submit_celebrity')
def on_submit(data):
    room = data['room']
    celebrity = data['celebrity']
    if room in rooms and request.sid not in rooms[room]['submitted_players']:
        rooms[room]['submissions'].append(celebrity)
        rooms[room]['submitted_players'].add(request.sid)  # Mark this player as submitted
        emit('submission_count', {'count': len(rooms[room]['submissions'])}, to=room)
        # Send personal confirmation to the submitting player
        emit('submission_confirmed')

@socketio.on('start_game')
def on_start(data):
    room = data['room']
    if room in rooms:
        rooms[room]['started'] = True
        emit('game_started', {'celebrities': rooms[room]['submissions']}, to=room)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port)
