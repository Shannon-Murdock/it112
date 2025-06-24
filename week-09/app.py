from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True) #primary key column, automatically generated IDs
    title = db.Column(db.String(80), index = True, unique = True) # book title
    author_name = db.Column(db.String(50), index=True, nullable=True) # author full name
    author_surname = db.Column(db.String(50), index=True, nullable=True) # author last name
    month = db.Column(db.String(20), index = True, unique = False) #the month of book suggestion
    year = db.Column(db.Integer, index = True, unique = False) #the year of book suggestion

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return f'<User {self.name}>'

# Create database tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    if name:
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
