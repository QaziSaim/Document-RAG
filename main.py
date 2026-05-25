from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from backend import ask_question

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            
            "response": ""
        }
    )


@app.post("/", response_class=HTMLResponse)
async def get_answer(request: Request, query: str = Form(...)):

    answer = ask_question(query)

    return templates.TemplateResponse(
        request,
        "index.html",
        {
           
            "response": answer,
            "query": query
        }
    )