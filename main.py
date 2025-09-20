from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import langchain_helper as lch
from utils import countries, name_types

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")



@app.get("/", response_class=HTMLResponse)
async def root(request: Request,gender:str="", country: str = "", name_type: str = ""):
    baby_name = ""
    if gender and country and name_type:
        response = lch.generate_baby_name(gender,country, name_type)
        baby_name = response['baby_name']

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "countries": countries,
            "name_types":name_types,
            "gender":gender,
            "country": country,
            "name_type": name_type,
            "baby_name": baby_name,
        }
    )