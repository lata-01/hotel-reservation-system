# 🍽️ Agentic AI Restaurant Table Booking System

An Agentic AI-powered restaurant reservation system built using:

* ⚡ FastAPI
* 🧠 Azure OpenAI (Chat Model)
* 🔁 LangGraph (ReAct Agent Orchestration)
* 🗄️ SQLite (Bookings & Waiting List)
* 🌐 Streaming API Responses

This system allows users to:

* Check real-time table availability
* Book tables
* Join waiting list when fully booked
* Interact with an AI agent using natural language
* Receive streaming responses with tool execution details

---

# 🏗️ Architecture

This is a true **Agentic System** using the ReAct pattern:

1. The model reasons about the request
2. Decides which tool to call
3. Executes the tool
4. Uses the result to continue reasoning
5. Returns final response

```
User → FastAPI → LangGraph ReAct Agent
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

# ⚙️ Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd backend
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

## 3️⃣ Install Dependencies

```bash
pip install fastapi uvicorn langchain langchain-openai langgraph
```

---

## 4️⃣ Create `.env` File

Create a `.env` file in the backend root directory:

```
AZURE_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_API_VERSION=2024-12-01-preview
AZURE_DEPLOYMENT=gpt-4o-mini
```

⚠ Use your actual Azure deployment name.

---

# 🚀 Run the Application

Start FastAPI:

```bash
uvicorn src.main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

# 🧪 API Endpoint

### POST

```
/api/v1/agent/chat
```

### Example Request

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
✔ Dynamic tool selection (ReAct pattern)
✔ Real-time database interaction
✔ Capacity conflict handling
✔ Waiting list management
✔ Streaming response handling

---

# 🛠️ Common Issues

### ❌ 404 DeploymentNotFound

* Check Azure deployment name
* Ensure correct `.env` configuration
* Confirm deployment status is **Succeeded**

### ❌ ModuleNotFoundError: src

Run scripts using:

```bash
python -m src.module_name
```

---

# 🚀 Future Improvements

* Add RAG-based restaurant search
* Add booking cancellation tool
* Add metadata filtering
* Add async database operations
* Add frontend dashboard
* Add notifications system
* Convert to multi-agent architecture

---
