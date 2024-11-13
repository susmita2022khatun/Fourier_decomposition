
# Fourier Decomposition

A Python-based project for decomposing mixed sinusoidal audio signals into their Fourier components. This repository provides tools for both Discrete Fourier Transform (DFT) and Fast Fourier Transform (FFT) calculations, along with an interface for processing and visualizing waveforms.

## Features
- DFT and FFT calculations on audio signals
- Frequency bin generation for FFT
- Audio loading and processing via `librosa`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/susmita2022khatun/Fourier_decomposition.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Run the main application**:
   ```bash
   python app.py
   ```
2. **Example**:
   Load an audio file and apply the FFT:
   ```python
   from process import read_wav_file, fft
   signal, sample_rate = read_wav_file("path/to/audio.wav")
   fft_result = fft(signal)
   ```

## File Descriptions
- `process.py`: Contains functions for DFT, FFT, frequency bin calculation, and audio file reading.
- `app.py`: Main application script for running the web interface.

