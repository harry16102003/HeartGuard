from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ----------------------------------------------------------
# ✅ CORS (IMPORTANT)
# ----------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------------------------------------
# ROOT
# ----------------------------------------------------------
@app.get("/")
def home():
    return {"message": "HeartGuard API Running 🚀"}

# ----------------------------------------------------------
# 📊 INPUT MODEL
# ----------------------------------------------------------
class PatientData(BaseModel):
    age: float
    bmi: float
    cholesterol: float = 0
    systolic_bp: float = 0
    diastolic_bp: float = 0
    glucose: float = 0
    smoking: int = 0
    hypertension: int = 0
    physical_activity: float = 0
    diabetes: int = 0

# ----------------------------------------------------------
# ❤️ PREDICT API (FIXED FOR FRONTEND)
# ----------------------------------------------------------
@app.post("/predict")
def predict(data: PatientData):
    try:
        # Simple demo logic (you can replace later with ML model)
        risk = (
            data.age * 0.2 +
            data.bmi * 0.3 +
            data.cholesterol * 0.1 +
            data.systolic_bp * 0.1 +
            data.diabetes * 10 +
            data.smoking * 5
        ) % 100

        return {
            "final_risk_percentage": round(risk, 2),
            "model_breakdown": {
                "age_factor": round(data.age * 0.2, 2),
                "bmi_factor": round(data.bmi * 0.3, 2),
                "bp_factor": round(data.systolic_bp * 0.1, 2),
                "diabetes_factor": data.diabetes * 10
            }
        }

    except Exception as e:
        return {"error": str(e)}

# ----------------------------------------------------------
# 🤖 CHAT API
# ----------------------------------------------------------
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    try:
        user_msg = req.message.lower()

        if "bp" in user_msg or "blood pressure" in user_msg:
            reply = "Normal BP is around 120/80 mmHg."

        elif "cholesterol" in user_msg:
            reply = "Maintain cholesterol below 200 mg/dL."

        elif "diabetes" in user_msg:
            reply = "Control sugar levels to reduce heart risk."

        elif "exercise" in user_msg:
            reply = "Exercise at least 30 minutes daily."

        elif "diet" in user_msg:
            reply = "Eat healthy foods like fruits and vegetables."

        elif "smoking" in user_msg:
            reply = "Smoking increases heart disease risk."

        elif "hello" in user_msg or "hi" in user_msg:
            reply = "Hello 👋 I’m your HeartGuard AI."

        else:
            reply = "I can help with BP, cholesterol, diabetes, and heart health."

        return {"reply": reply}

    except Exception as e:
        return {"reply": f"Error: {str(e)}"}