from fastapi import FastAPI
from app.api import user, company

app = FastAPI()

app.include_router(user.router)
app.include_router(company.router)