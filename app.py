from fastapi import FastAPI
from controllers.calculateLocation import router as calculateLocation_router
from controllers.addFingerPrint import router as addFingerPrint_router
from controllers.findPath import router as findPath_router
from controllers.authenticateAdmin import router as auth_router
from db_connect import *
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("HOST")
port = os.getenv("PORT")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASSWORD")

app = FastAPI()

initialize_db(db_user, db_pass)

app.include_router(calculateLocation_router, prefix="/mylocation", tags=["my-location"])
app.include_router(addFingerPrint_router, prefix="/fingerprint", tags=["finger-print"])
app.include_router(findPath_router, prefix="/path", tags=["path"])
app.include_router(auth_router, prefix="/auth", tags=["authenticate admin"])



@app.get("/")
def read_root():
    return {"message": "active"}

# if __name__ == "__main__":
#     uvicorn.run("app:app", host=host, port=port, reload=True)