from flask import Flask, jsonify, request, abort

app = Flask(__name__)

todos = []
next_id = 1


# GET /todos and GET all todos
@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos), 200



# GET /todos/<id> and GET a single todo by ID
@app.route("/todos/<int:todo_id", methods=["GET"])
def get_todo(todo_id):
    for todo in todos:
        if todo["id"] ==todo_id:
            return jsonify(todo), 200