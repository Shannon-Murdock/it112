# Import Libraries to create the web app, handle incoming HTTP requests, 
# provide database, and render HTML templates
from flask import Flask, request, render_template
import sqlite3

# Initialize Flask App
app = Flask(__name__)

# Database Initialization
def init_db():
    
    # Connect to the SQLite database (or create it if it doesn't exist)
    # Create a table named 'entries' with columns 'id' (primary key) and 'name' (text)
    with sqlite3.connect('data.db') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY, name TEXT)')
        conn.commit()

# Define Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    
    # Handle both GET and POST requests for the root URL ('/')
    if request.method == 'POST':
        
        # Retrieve the 'name' field from the submitted form data
        name = request.form['name']
        
        # Insert the submitted name into the 'entries' table in the database
        with sqlite3.connect('data.db') as conn:
            conn.execute('INSERT INTO entries (name) VALUES (?)', (name,))
            conn.commit()
    
    # Render the HTML form (index.html) for both GET and POST requests
    return render_template('index.html')

# Run the Application
if __name__ == '__main__':
    
    # Initialize the database before starting the Flask app
    init_db()

    # Start the Flask development server with debugging enabled
    app.run(debug=True)
