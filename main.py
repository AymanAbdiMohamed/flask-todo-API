from flask import Flask, jsonify, request, abort

app = Flask(__name__)

todos = []
next_id = 1


# GET /todos
# Return all todos
@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos), 200


# GET /todos/<id>
# Return a single todo by ID
@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            return jsonify(todo), 200

    abort(404, description="Todo not found")


# POST /todos
# Create a new todo
@app.route("/todos", methods=["POST"])
def create_todo():
    global next_id

    # Ensure JSON body exists and contains a title
    if not request.json or "title" not in request.json:
        abort(400, description="Title is required")

    new_todo = {
        "id": next_id,
        "title": request.json["title"],
        "completed": request.json.get("completed", False)
    }

    todos.append(new_todo)
    next_id += 1

    return jsonify(new_todo), 201


# PUT /todos/<id>
# Update an existing todo
@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    if not request.json:
        abort(400, description="Request body must be JSON")

    for todo in todos:
        if todo["id"] == todo_id:
            todo["title"] = request.json.get("title", todo["title"])
            todo["completed"] = request.json.get("completed", todo["completed"])
            return jsonify(todo), 200

    abort(404, description="Todo not found")


# DELETE /todos/<id>
# Delete a todo
@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            return jsonify({"message": "Todo deleted"}), 200

    abort(404, description="Todo not found")


# Application entry point
if __name__ == "__main__":
    app.run(debug=True)
