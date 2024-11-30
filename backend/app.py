from fastapi import FastAPI
from pydantic import BaseModel
import requests
from services.auth import validated_user
from services.summarizer import summarize_article
import uvicorn


app = FastAPI(redoc_url=False)

class SummarizeRequest(BaseModel):
    article: str
    username: str
    password: str


@app.post("/summarize_article")
def summarizer(request: SummarizeRequest):
      
      if validated_user(request.username, request.password):
            summary = summarize_article(request.article)
            return {"summary": summary, "success": True}
      return {"message": "Invalid Credentials!", "success": False}

if __name__=="__main__":
      uvicorn.run(app=app, host="0.0.0.0", port=8088)