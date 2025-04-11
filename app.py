from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Ensure upload folder exists
UPLOAD_FOLDER = 'static/id_proofs'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Apply for bus pass
@app.route('/apply', methods=['GET', 'POST'])
def apply():
    if request.method == 'POST':
        name = request.form['name']
        college = request.form['college']
        route = request.form['route']
        duration = request.form['duration']

        # ✅ Handle file upload safely
        if 'id_proof' not in request.files:
            return "❌ ID proof file is missing!"
        id_file = request.files['id_proof']

        # Save file
        filename = name.replace(" ", "_") + "_ID_" + id_file.filename
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        id_file.save(filepath)

        conn = sqlite3.connect('buspass.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO applications (name, college, route, duration, status, id_path) VALUES (?, ?, ?, ?, ?, ?)",
                       (name, college, route, duration, 'Pending', filepath))
        conn.commit()
        conn.close()

        return render_template('success.html', name=name)
    return render_template('apply_pass.html')

# Admin login (from database)
@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('buspass.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM admins WHERE username = ? AND password = ?", (username, password))
        admin = cursor.fetchone()

        if admin:
            cursor.execute("SELECT * FROM applications")
            data = cursor.fetchall()
            conn.close()
            return render_template('admin_dashboard.html', applications=data)
        else:
            conn.close()
            return render_template('admin_login.html', error="❌ Invalid credentials")
    
    return render_template('admin_login.html')

# Update status (Approve/Reject)
@app.route('/update_status/<int:app_id>', methods=['POST'])
def update_status(app_id):
    new_status = request.form['status']
    conn = sqlite3.connect('buspass.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE applications SET status = ? WHERE id = ?", (new_status, app_id))
    conn.commit()
    conn.close()
    return redirect('/admin')

# Track My Application (student view)
@app.route('/track', methods=['GET', 'POST'])
def track_application():
    if request.method == 'POST':
        name = request.form['name']
        conn = sqlite3.connect('buspass.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, route, duration, status FROM applications WHERE name = ?", (name,))
        result = cursor.fetchone()
        conn.close()

        if result:
            return render_template('track_status.html', status=result[3], route=result[1], duration=result[2], id=result[0])
        else:
            return render_template('track_status.html', status=None)
    return render_template('track_status.html')

# Digital bus pass page
@app.route('/pass/<int:app_id>')
def view_pass(app_id):
    conn = sqlite3.connect('buspass.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, college, route, duration, status FROM applications WHERE id = ?", (app_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return render_template('bus_pass.html',
                               name=row[0],
                               college=row[1],
                               route=row[2],
                               duration=row[3],
                               status=row[4])
    else:
        return "No pass found for this ID."

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
