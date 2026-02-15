import os
import logging
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

SERVER_PORT = int(os.getenv("SERVER_PORT", 8000))
LOG_FILE = os.getenv("LOG_FILE", "/app/logs/app.log")

print(LOG_FILE)

if not os.path.exists(os.path.dirname(LOG_FILE)):
    os.makedirs(os.path.dirname(LOG_FILE))

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    logging.info('Root endpoint accessed')
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    logging.info(f'Server started on port {SERVER_PORT}')
    uvicorn.run(app, host="0.0.0.0", port=SERVER_PORT)

