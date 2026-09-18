# 🐍 Python Projects

A collection of Python projects, experiments, and small applications that I built while learning and exploring different areas of Python development.

This repository includes projects involving **GUI development, computer vision, Telegram/Bale bots, basic algorithms, text processing, and object-oriented programming**.

> This repository represents my learning journey and contains projects of different levels of complexity.

---

## 📂 Projects

| Project            | Description                                                    | Technologies                               |
| ------------------ | -------------------------------------------------------------- | ------------------------------------------ |
| `face-project/`    | Face detection / computer vision experiments                   | Python, OpenCV                             |
| `python_sentense/` | Experiments with Python text and sentence processing           | Python                                     |
| `try/`             | Small experiments and tests                                    | Python                                     |
| `bot3.py`          | Telegram bot for downloading media from SoundCloud and YouTube | Python, Telegram Bot API, Requests, PyTube |
| `bot5.py`          | Bale bot with YouTube media downloading functionality          | Python, Bale Bot API, yt-dlp               |
| `caculate.py`      | Simple desktop calculator with a graphical interface           | Python, Tkinter                            |
| `library.py`       | Command-line library management program                        | Python, OOP                                |

---

## 🤖 Telegram Media Downloader

`bot3.py` is an early Telegram bot project that I built to experiment with:

* Telegram Bot API
* Inline keyboards
* Handling user messages
* Processing URLs
* Downloading audio from SoundCloud
* Downloading audio from YouTube
* Managing simple per-user states

The bot uses Python libraries such as:

```text
requests
pytube
soundcloud_downloader
```

### Basic flow

```text
User
  ↓
/start
  ↓
Choose download option
  ↓
Send URL
  ↓
Process URL
  ↓
Download media
```

---

## 📥 Bale YouTube Downloader

`bot5.py` is another bot project built to experiment with the **Bale Bot API** and `yt-dlp`.

The bot provides options for processing a YouTube URL and downloading/transferring the resulting media.

Technologies used:

* Python
* Requests
* yt-dlp
* Bale Bot API

---

## 🧮 Calculator

`caculate.py` is a simple graphical calculator built with **Tkinter**.

It demonstrates basic GUI programming and event handling in Python.

### Operations

* Addition `+`
* Multiplication `*`
* Subtraction `-`
* Division `/`

### Run

```bash
python caculate.py
```

---

## 📚 Library Management

`library.py` is a small command-line project created to practice **Object-Oriented Programming (OOP)** in Python.

The project contains a `library` class that manages a collection of books.

### Features

* Add a book
* Show stored books
* Delete a book
* Search for a book
* Interactive command-line menu

### Example

```text
1. Add a book
2. Show books
3. Delete a book
4. Search for a book
```

### Run

```bash
python library.py
```

---

## 👁️ Face Project

The `face-project` directory contains experiments related to **face detection / computer vision**.

The project was created as part of my exploration of computer vision with Python.

---

## 🧪 Experiments

The `python_sentense` and `try` directories contain smaller experiments and learning exercises.

These projects are intentionally kept in the repository as part of my development history.

---

## 🛠️ Technologies

Throughout these projects, I have worked with:

* 🐍 Python
* 🖥️ Tkinter
* 👁️ OpenCV
* 🤖 Telegram Bot API
* 💬 Bale Bot API
* 🌐 Requests
* 🎥 yt-dlp
* ▶️ PyTube
* 🧱 Object-Oriented Programming
* 🔄 APIs
* 📦 Python packages

---

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/hoomanyyy/python_projects.git
```

Enter the directory:

```bash
cd python_projects
```

Then run the project you want to explore.

For example:

```bash
python caculate.py
```

or:

```bash
python library.py
```

Bot projects may require additional Python packages and API credentials.

---

## 🔐 Security

**Never put API tokens, bot tokens, passwords, or other secrets directly in source code.**

For bot projects, credentials should be stored using environment variables:

```python
import os

TOKEN = os.getenv("BOT_TOKEN")
```

Create a `.env` file locally if needed:

```env
BOT_TOKEN=your_token_here
```

and make sure `.env` is included in `.gitignore`.

If a token has already been committed to a public repository, **revoke/regenerate it immediately**.

---

## 📌 Project Status

These projects were created primarily for learning, experimentation, and improving my Python development skills.

Some projects are experimental and may require updates or additional configuration before running.

---

## 🎯 What I Learned

Working on these projects helped me practice:

* Python fundamentals
* Functions and classes
* Object-oriented programming
* GUI development
* API communication
* Bot development
* File and media handling
* Basic computer vision
* Working with third-party Python libraries
* Debugging and experimenting with real projects

---

## 👨‍💻 Author

**Hooman**

GitHub: [@hoomanyyy](https://github.com/hoomanyyy)

---

⭐ If you find something interesting in this repository, feel free to explore the individual projects.
