# 🐦 TweetBar — Django Microblogging App

A fully-featured Twitter-inspired microblogging platform built with **Django 5** as a portfolio practice project.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Django-5.2-green?style=flat-square&logo=django)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## ✨ Features

| Feature | Details |
|---------|---------|
| 🔐 **Authentication** | Register, Login, Logout |
| ✍️ **Post Tweets** | Up to 280 characters with optional photo upload |
| ❤️ **Like / Unlike** | Toggle likes on any tweet |
| 👤 **User Profiles** | View tweet history and stats per user |
| 🔍 **Search** | Search tweets by content or username |
| 🛡️ **Permissions** | Only tweet owners can edit/delete their posts |
| 🎨 **Premium UI** | Dark glassmorphism theme with smooth animations |

---

## 🖥️ Screenshots

> Run the app locally and visit `http://127.0.0.1:8000` to see it in action.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/tweetbar.git
cd tweetbar

# 2. Create and activate virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Navigate to the project directory
cd chaiheadq

# 5. Run database migrations
python manage.py migrate

# 6. Create a superuser (optional, for admin panel)
python manage.py createsuperuser

# 7. Start the development server
python manage.py runserver
```

Visit **http://127.0.0.1:8000** in your browser.

---

## 📁 Project Structure

```
chaiheadq/
├── chaiheadq/          # Project config (settings, urls, wsgi)
├── tweet/              # Main app
│   ├── migrations/     # Database migrations
│   ├── templates/      # App-specific templates
│   ├── admin.py        # Admin configuration
│   ├── forms.py        # TweetForm + UserRegistrationForm
│   ├── models.py       # Tweet + Like models
│   ├── urls.py         # App URL patterns
│   └── views.py        # All view functions
├── templates/          # Base layout template
├── media/              # Uploaded photos (gitignored)
├── static/             # Static files
└── manage.py
```

---

## 🛠️ Tech Stack

- **Backend:** Django 5.2, Python
- **Database:** SQLite (development)
- **Frontend:** Bootstrap 5.3, Bootstrap Icons, Google Fonts (Inter)
- **Image Handling:** Pillow

---

## 📌 Key URLs

| URL | Page |
|-----|------|
| `/` | Landing page |
| `/feed/` | Tweet feed |
| `/create/` | Post a new tweet |
| `/login/` | Login |
| `/register/` | Register |
| `/profile/<username>/` | User profile |
| `/search/?q=...` | Search results |
| `/admin/` | Django admin panel |

---

## 📄 License

MIT License — feel free to use this project as a reference or portfolio piece.
