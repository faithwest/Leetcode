from flask import Flask, request, jsonify, abort

app = Flask(__name__)

tasks = {}
next_id = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global next_id
    data = request.get_json()
    title = data.get('title')
    completed = data.get('completed', False)
    
    if not title:
        abort(400, description="Title is required")
    
    task_id = next_id
    next_id += 1
    task = {'id': task_id, 'title': title, 'completed': completed}
    tasks[task_id] = task
    return jsonify(task), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(list(tasks.values())), 200

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = tasks.get(task_id)
    if task is None:
        abort(404)
    return jsonify(task), 200

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = tasks.get(task_id)
    if task is None:
        abort(404)
    
    data = request.get_json()
    title = data.get('title', task['title'])
    completed = data.get('completed', task['completed'])
    
    task['title'] = title
    task['completed'] = completed
    return jsonify(task), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id not in tasks:
        abort(404)
    del tasks[task_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
