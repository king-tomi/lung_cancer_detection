# Lung Cancer Detection Application

## Overview
This repository contains the code for a Lung Cancer Detection application that uses a deep learning model to classify lung scans. The application is built with Keras and FastAPI for efficient image processing and prediction.

## Project Description
The application detects lung cancer from medical scans by classifying them into different stages. Users can upload lung scans through a FastAPI endpoint, and the application processes these images to return predictions. This tool aids in early diagnosis and treatment planning for lung cancer patients.

## Features
- Deep learning model for lung cancer detection
- FastAPI service for image upload and prediction
- Accurate classification of lung scans

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/king-tomi/lung-cancer-detection-app.git
   cd lung-cancer-detection-app

2. Install the required dependencies:
  ```bash
  pip install -r requirements.txt
```

3. Run the FastAPI server:
    ```
    uvicorn app:app --reload

## Usage

- Upload a lung scan through the /upload/ endpoint.
- The image will be processed and classified into one of the lung cancer stages.
- The prediction result will be returned as a JSON response.

## Model Details
- Architecture: Convolutional Neural Network (CNN)
- Framework: Keras
- Dataset: Custom dataset for lung cancer detection
