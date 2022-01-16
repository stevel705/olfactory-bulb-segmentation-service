import io

from binary_segmentation.predict import predict
from starlette.responses import Response

from fastapi import FastAPI, File

app = FastAPI(
    title="Olfactory bulb segmentation",
    description="""Obtain semantic segmentation mask of the image in input via U-Net implemented in PyTorch.""",
    version="0.0.1",
)


@app.post("/segmentation")
def get_segmentation_mask(file: bytes = File(...)):
    """Get segmentation mask from image file"""
    segmented_image = predict(file)
    bytes_io = io.BytesIO()
    segmented_image.save(bytes_io, format="PNG")
    return Response(bytes_io.getvalue(), media_type="image/png")