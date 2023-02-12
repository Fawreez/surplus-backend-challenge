import uvicorn
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from wrapper.product import *
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

class UpdateProduct(BaseModel):
    product_id: int
    name: str
    description: str
    enable: bool

class CreateProduct(BaseModel):
    name: str
    description: str
    enable: bool
    category: str

class CreateImage(BaseModel):
    name: str
    image_file: str
    enable: bool


@app.post("/create_product")
async def create_product(product_data: CreateProduct):
    response = add_product(product_data.dict())
    
    return JSONResponse(response)


@app.get("/read_product")
async def read_product(product_id: int):
    response = get_product(product_id)

    return JSONResponse(response)


@app.post("/update_product")
async def update_product(product_data: UpdateProduct):
    response = modify_product(product_data.dict())

    return JSONResponse(response)


@app.delete("/delete_product")
async def delete_product(product_id: int):
    response = remove_product(product_id)

    return JSONResponse(response)


@app.post("/create_image")
async def create_image(image_data: CreateImage):
    response = add_image_to_db(image_data.dict())

    return JSONResponse(response)





@app.get("/")
async def main():
    content = """
            Hello World!
            """
    return HTMLResponse(content=content)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
