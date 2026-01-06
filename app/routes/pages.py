from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.auth import verify_token
from app.templates import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    
    if not token or not token.startswith("Bearer "):
        return RedirectResponse(url="/login")
    
    token = token[7:]  # Убираем "Bearer "
    username = verify_token(token)
    
    if not username:
        return RedirectResponse(url="/login")
    
    user = db.query(User).filter(User.username == username).first()
    
    if not user:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "dashboard.html", 
        {"request": request, "user": user}
    )