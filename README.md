# 🚀 QR-Based Form Submission System

A FastAPI-based backend project that allows organizations to generate QR codes linked to custom forms. Users can scan the QR, fill out the form, and submit their responses, which are stored locally.

---

## 📌 Features

* 📄 Dynamic form generation for different organizations
* 🔗 Unique QR code for each organization
* 🧾 Form submission handling
* 💾 Data stored in JSON files
* 🌐 FastAPI backend with Jinja2 templates
* 🎨 Static files support (CSS, QR images)

---

## 🛠️ Tech Stack

* Backend: FastAPI
* Templating: Jinja2
* Language: Python
* Storage: JSON (file-based)
* QR Generation: Custom module (`qr.py`)

---

## 📁 Project Structure

```
Alpha/
│
├── main.py              # Entry point
├── app.py               # Main FastAPI logic
├── qr.py                # QR code generation
├── requirements.txt
│
├── templates/           # HTML templates
│   ├── form.html
│   ├── admin.html
│   ├── qr_page.html
│   └── register_org.html
│
├── static/
│   ├── css/
│   └── qr/              # Generated QR images (ignored in git)
│
├── db_user.json         # User submissions (optional ignore)
├── db_org.json          # Organization data (optional ignore)
└── info.txt             # Ignored file
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone <your-repo-url>
cd Alpha
```

### 2️⃣ Create virtual environment

```
python -m venv venv
```

### 3️⃣ Activate environment

**Windows:**

```
venv\Scripts\activate
```

**Mac/Linux:**

```
source venv/bin/activate
```

### 4️⃣ Install dependencies

```
pip install -r requirements.txt
make a 
```

---

## ▶️ Run the Server

```
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
check http://127.0.0.1:8000/docs to check API working
check http://127.0.0.1:8000/register-org it will redirect you to a QR page after registering once the QR is scanned a form will open and it will store data
```

---

## 📷 How It Works

1. Register an organization
2. QR code is generated
3. User scans QR
4. Form opens in browser
5. User submits data
6. Data stored in JSON

---

## 🚫 .gitignore Notes

The following are ignored:

* `venv/`
* `__pycache__/`
* `static/qr/`
* `info.txt`

---

## 🔮 Future Improvements

* Use database
* Add authentication for admin
* Deploy on cloud (Render)
* Add analytics dashboard

---

## 👨‍💻 Author

Ashutosh

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
