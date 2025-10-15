# 💧 Water Intake Tracker

A modern, AI-powered web application to help users track their daily water intake, get smart feedback, and stay hydrated. Built with Streamlit for the dashboard and FastAPI for the backend, this project demonstrates clean architecture, modular code, and practical use of AI agents.

---

## Features

- **Log Water Intake:** Users can log their daily water consumption.
- **AI Feedback:** Get personalized feedback on your water intake using an AI agent.
- **History Visualization:** View your water intake history in a clear, interactive chart.
- **Modular Design:** Clean separation of concerns with database, agent, API, and logging modules.

---

## Project Structure

```
water_tracker/
│
├── dashboard.py              # Streamlit dashboard for user interaction
│
└── src/
    ├── __init__.py           # Package initializer
    ├── agent.py              # AI agent for analyzing water intake
    ├── api.py                # FastAPI endpoints for logging and retrieving data
    ├── database.py           # Database logic for storing and fetching intake data
    ├── logger.py             # Logging configuration and helpers
    └── __pycache__/          # Python cache files
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)
- (Recommended) [virtualenv](https://virtualenv.pypa.io/en/latest/)

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/tapumaharana91/water_tracker.git
    cd water_tracker
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    venv\Scripts\activate  # On Windows
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

---

## Usage

### 1. Run the Streamlit Dashboard

From the `water_tracker` directory:
```sh
streamlit run dashboard.py
```
This will launch the web dashboard in your browser.

### 2. Run the FastAPI Backend (if applicable)

If you want to run the API separately:
```sh
uvicorn src.api:app --reload
```

---

## File Descriptions

- **dashboard.py**  
  Main entry point for the Streamlit dashboard UI.

- **src/agent.py**  
  Contains the `waterIntakeAgent` class for analyzing user intake and providing feedback.

- **src/api.py**  
  FastAPI application exposing endpoints for logging and retrieving water intake data.

- **src/database.py**  
  Handles all database operations (logging intake, fetching history).

- **src/logger.py**  
  Sets up logging for the application.

- **src/__init__.py**  
  Marks the `src` directory as a Python package.

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## License

[MIT](LICENSE)

---

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)