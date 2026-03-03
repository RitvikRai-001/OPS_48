# 🏥 CareSphere - AI-Powered Healthcare Management Platform

> **🏆 Built for Hackathon Excellence**

**CareSphere** is a comprehensive, AI-driven healthcare management platform that revolutionizes medication adherence and patient care through intelligent automation, predictive analytics, and seamless integration with modern healthcare workflows.

---

##  Table of Contents
- [Overview](#overview)
- [Features](#features)
  - [Basic Features](#basic-features)
  - [Advanced Features](#advanced-features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Folder Structure](#folder-structure)
- [Future Roadmap](#future-enhancements)
---

##  Overview

The *CareSphere* helps users set up personalized medication schedules and ensures timely intake through intelligent reminders and visual tracking dashboards.  
Advanced AI features enhance user engagement by learning patterns and providing proactive suggestions.

---

##  Features

###  Basic Features
1. *Medicine Schedule Setup:*  
   Users can add pill name, dosage, time, and frequency.

2. *Smart Notifications:*  
   Receive timely reminders via *browser alerts* and *email*(this is not yet implemented).

3. *Dose Tracking:*  
   Simple log to track *taken vs missed doses*.

4. *User Dashboard:*  
   View *upcoming* and *past reminders* in a clean dashboard.

5. *CRUD Functionality:*  
   Edit or delete medication schedules easily.

6. *Data Visualization Dashboard:*  
   Graphs showing *adherence rates, **missed doses, and **trends over time*.

---

###  Advanced Features
1. *AI-Powered Adherence Prediction:*  
   - Detects user patterns (e.g., missing night doses).  
   - Sends *extra reminders* before high-risk times.  
   - Offers *proactive nudges*, e.g.,  
     > “You usually forget your pill after dinner — should I remind you again in 15 minutes?”

2. *AI Chatbot Health Assistant:*  
   - Users can ask natural language questions such as:  
     - “What pills do I need to take today?”  
     - “Did I miss any dose yesterday?”

3. *Google Calendar Integration (Showstopper Feature):*  
   - Medication schedules *sync directly* with Google Calendar.  
   - AI assistant can *auto-update* calendar events if a dose is missed or rescheduled.

---

##  Tech Stack

| Category | Technologies |
|-----------|---------------|
| *Frontend* | React.js, Tailwind CSS, Chart.js |
| *Backend* | Node.js, Express.js |
| *Database* | MongoDB |
| *Notifications* | Firebase Cloud Messaging (FCM) | nodecron |
| *Integration* | Google Calendar API |
| *Authentication* | JWT-based Auth |
|  *AI / LLM*   | OpenAI api |
---

##  Installation

### Prerequisites
- Node.js (v18+)
- npm or yarn
- MongoDB running locally or via Atlas
- Firebase project setup for notifications
- OpenAI token generation for chatbot

### Steps
```bash
# Clone the repository
https://github.com/RitvikRai-001/OPS_48.git

# Move into project directory
cd OPS_48

#There are 4 major components:
1.BACKEND

# Move into backend folder
cd backend

# Install dependencies
npm install

# Create a .env file and add:
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_secret_key
FIREBASE_API_KEY=your_firebase_key
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
OPENAI_API_TOKEN="your token"
NEXT_PUBLIC_FIREBASE_PROJECT_ID=project id
FIREBASE_CLIENT_EMAIL=your client email
FIREBASE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\nyour private key-----\n",
GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\your\service-account-file.json"


# Start the development server
npm run dev

 2.FRONTEND
# Move into frontend folder
cd frontend
# Install dependencies
npm install

# Create a .env file and add:
VITE_FIREBASE_VAPID_KEY=your_vite_key

# Start the frontend
npm run dev

3.AGENT
# Move into agent folder
cd agent

#install requirements
pip install -r requirements.txt

#create a .env and add
BACKEND_URL=http://localhost:8000
OPENAI_API_KEY=your_openai_api_key

#start the agent
mov out to OPS_48 folder and run the agent using these 2 commands
cd ..
uvicorn agent.main:app --host 0.0.0.0 --port 8002 --reload

4.LLM_SERVICE
# Move into llm service folder
cd llm-services

#install requirements
pip install -r requirement.txt

#create a .env and add
GOOGLE_API_KEY=your_google_api_key

#start the agent
uvicorn main:app --host 0.0.0.0 --port 8001 --reload

```

###FOLDER STRUCTURE
```bash
OPS_48/
│
├── agent/                      # Python-based AI agent system
│   ├── guardrails/             # Safety & validation rules for LLM
│   ├── prompts/                # Prompt templates for agent
│   ├── tools/                  # Tool-calling logic
│   ├── utils/                  # Helper utilities
│   ├── __init__.py
│   ├── agent_executer.py       # Core agent execution logic
│   ├── main.py                 # Entry point for agent
│   └── requirements.txt        # Python dependencies
│
├── backend/                    # Node.js + Express API
│   ├── .vercel/                # Deployment config
│   ├── public/                 # Static assets
│   ├── src/
│   │   ├── controllers/        # Route controllers
│   │   ├── db/                 # Database connection logic
│   │   ├── firebase/           # Firebase notification logic
│   │   ├── middleware/         # Auth & error middleware
│   │   ├── ml/                 # ML prediction integration
│   │   ├── model/              # Mongoose schemas
│   │   ├── routes/             # API routes
│   │   ├── utils/              # Utility helpers
│   │   ├── app.js              # Express app config
│   │   ├── constant.js         # Constants
│   │   └── index.js            # Server entry
│   ├── package.json
│   └── package-lock.json
│
├── frontend/                   # React (Vite) frontend
│   ├── src/
│   │   ├── Firebase/           # Firebase config (client side)
│   │   ├── assets/             # Images & static assets
│   │   ├── components/         # Reusable UI components
│   │   ├── context/            # Global state management
│   │   ├── pages/              # App pages (Dashboard, Login, etc.)
│   │   ├── utils/              # Frontend helpers
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── api.js              # API configuration
│   │   ├── index.css
│   │   └── main.jsx            # React entry point
│   ├── index.html
│   ├── vite.config.js
│   ├── package.json
│   ├── package-lock.json
│   ├── eslint.config.js
│   └── README.md
│
├── llm-services/               # FastAPI microservice for AI/LLM
│   ├── __pycache__/
│   ├── .env
│   ├── .gitignore
│   ├── main.py                 # FastAPI server
│   ├── test.py
│   ├── requirement.txt         # Python dependencies
│   └── package-lock.json
│
├── .gitignore
└── README.md
```
---

## 🚀 **Future Roadmap**

### **Phase 2: Advanced Features**
- 🔊 Voice-activated medication reminders
- 📱 Mobile app with offline capabilities
- 🏥 Hospital EHR system integration  
- 🌐 Multi-language support and localization

### **Phase 3: Enterprise Features**
- 🏢 Healthcare institution admin dashboards
- 📊 Population health analytics
- 💊 Pharmacy integration and prescription sync
- 🔬 Clinical trial participation matching

### **Phase 4: Global Scale**
- ☁️ Multi-cloud deployment strategy
- 🌍 International regulatory compliance
- 🤝 Third-party healthcare app integrations
- 🧬 Personalized medicine recommendations

---
