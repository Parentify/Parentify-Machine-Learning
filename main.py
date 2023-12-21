from fastapi import FastAPI, File, Form, UploadFile
from PIL import Image
from io import BytesIO
from ml_model.prediction import predict


app = FastAPI()

def load_image(data):
    return Image.open(BytesIO(data))

@app.get("/")
def hello():
    return {"Hello":"World"}

@app.post("/predict/")
def create_file(file: UploadFile):
    image = load_image(file.file.read())
    prediction_label, confidence_level = predict(image)
    return {"prediction":prediction_label, "confidence":str(confidence_level)}
