from flask import Flask, render_templates, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite3:///'
db = SQLAlchemy(app)


class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, defult=0)
    date_created = db.Column(db.DateTime, defult=datetime.utcnow)

    def __repr__(self):
        return '<Task %id' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        pass
    else:
        render_templates('index.html')
    return render_templates('index.html')


if __name__ == '__main__':
    app.run()
