from app import app
from app import socketio
import os

host = os.environ.get('IP', '0.0.0.0')
port = int(os.environ.get('PORT', 5000))
socketio.run(app, host=host, port=port, debug=True)
#app.run(host=host, port=port, debug=True)