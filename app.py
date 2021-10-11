from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    SNo = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


def __repr__(self) -> str:
    return f"{self.SNo}-{self.title}"


@app.route('/', methods=['POST', 'GET'])
def entry_point():
    if request.method == 'POST':
        # print("post")
        # print(request.form['title'])
        # print(request.form['desc'])
        title_var = (request.form['title'])
        desc_var = (request.form['desc'])
        todo = Todo(title=title_var, desc=desc_var)

        db.session.add(todo)
        db.session.commit()

    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)


@app.route('/DDDD')
def pro():
    allTodo = Todo.query.all()
    print(allTodo)
    return 'this is product page'


@app.route('/delete/<int:SNo>')
def delete(SNo):
    todo = Todo.query.filter_by(SNo=SNo).first()

    db.session.delete(todo)
    db.session.commit()

    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True, port=8000)