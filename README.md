# World In Live 🌐

A real-time news aggregator web application built with Python and Flask. It fetches live RSS feeds from major news outlets using `feedparser`, extracts headlines and summaries, and renders them dynamically across different categories.

🔗 **Live Demo:** [world-in-live.onrender.com](https://world-in-live.onrender.com)

---

## Features

* **Real-time News:** Fetches live headlines across various categories (World, Technology, Business, Sports).
* **Dynamic Rendering:** Server-side template rendering powered by Jinja2.
* **Responsive UI:** Clean, modern card layout built with CSS for desktop and mobile devices.
* **Production Deployment:** Deployed using Gunicorn as a WSGI server on Render.

---

## Tech Stack

* **Backend:** Python, Flask
* **Feed Ingestion:** Feedparser
* **Production Server:** Gunicorn
* **Frontend:** HTML5, CSS3, Jinja2 Templates
* **Hosting:** Render

---

## Project Structure

```text
News-Aggregator/
├── templates/
│   └── index.html       # Jinja2 frontend template
├── app.py               # Flask application logic and RSS routing
├── requirements.txt     # Python project dependencies
├── .gitignore           # Git ignore file for virtual environment
└── README.md            # Project documentation
