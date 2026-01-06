from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

from app.database import engine
from app.models import Base
from app.routes import auth, users, pages

# Создаем таблицы
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Auth Project")

# Подключаем статические файлы
os.makedirs("app/static", exist_ok=True)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Подключаем роутеры
app.include_router(pages.router)
app.include_router(auth.router)
app.include_router(users.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)