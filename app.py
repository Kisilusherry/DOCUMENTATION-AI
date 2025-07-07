from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database URI
# Use three slashes (///) for a relative path, four (////) for an absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable unnecessary tracking feature
db = SQLAlchemy(app)  # Initialize SQLAlchemy with the app


# ------------------------
# Database Model
# ------------------------

class Todo(db.Model):
    """
    Model representing a single to-do item.

    Attributes:
        id (int): Primary key, unique task identifier.
        title (str): Description of the task.
        complete (bool): Task completion status.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


# ------------------------
# Route: Home Page
# ------------------------

@app.route("/")
def home():
    """
    Render the homepage with the list of all to-do items.

    Returns:
        str: Rendered HTML page with tasks.
    """
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)


# ------------------------
# Route: Add New Task
# ------------------------

@app.route("/add", methods=["POST"])
def add():
    """
    Handle adding a new task from form input.

    Reads 'title' from form, creates a new Todo object, commits it to the DB.
    Redirects to the homepage.
    """
    title = request.form.get("title")  # Get title from form
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))


# ------------------------
# Route: Update Task (toggle complete)
# ------------------------

@app.route("/update/<int:todo_id>")
def update(todo_id):
    """
    Toggle the completion status of a task by its ID.

    Args:
        todo_id (int): ID of the task to update.
    """
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete  # Flip the status
    db.session.commit()
    return redirect(url_for("home"))


# ------------------------
# Route: Delete Task
# ------------------------

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    """
    Delete a task from the database by its ID.

    Args:
        todo_id (int): ID of the task to delete.
    """
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


# ------------------------
# App Entry Point
# ------------------------

if __name__ == "__main__":
    db.create_all()  # Create database tables if not already present
    app.run(debug=True)
