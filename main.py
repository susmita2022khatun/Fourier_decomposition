from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
import os
import numpy as np
from process import read_wav_file, discrete_fourier, fft, fftfreq

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    
    signal, sample_rate = read_wav_file(file_location)
    signal_fft = fft(signal)
    amplitude_spectrum = np.abs(signal_fft)
    amplitude_spectrum = amplitude_spectrum / np.max(amplitude_spectrum)
    freqs = fftfreq(len(signal), sample_rate)
    
    threshold = 0.2
    dominant_freq_indices = np.where(amplitude_spectrum[:len(signal) // 2] >= threshold)[0]
    dominant_freqs = freqs[dominant_freq_indices]

    return {"filename": file.filename, "dominant_frequencies": dominant_freqs.tolist()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
