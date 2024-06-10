from fastapi import FastAPI

from models.database import create_db, Session
from models.models import *
from router.router import router as rig_routers




create_db()
app = FastAPI()
app.include_router(rig_routers)





