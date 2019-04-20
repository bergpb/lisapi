from app import app
from app.helpers import helpers
from flask_socketio import SocketIO, emit


socketio = SocketIO(app)


@socketio.on('updateStatus', namespace='/sockets')
def on_update(data):
    """Update content in page"""
    data = helpers.statusInfo()
    emit('statusUpdated', data.json)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
