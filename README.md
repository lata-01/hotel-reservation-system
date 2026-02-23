# 🍽️ Agentic AI Restaurant Table Booking System

An Agentic AI-powered restaurant reservation system built using:

- ⚡ FastAPI
- 🧠 Azure OpenAI (Chat + Embeddings)
- 🔁 LangGraph (ReAct Agent Orchestration)
- 📚 ChromaDB (RAG - Restaurant Knowledge)
- 🗄️ SQLite (Bookings & Waiting List)
- 🌐 Streaming API Responses

This system allows users to:
- Search restaurants using semantic understanding
- Check real-time table availability
- Book tables
- Join waiting list when fully booked
- Interact through a streaming AI agent

---

# 🏗️ Architecture

This is a true **Agentic System** using the ReAct pattern:
- The model reasons
- Decides which tool to call
- Executes the tool
- Continues reasoning

---


---

# ⚙️ Setup Instructions

## 1️ Clone Repository

```bash
git clone <your-repo-url>
cd backend

python -m venv venv
venv\Scripts\activate   # Windows

AZURE_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_API_VERSION=2024-12-01-preview

AZURE_DEPLOYMENT=gpt-4o-mini

## 2🚀 Run the Application

Start FastAPI:

uvicorn src.main:app --reload

Server runs at:

http://127.0.0.1:8000
## 3🧪 API Endpoint
POST
/api/v1/agent/chat
Example Request
{
  "user_id": "123",
  "query": "Book a table for 4 at Spice Garden tomorrow at 7 PM"
}

The system will:

Ask for missing details if needed

Check availability using tool

Save booking if seats available

Offer waiting list if full

##🗄️ Database Schema
Hotels

name

location

max_capacity

Bookings

restaurant_name

date

start_time

end_time

number_of_person

user_name

mobile_number

Waiting List

restaurant_name

date

start_time

end_time

number_of_person

user_name

mobile_number

##🧠 Agent Capabilities

✔ Multi-step reasoning
✔ Tool selection (ReAct pattern)
✔ Real-time database interaction
✔ Capacity conflict handling
✔ Waiting list management
✔ Streaming response handling

##🛠️ Common Issues
❌ 404 DeploymentNotFound

Check Azure deployment name

Ensure correct .env configuration

Confirm deployment status is "Succeeded"

❌ ModuleNotFoundError: src

Run scripts using:

python -m src.some_module
##🚀 Future Improvements

Add RAG-based restaurant search

Add cancellation tool

Add metadata filtering

Add async DB operations

Add frontend dashboard

Add notifications system

Convert to multi-agent architecture
