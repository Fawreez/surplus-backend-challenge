import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()









@app.get("/")
async def main():
    content = """
            Hello World!
            """
    return HTMLResponse(content=content)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
