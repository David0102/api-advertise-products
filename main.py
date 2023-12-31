from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import user_router, product_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

app.mount("/staticfiles/users", StaticFiles(directory="staticfiles/users"))
app.mount("/staticfiles/products", StaticFiles(directory="staticfiles/products"))

app.include_router(user_router.router)
app.include_router(product_router.router)