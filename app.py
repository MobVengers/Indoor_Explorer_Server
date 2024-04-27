from fastapi import FastAPI
# import uvicorn
from controllers.calculateLocation import router as calculateLocation_router
from controllers.addFingerPrint import router as addFingerPrint_router
from controllers.healthCheck import router as healthCheck_router
from controllers.findPath import router as findPath_router
from db_connect import *
from dotenv import load_dotenv
# import os

load_dotenv()

app = FastAPI()

initialize_db()

app.include_router(calculateLocation_router, prefix="/mylocation", tags=["my-location"])
app.include_router(addFingerPrint_router, prefix="/fingerprint", tags=["finger-print"])
app.include_router(healthCheck_router, prefix="/health", tags=["health-check"])
app.include_router(findPath_router, prefix="/path", tags=["path"])

# host = os.getenv("HOST")
# port = os.getenv("PORT")

# if __name__ == "__main__":
#     uvicorn.run("app:app", host=host, port=port, reload=True)