from fastapi import FastAPI
from routers import blog_get 
from routers import blog_post
from routers import user
from routers import article
from db import models
from db.database import engine
from exceptions import StoryException
from fastapi import Request
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from auth import authentication

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(authentication.router)  
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/host')
def index():
    return {'message': 'Hello world!'}

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={"message": str(exc)}
    )

models.Base.metadata.create_all(engine)