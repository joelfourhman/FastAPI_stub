from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount the "static" directory as "/static"
app.mount("/", StaticFiles(directory="static"), name="static")

# Serve index.html at the root path
@app.get("/")
async def index():
    return app.dependency_overrides.get(
        StaticFiles
    ).send_index_html("index.html")
