from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import json
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
import qr
from fastapi.staticfiles import StaticFiles
from typing import Optional



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

IP_URL = "http://172.16.210.94:8000"

templates = Jinja2Templates(directory="templates")

USER_DB_FILE = "db_user.json"
ORG_DB_FILE = "db_org.json"


def read_user_db():
    try:
        with open(USER_DB_FILE, "r") as f:
            return json.load(f)
    except:
        return []


def write_user_db(data):
    with open(USER_DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def read_org_db():
    try:
        with open(ORG_DB_FILE, "r") as f:
            return json.load(f)
    except:
        return []


def write_org_db(data):
    with open(ORG_DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.get("/")
def status():
    return "Status OK"

@app.get("/{org_name}/form", response_class=HTMLResponse)
async def get_form(request: Request, org_name: str):


    db = read_org_db()

    org_exists = any(org["name"] == org_name for org in db)

    if not org_exists:
        return PlainTextResponse("Organization not found", status_code=404)

    # print("ROUTE HIT")

    return templates.TemplateResponse( name="form.html",
                                      request= request,
                                      context={"org_name": org_name}
                                      )


@app.post("/{org_name}/form", response_class=PlainTextResponse)
async def submit_form(
    org_name: str,
    name: str = Form(...),
    dob: str = Form(...),
    phone: str = Form(...),
    feedback: Optional[str] = Form(None)
    ):

    # print("ROUTE HIT")
    new_user = {
        "name": name,
        "dob": dob,
        "phone": phone,
        "organsation name": org_name,
        "feedback": feedback or "",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data = read_user_db()
    data.append(new_user)
    write_user_db(data)

    return "Saved successfully!"

@app.get("/admin")
async def admin(request: Request):
    try:
        users = read_user_db()
        # print(users[0])
        # return {"test" : 'pass'}
        return templates.TemplateResponse(
            name="admin.html",
            request=request,
            context={"users":users}
        )
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/register-org")
def open_register_page(request: Request):
    return templates.TemplateResponse(
        name= "register_org.html",
        request= request
    )

    
@app.post("/register-org")
async def register(request: Request):
    print("ROUTE HIT")
    data = await request.form()

    # print(data)

    org_name = data.get('name',None)
    email = data.get('email',None)

    if not org_name or not email:
        return {"error": "Missing fields"}
    
    base_url = str(request.base_url).rstrip("/")

    filepath = qr.qr_generate(org_name, base_url)
    
    new_org = {
        "name": org_name,
        "email": email,
        "img": filepath,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data = read_org_db()
    data.append(new_org)
    write_org_db(data)

    return RedirectResponse(f"/redirect_to_qr?img={filepath}", status_code=303)

@app.get("/redirect_to_qr")
def redirectingtoqr(request: Request, img: str):
    # print("ROUTE HIT")
    # print(img)
    from fastapi import Request
    return templates.TemplateResponse(
        name="qr_page.html",
        request=request,
        context={
            "image_name": img,
            "image_url": f"{img}"
        }
    )