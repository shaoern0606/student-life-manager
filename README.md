# Student Life Manager

A smart AI assistant that helps students plan their weekly schedule by combining **study planning**, **entertainment planning**, and **transport planning**. The system orchestrates multiple agents to provide optimized study sessions, indoor/outdoor entertainment recommendations, and transport directions.

---

## System Architecture (A2A Flow)

The system follows an **Agent-to-Agent (A2A) orchestration** model:

```text
User Input
   │
   ▼
Root Agent (Coordinator)
   ├─ Study Planner Agent
   │    ├─ Google Search Sub-Agent
   │    └─ URL Context Sub-Agent
   ├─ Entertainment Planner Agent
   │    ├─ Indoor Entertainment Agent
   │    │    ├─ Google Search Sub-Agent
   │    │    └─ URL Context Sub-Agent
   │    └─ Outdoor Entertainment Agent
   │         ├─ Google Search Sub-Agent
   │         └─ URL Context Sub-Agent
   └─ Transport Planner Agent
        ├─ Google Search Sub-Agent
        └─ URL Context Sub-Agent
```

## Functional Diagram 1

![Functional Diagram 1](https://drive.google.com/uc?export=view&id=1PYLLZeUCFqC_2xPH8w1b3WF76tZS4R5I)

## Functional Diagram 2

![Functional Diagram 2](https://drive.google.com/uc?export=view&id=1b7j_UMeHDMjfUIVBXKx7v9LeowKMfBfq)

---

## Agent Profiles

| Agent Name | Role Description |
|------------|-----------------|
| **Root Agent (Coordinator)** | Orchestrates all tasks, merges study, entertainment, and transport plans, and provides reasoning logs. |
| **Study Planner Agent** | Plans study sessions based on assignments, exams, free slots, and user preferences. |
| **Entertainment Planner Agent** | Decides between indoor and outdoor activities and delegates to corresponding agents. |
| **Indoor Entertainment Agent** | Suggests indoor activities like reading, gaming, or hobbies based on user preferences. |
| **Outdoor Entertainment Agent** | Suggests outdoor activities and requests transport planning for each activity. |
| **Transport Planner Agent** | Calculates optimal travel routes including distance, estimated time, and transport modes. |
| **Google Search Sub-Agents** | Perform web searches to provide real-time information to their parent agents. |
| **URL Context Sub-Agents** | Fetch and summarize content from URLs to inform the parent agents’ decisions. |

---

## Setup Instructions

### Prerequisites
- Python 3.13+  
- Docker (for containerized deployment)  
- Google Cloud account (optional, for deployment on Cloud Run)  
- Gemini API Key for LLM access  

### Local Setup
#### Primary Method: ADK Web (Recommended)
---
1. Clone the repository:
```bash
git clone <your-repo-url>
cd studentlifemanager
```
2. Create a virtual environment and activate it:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Set your Gemini API Key:
```bash
export GOOGLE_API_KEY="your_api_key_here"
```
5. Start the ADK Web UI:
```bash
adk web
```
#### Alternative: FastAPI Server
---
If you prefer programmatic access via HTTP requests:
1.	Make sure main.py in app/ has:

```bash
from fastapi import FastAPI
from agents.agent import root_agent

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Student Life Manager AI running"}

@app.post("/run")
async def run_agent(user_input: str):
    response = await root_agent.run(user_input)
    return {"response": response}
```
2.	Run FastAPI locally:
```bash
uvicorn app.main:app --reload
```
3.	Access API at http://127.0.0.1:8000
Example POST request:
```bash
POST /run
{
    "user_input": "I want to plan my week. Assignments: Math due Wednesday. Free slots: Monday 3-6pm."
}
```
Expected response:
```bash
{
    "response": "Your weekly schedule has been created. Study Math on Monday 3-5pm. Physics review on Tuesday 2-4pm. Indoor gaming on Monday evening. Transport routes included."
}
```

---
### Docker Deployment
1. Build Docker image:
```bash
docker build -t student-life-manager .
```
2. Run container:
```bash
docker run -d -p 8000:8000 --name slm_app student-life-manager
```
3. Access the app at http://localhost:8000

---
### Cloud Deployment (Optional)
1.	Authenticate with Google Cloud:
```bash
gcloud auth login
gcloud config set project studentlifemanager-490209
gcloud auth configure-docker
```
2. Deploy to Cloud Run from source:
```bash
gcloud run deploy student-life-manager \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8000
```
3. Add your Gemini API Key in Cloud Run → Environment Variables:
```bash
Key: GOOGLE_API_KEY
Value: your_api_key_here
```
