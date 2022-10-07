from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Instantiate new Flask app
app = Flask(__name__)

# Set configuation for new SQLite database
# This is the URI to specify the database we can to establish a connection with
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# This disables tracking and thereby uses less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Connect the application with SQLAlchemy
db = SQLAlchemy(app)

# Create a model for todo items with id, title, and complete (completion status) columns
class Todo(db.Model):
    # id is a primary key, meaning it is used to identify the uniqueness of rows in a table
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

# In Flask, each route is associated with a function that will handle the logic for that URL
@app.route("/")
def home():
    # Get all the todo items from the database
    todo_list = Todo.query.all();
    # Render the HTML file "base.html" and pass in the todo items as an argument
    return render_template("base.html", todo_list=todo_list)

# Create functionality for adding a todo list item
# POST request since this is triggered when the user hits enter or clicks "Add"
@app.route("/add", methods=["POST"])
def add():
    # Get the todo list title (the task) from the "form" or input field
    title = request.form.get("title")
    # Create a new Todo object based on the defined Todo model above
    new_todo = Todo(title=title, complete=False)
    # Add the new todo item to the database
    db.session.add(new_todo)
    # Each time we alter the database a new session is started
    # At the end of the "transaction", we have to commit in order to end it
    db.session.commit()
    # Redirect back to the home function which will display the newly updated list of todos
    return redirect(url_for("home"))

# Create the update functionality, i.e. changing the completion status of a todo item
# This route requires the todo item's id (passed in from base.html) in order to 
# access the correct element in the database
@app.route("/update/<int:todo_id>")
def update(todo_id):
    # Get the todo item in the database
    # First will make sure only one item is returned
    todo = Todo.query.filter_by(id=todo_id).first()
    # Set the completion status to the opposite of what it is currently
    todo.complete = not todo.complete
    # End the session
    db.session.commit()
    # Redirect back to home, which will display the updated todo list items
    return redirect(url_for("home"))

# Create the delete functionality
# As with the update functionality, this requires the todo item's id which is passed in
# from the base.html file
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    # Find the todo item the user would like to delete
    todo = Todo.query.filter_by(id=todo_id).first()
    # Remove the todo item from the database
    db.session.delete(todo)
    # End the session by committing
    db.session.commit()
    # Return back to "home", which will query again for a list of all Todo items
    # This list will now not include the deleted todo item
    return redirect(url_for("home"))
    

if __name__ == "__main__":
    # SQLAlchemy needs an active application context, so this ensures we don't get an
    # error when trying to open the app
    with app.app_context():
        # This method creates all the tables in the database
        db.create_all()
    app.run(debug=True)