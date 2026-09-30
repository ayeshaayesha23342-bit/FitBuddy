from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="FitBuddy - AI Fitness Plan Generator")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>FitBuddy</title>
        <style>
            body { font-family: Arial; text-align: center; padding: 80px; }
            h1 { font-size: 42px; }
            p { font-size: 20px; }
        </style>
    </head>
    <body>
        <h1>FitBuddy</h1>
        <p>AI Fitness Plan Generator using Gemini Models</p>
        <p>Generate personalized workout plans and nutrition tips.</p>
    </body>
    </html>
    """

@app.get("/health")
def health():
    return {"status": "healthy", "project": "FitBuddy"}
