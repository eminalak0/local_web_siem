# Local Web SIEM
This is a **Python-based local web SIEM (Security Information and Event Management) tool** that collects logs from different sources and displays them in a web dashboard. It is a beginner-to-intermediate level cybersecurity project that can be used for portfolio purposes.

---

## Features
- Collects logs via a REST API
- Stores logs in a local SQLite database (`logs.db`)
- Displays logs on a **web dashboard** that auto-refreshes every few seconds
- Supports log severity levels: **INFO**, **WARN**, **CRIT**
- Beginner-friendly and easy to extend with filtering, alerts, or visualizations

---

## How to Use
1. Ensure you have **Python 3.x** installed.
2. Clone the repository or download the files.
3. Open the project folder in VS Code or any Python editor.
4. Create and activate a **Python virtual environment**.
5. Install required dependencies from `requirements.txt`.
6. Run the Flask web application.
7. Open the dashboard in a browser at `http://127.0.0.1:5000/`.

---

## Project Structure
- `app.py` → Flask backend
- `db.py` → Initializes the SQLite database
- `logs.db` → SQLite database (auto-created, do not include in GitHub)
- `requirements.txt` → Python dependencies
- `templates/` → HTML files for the dashboard
- `static/` → JS and CSS files for the dashboard

---

## Next Steps / Improvements
- Add filtering by log type or severity
- Add alerts for critical logs
- Add charts or visualizations for trends
- Add authentication to secure the dashboard
