# HRMS Lite - API-First Human Resource Management System

A lightweight, robust backend system for managing employee records and tracking daily attendance. Designed with an **API-First architecture**, utilizing FastAPI's interactive documentation as the primary administrative interface.

## 🚀 Live Application
- **Live Deployment:** [PASTE YOUR RENDER URL HERE]
- **GitHub Repository:** https://github.com/GauravT19/HRMS-lite

> **Note:** Clicking the Live Deployment link will open the **Interactive Dashboard (Swagger UI)** immediately.

---

## 📖 Project Overview
HRMS Lite is designed to simulate essential HR operations. Instead of a traditional decoupled frontend, this project leverages **FastAPI's auto-generated interactive documentation** to provide a functional, zero-overhead user interface. This ensures strict type safety, rapid development, and immediate testing capabilities.

### Key Features
* **Employee Management:** Register, view, and delete employees.
* **Attendance Tracking:** Mark daily attendance (Present/Absent) with date validation.
* **History Logs:** View detailed attendance history for any employee.
* **Data Persistence:** Uses **PostgreSQL** in production (via Render) and **SQLite** for local development.
* **Validation:** Automatic email uniqueness checks and data schema validation using Pydantic.

---

## 🛠 Tech Stack
* **Language:** Python 3.9+
* **Framework:** FastAPI
* **Database:** PostgreSQL (Production), SQLite (Local)
* **ORM:** SQLAlchemy
* **Validation:** Pydantic V2
* **Server:** Uvicorn

---

Using the **Swagger UI** as the frontend:
1.  **Reliability:** Eliminates client-side state errors and CORS issues.
2.  **Speed:** Focuses effort on robust business logic and database modeling rather than UI styling.
3.  **Standardization:** Provides a standard interface used by developers and QA engineers globally.

---

## ⚙️ Steps to Run Locally

### Prerequisites
* Python 3.8 or higher
* Git

### Installation
1.  **Clone the repository**
    ```bash
    git clone [PASTE YOUR GITHUB REPO LINK HERE]
    cd hrms-backend
    ```

2.  **Create a Virtual Environment** (Recommended)
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application**
    ```bash
    uvicorn main:app --reload
    ```

5.  **Access the Dashboard**
    Open your browser and navigate to:
    `http://127.0.0.1:8000`

---

## 🧪 Usage Instructions (How to test)

Since the UI is technical, follow these steps to test the functionality:

1.  **Add an Employee:**
    * Click `POST /employees`.
    * Click **Try it out**.
    * Edit the JSON body (change name/email).
    * Click **Execute**.
2.  **Mark Attendance:**
    * Copy the `id` of the employee you just created.
    * Click `POST /attendance`.
    * Click **Try it out**.
    * Paste the `employee_id` and set the status (e.g., "Present").
    * Click **Execute**.
3.  **View History:**
    * Click `GET /attendance/{employee_id}`.
    * Enter the ID and click **Execute**.

---

## ⚠️ Assumptions & Limitations
1.  **UI:** The application uses Swagger UI for interaction. It is functional but intended for internal/admin use rather than general employees.
2.  **Database:** The local setup uses SQLite for simplicity. The Render deployment uses a persistent PostgreSQL instance.
