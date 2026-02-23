# 🍽️ Agentic AI Restaurant Table Booking System

A full-stack Agentic AI-powered restaurant reservation system built using:

## 🔹 Backend

* ⚡ FastAPI
* 🧠 Azure OpenAI (Chat Model)
* 🔁 LangGraph (ReAct Agent)
* 🗄️ SQLite (Bookings & Waiting List)
* 🌐 Streaming API responses

## 🔹 Frontend

* ⚛️ React
* 🔄 Real-time streaming display
* 💬 Interactive chat interface

---

# 🏗️ System Architecture

```
Frontend (React)
        ↓
FastAPI Backend
        ↓
LangGraph ReAct Agent
        ↓
-----------------------------------------
| Current Date Tool                     |
| Check Availability Tool (SQLite)      |
| Save Booking Tool (SQLite)            |
| Join Waiting List Tool (SQLite)       |
-----------------------------------------
        ↓
Azure OpenAI (Chat Model)
```

---

# 📁 Project Structure

```
project-root/
│
├── backend/
│   ├── src/
│   ├── main.py
│   └── ...
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── ...
│
└── README.md
```

---

# ⚙️ Setup Instructions

## 🔹 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd project-root
```

---

# 🧠 Backend Setup

## 2️⃣ Navigate to Backend

```bash
cd backend
```

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

## 4️⃣ Install Dependencies

```bash
pip install fastapi uvicorn langchain langchain-openai langgraph
```

## 5️⃣ Create `.env` File

Create a `.env` file inside `backend/`:

```
AZURE_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_API_VERSION=2024-12-01-preview
AZURE_DEPLOYMENT=gpt-4o-mini
```

⚠ Make sure deployment name matches Azure.

---

## 6️⃣ Run Backend

From `backend/` folder:

```bash
python main.py
```

OR

```bash
uvicorn src.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

# 💻 Frontend Setup (React)

## 7️⃣ Navigate to Frontend

Open new terminal:

```bash
cd frontend
```

## 8️⃣ Install Node Dependencies

```bash
npm install
```

## 9️⃣ Run Frontend

```bash
npm run dev
```

Frontend runs at:

```
http://localhost:3000
```

---

# 🚀 How to Run Full System

### Terminal 1

```
cd backend
uvicorn src.main:app --reload
```

### Terminal 2

```
cd frontend
npm run dev
```

Then open:

```
http://localhost:3000
```

---

# 🧪 API Endpoint

```
POST /api/v1/agent/chat
```

Example Request:

```json
{
  "user_id": "123",
  "query": "Book a table for 4 at Spice Garden tomorrow at 7 PM"
}
```

---

# 🗄️ Database Schema

## Hotels

* name
* location
* max_capacity

## Bookings

* restaurant_name
* date
* start_time
* end_time
* number_of_person
* user_name
* mobile_number

## Waiting List

* restaurant_name
* date
* start_time
* end_time
* number_of_person
* user_name
* mobile_number

---

# 🧠 Agent Capabilities

✔ Multi-step reasoning
✔ Tool selection (ReAct pattern)
✔ Real-time database interaction
✔ Capacity conflict handling
✔ Waiting list management
✔ Streaming responses to frontend

---

# 🛠️ Common Issues

### ❌ 404 DeploymentNotFound

* Check Azure deployment name
* Verify `.env`
* Confirm deployment status is "Succeeded"

### ❌ CORS Errors

Make sure FastAPI CORS middleware allows frontend origin.

---

# 🔮 Future Improvements

* Add RAG-based restaurant search
* Add booking cancellation
* Add user authentication
* Add admin dashboard
* Add notification system
* Convert to multi-agent system

---


