from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from ollama_client import ask_ollama

app = FastAPI()

# Permette richieste dal frontend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "CyberIntel Copilot backend is running"}

@app.post("/upload")
async def upload_report(file: UploadFile = File(...)):
    content = await file.read()
    return {"filename": file.filename, "content_snippet": content[:200].decode(errors="ignore")}

@app.post("/ask")
def ask_model(prompt: str):
    response = ask_ollama(prompt)
    return {"response": response}
