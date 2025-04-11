<<<<<<< HEAD
# 🚌 Cloud-Based Bus Pass System

A smart, secure, and professional web-based application to manage student bus pass applications and approvals. Built using **Flask**, **SQLite**, and **Python**, this system is part of my internship with **CodeAlpha**, April 2025.

---

## 🌟 Features

### 👨‍🎓 Student Side
- 📝 Apply for a new bus pass by submitting details and ID proof
- 📤 Upload ID proof (PDF, PNG, JPG)
- 🔍 Track your application status
- 🪪 View a digital bus pass if approved

### 🧑‍💼 Admin Side
- 🔐 Secure login
- 📋 View all applications
- ✅ Approve/Reject using dropdowns
- 📎 View uploaded ID proofs
- 📬 Track status in real time

---

## 🛠️ Tech Stack

| Tech        | Use Case                       |
|-------------|--------------------------------|
| Python      | Core backend logic             |
| Flask       | Web framework                  |
| SQLite      | Database (lightweight & local) |
| HTML/CSS    | UI styling and layout          |
| Jinja2      | Flask templating               |

---

## 📁 Project Structure

cloud-bus-pass/ ├── static/ │ └── id_proofs/ # Uploaded ID files ├── templates/ │ ├── index.html │ ├── apply_pass.html │ ├── success.html │ ├── admin_login.html │ ├── admin_dashboard.html │ ├── track_status.html │ └── bus_pass.html ├── buspass.db # SQLite DB ├── app.py # Main Flask app └── README.md # You're here!

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/sahana-portfolio/cloud-bus-pass-system.git
cd cloud-bus-pass-system
pip install flask


🛠 Initialize Database
# In Python shell
import sqlite3
conn = sqlite3.connect('buspass.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    college TEXT,
    route TEXT,
    duration TEXT,
    status TEXT,
    id_path TEXT
)''')

cursor.execute('''CREATE TABLE admins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)''')

cursor.execute("INSERT INTO admins (username, password) VALUES ('admin', 'admin123')")
conn.commit()
conn.close()

▶️Run the app
python app.py

Then open:
👉 http://127.0.0.1:5000/

📸 Screenshots

### 📝 Apply Page  
![Apply Page](https://raw.githubusercontent.com/sahana-portfolio/cloud-bus-pass-system/main/apply.png)

### 🧑‍💼 Admin Dashboard  
![Admin Dashboard](https://raw.githubusercontent.com/sahana-portfolio/cloud-bus-pass-system/main/admin.png)

### 🪪 Digital Bus Pass  
![Digital Pass](https://raw.githubusercontent.com/sahana-portfolio/cloud-bus-pass-system/main/pass.png)

=======
# cloud-bus-pass-system
A cloud-based smart web app for managing college student bus pass applications.
>>>>>>> 56e6e29990986ddc1efb36d97fa38955337815eb
