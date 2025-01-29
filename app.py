from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for all origins, methods, and headers
origins = [
    "http://localhost",  # Allows front-end running locally
    "http://localhost:8000",  # Another possible URL for testing
    "*",  # Allows any domain (be careful with this in production)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Specifies allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


    