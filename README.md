# FastAPI Auth Project - Исправленная версия

Проект аутентификации пользователя на FastAPI с использованием JWT токенов.

## 🚀 Быстрый старт

### Вариант 1: Простая установка

1. Установите зависимости:
```bash
pip install fastapi uvicorn sqlalchemy python-jose[cryptography] passlib[bcrypt] python-multipart jinja2 python-dotenv
```

2. Запустите приложение:
```bash
uvicorn app.main:app --reload
````