from flask import Flask, render_template, request
from models.astar import a_star_search

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
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    return render_template('index.html', map=map)

@app.route('/send-map', methods=['POST'])
def receive_map():
    
    map_data = request.json['map']
    map_search = a_star_search(map_data)
    return render_template('search.html', map=map_search)

if __name__ == '__main__':
    app.run()