from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for all origins, methods, and headers
origins = [
  " https://russopy.github.io/twilohtml/",
  "https://statuesque-gaufre-01d230.netlify.app/",
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


    