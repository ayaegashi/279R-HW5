# 279R HW4: To-Do List App using Flask

## Reflection

#### What are the significant software concepts that this combination of technologies has that each previous set of technologies did not? Or that they handle significantly differently?

A major difference between Flask and some of the other software combinations we have used is how the database is integrated into my todo list app. In previous Tier 1 homeworks, we used MongoDB and Firebase, each of which requires the developer to set up the database externally and then link it into the code. In comparison, this Flask app uses a SQLite database, which we instantiated directly in the app.py file. In addition, we used SQLAlchemy, an ORM library that allows us to manipulate the data without writing actual SQL. Thus, since the database and the app are more integrated in Flask, this allows the developer to remain in their code editor. On the other hand, there is not one dashboard developers can go to to visually see their database entries as well as any statistics. For example, in order to examine the SQLite database you can download the SQLite DB Browser.

Besides the difference in database integration, Flask felt similar to Svelte and JSX in React as it integrates the HTML and dynamic functionality quite intuitively. One difference was that each functionality was associated with a different route, which was not necessary in Svelte.

## Citations

This to-do list app was created by following this online tutorial: https://www.python-engineer.com/posts/flask-todo-app/

In order to create the strike-through effect for completed tasks, I also referenced this answer on StackOverflow: https://stackoverflow.com/questions/67327845/flask-python-add-strikethrough-styling-to-todo-list-item-in-flask-app

I also looked into SQLAlchemy by referencing https://www.sqlalchemy.org/


## How to Open my To-Do List App

