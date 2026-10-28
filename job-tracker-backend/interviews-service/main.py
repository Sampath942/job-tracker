from fastapi import FastAPI
from internal.routes import interviews_router as interviews_router

app = FastAPI()

app.include_router(interviews_router.router)
