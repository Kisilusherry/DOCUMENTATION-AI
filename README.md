
# 📝 Flask To-Do List Application

A **simple and functional To-Do web app** built with **Python**, **Flask**, and **SQLite**. This project is ideal for beginners who want to learn web development using Flask.

---

## 📌 Overview

This app allows users to:
- ✅ Add new to-do items
- ✏️ Update (mark complete/incomplete)
- 🗑 Delete items
- 📦 Persist data using a lightweight SQLite database

The user interface is built using **Semantic UI** for a clean, responsive layout.

---

## 🧰 Technologies Used

| Component    | Description                          |
|--------------|--------------------------------------|
| Python       | Backend programming language         |
| Flask        | Micro web framework                  |
| SQLAlchemy   | ORM (Object Relational Mapper)       |
| SQLite       | Local file-based database            |
| Semantic UI  | Frontend CSS framework               |
| HTML (Jinja) | Template rendering engine (Flask)    |

---

## 🚀 Getting Started — No Experience Needed

Follow these **step-by-step instructions** to run the app on your laptop.

### 1️⃣ Install Python (if you don't have it)

- Visit [https://www.python.org/downloads/](https://www.python.org/downloads/)  
- Download the latest version (e.g., Python 3.11+)
- Install it, and make sure to check **"Add Python to PATH"**

To confirm it's working, open a terminal or command prompt and run:

```bash
python --version
````

---

### 2️⃣ Clone the Project

If you have Git installed:

```bash
git clone https://github.com/patrickloeber/flask-todo.git
cd flask-todo
```

**OR** download it as a ZIP:

* Click the green **“Code”** button on the repo
* Choose **“Download ZIP”**
* Extract it, then navigate into the folder

---

### 3️⃣ (Optional) Create a Virtual Environment

This step helps isolate your app dependencies:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

---

### 4️⃣ Install the Required Packages

If there's a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

If not, run this instead:

```bash
pip install flask flask_sqlalchemy
```

---

### 5️⃣ Run the App Locally

```bash
python app.py
```

If successful, you’ll see something like:

```
* Running on http://127.0.0.1:5000/
```

Open your browser and go to that address to use the app!

---

## 🧪 Project Structure

```
flask-todo/
│
├── app.py              # Main Flask application
├── db.sqlite           # SQLite database file (created automatically)
├── requirements.txt    # Python package dependencies
│
├── templates/
│   └── base.html       # HTML UI with embedded Jinja2 code
│
├── static/             # For optional custom CSS/JS
└── README.md           # This file
```

---

## 🧠 How the App Works

### Database Model (`Todo`)

```python
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
```

### Flask Routes

| URL Path            | Method | Purpose                    |
| ------------------- | ------ | -------------------------- |
| `/`                 | GET    | Show list of all to-dos    |
| `/add`              | POST   | Add a new task             |
| `/update/<todo_id>` | GET    | Toggle complete/incomplete |
| `/delete/<todo_id>` | GET    | Delete a task              |

---

## 🛠 Customization Ideas

You can modify or extend the app in many ways:

* ✅ Add **due dates** to tasks
* ✅ Add **user login** with Flask-Login
* ✅ Filter tasks (e.g., only show completed)
* ✅ Add **flash messages** on update/delete
* ✅ Use **Bootstrap** instead of Semantic UI
* ✅ Convert to a **RESTful API**

---

## 🧹 Troubleshooting

| Issue                        | Solution                                                  |
| ---------------------------- | --------------------------------------------------------- |
| `ModuleNotFoundError: flask` | Run `pip install flask flask_sqlalchemy`                  |
| `db.sqlite` not found        | It’s auto-created when `db.create_all()` runs in `app.py` |
| Nothing happens on "Add"     | Ensure the input field is filled and the form uses POST   |
| App doesn't look styled      | Ensure you're connected to the internet (Semantic UI CDN) |

---

## 📦 Example `requirements.txt`

```txt
flask
flask_sqlalchemy
```

Save this file and run:

```bash
pip install -r requirements.txt
```

---

## ✅ Best Practices

* Use `.gitignore` to ignore files like `__pycache__`, `.env`, and `db.sqlite`
* Never expose real database credentials or secret keys in production
* Use `debug=False` in production environments

---

## 📜 License

This project is licensed under the MIT License.  
You are free to use, modify, and distribute it as you wish.

---

## 👨‍💻 Author & Credits

- **Built by:** [Patrick Loeber](https://github.com/patrickloeber/flask-todo)  
- **Documentation by:** Sherry Kisilu

If you found this project helpful or informative, feel free to ⭐ star the repo or fork it and make it your own!

---

