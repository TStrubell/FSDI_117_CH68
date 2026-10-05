# SGnG Portfolio  
### Strubell Goods & Gear · Strubell Publishing LLC  
### Built with Django · FSDI 117 · Cohort 68

---

## 📌 Overview

This portfolio represents the unified technical, architectural, and documentation work of **Timothy O. Strubell** — veteran, developer, and founder of **Strubell Goods & Gear (SGnG)** and **Strubell Publishing LLC**.

The project was built as part of the **Full Stack Development Immersive (FSDI)** program at **San Diego Global Knowledge University**, integrating:

- Django models  
- Admin configuration  
- SGnG‑branded templates  
- Static and media handling  
- Project and skill management  
- Contact form (Assignment 3)  
- Full assignment documentation (Assignments 1–4)

---

## 🧱 Tech Stack

- **Python 3.x**
- **Django 4.x**
- **HTML / CSS (SGnG Theme)**
- **SQLite (default Django DB)**
- **VS Code**
- **GitHub**

---

## 📂 Project Structure

portfolio/
│
├── templates/portfolio/
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── experience.html
│   ├── projects.html
│   ├── skills.html
│   └── contact.html
│
├── static/css/styles.css
│
├── models.py
├── views.py
└── admin.py

---

## 🗂️ Features

### ✔ Dynamic Project Cards  
Projects are stored in the database and rendered dynamically on `/projects/`.

### ✔ Dynamic Skill Cards  
Skills are stored in the database and rendered dynamically on `/skills/`.

### ✔ SGnG‑Branded UI  
Custom CSS theme inspired by SGnG’s design language:

- Cambria typography  
- SGnG Navy (`#0b1120`)  
- SGnG Teal (`#66fcf1`)  
- SGnG Orange (`#f97316`)  

### ✔ Django Admin Integration  
Full CRUD support for Projects and Skills.

### ✔ Contact Form (Assignment 3)  
Email functionality implemented using Django’s `send_mail`.

---

## 🛠️ Installation

- ```bash
- git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME
- cd YOUR_REPO_NAME
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver

---

### 📸 Screenshots
Screenshots for Assignments 1–4 are included in the submission documents.

---

### 📬 Contact
Email: tim.strubell@icloud.com
Location: Louisville, Kentucky
Brand: Strubell Goods & Gear · Strubell Publishing LLC

---

### 🤖 AI Disclosure
AI assistance was used for debugging, documentation, and template refinement.
All final code was written, tested, and validated by the developer.

© 2026 Strubell Publishing LLC · SGnG
