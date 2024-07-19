from flask import Flask, render_template,url_for, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Define the initial map (0: path, 1: wall, 2: entrance, 3: exit)
    map = [
        [2, 0, 0, 1, 1, 0, 0, 0, 3, 0],
        [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 1, 0, 1, 1, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    return render_template('index.html', map=map)

@app.route('/send-map', methods=['POST'])
def receive_map():
    map_data = request.json['map']
    print(map_data)
    # Process the map data here, regenerate index as needed
    return jsonify({'status': 'success', 'message': 'Map data received'})

if __name__ == '__main__':
    app.run()