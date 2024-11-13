
# Fourier Decomposition Web Application

This project is a web application built with **FastAPI** that allows users to upload audio files (WAV format) and decompose them into their Fourier components. The application performs a **Fast Fourier Transform (FFT)** on the audio signal and identifies the dominant frequencies.

## Features
- **File Upload**: Allows users to upload WAV files for processing.
- **Fourier Analysis**: Computes the Fourier Transform of the audio signal and returns the dominant frequencies.
- **Visualization**: (Optional) Could be extended for plotting or visualizing the frequency spectrum.

## Technologies
- **FastAPI**: For creating the web application.
- **librosa**: For loading and reading audio files.
- **NumPy**: For performing the FFT and manipulating the signal.
- **Jinja2**: For rendering HTML templates.

## Installation

### Prerequisites
- Python 3.7+
- A virtual environment (optional but recommended)

### Steps to Set Up

1. **Clone the repository**:
   ```bash
   git clone https://github.com/susmita2022khatun/Fourier_decomposition.git
   cd Fourier_decomposition
   ```

2. **Create and activate a virtual environment** (optional):
   ```bash
   python -m venv venv
   # On Windows
   venv\Scriptsctivate
   # On Mac/Linux
   source venv/bin/activate
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure the `uploads` and `static` directories exist**:
   - `uploads/` will store the uploaded audio files.
   - `static/` will contain static files (CSS, JS, etc.).

5. **Run the application**:
   ```bash
   python main.py
   ```

   The application will start the server at `http://127.0.0.1:8000/`.

## Usage

1. **Visit the application** in a browser at `http://127.0.0.1:8000/`.
2. **Upload a WAV file** using the file input on the webpage.
3. The server will process the audio and return a JSON response containing the dominant frequencies in the audio signal.

### Example Response:
```json
{
  "filename": "example.wav",
  "dominant_frequencies": [440.0, 880.0, 1320.0]
}
```

## Code Overview

- **`main.py`**: Contains the FastAPI application logic, including routes for uploading files and processing them using the FFT.
- **`process.py`**: Contains helper functions for performing Fourier decomposition, including `discrete_fourier`, `fft`, and `fftfreq`.
- **`static/`**: Directory for static files like CSS or JavaScript (optional, could be used for front-end enhancements).
- **`templates/`**: Contains HTML templates (like `index.html`) rendered by FastAPI using Jinja2.

