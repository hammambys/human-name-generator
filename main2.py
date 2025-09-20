from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import langchain_helper as lch

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

animal_types = ["Dog", "Cat", "Hamster", "Rat", "Snake", "Lizard", "Cow"]

@app.get("/", response_class=HTMLResponse)
async def root(request: Request, animal_type: str = "", pet_color: str = ""):
    pet_name = ""
    if animal_type and pet_color:
        response = lch.generate_pet_name(animal_type, pet_color)
        pet_name = response['pet_name']

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "animal_types": animal_types,
            "animal_type": animal_type,
            "pet_color": pet_color,
            "pet_name": pet_name,
        }
    )