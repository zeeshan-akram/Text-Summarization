# Text Summarization Application

This repository contains a text summarization application that utilizes a FastAPI backend and a Gradio-based frontend for summarizing articles. Users can input an article, their username, and password to get a summarized version of the article.

## Features
- **FastAPI Backend**: A RESTful API for handling summarization requests.
- **Hugging Face Transformers**: The backend uses the Hugging Face Transformers library with the Google T5-small model for text summarization.
- **Gradio Frontend**: A user-friendly interface for interacting with the summarization service.
- **Secure Input**: Password input field in the Gradio app masks user passwords.

## Directory Structure
```
backend/
    app.py                 # Entry point for the FastAPI backend
    services/
        auth.py            # Handles authentication logic
        summarizer.py      # Implements text summarization using Hugging Face T5-small
    config.py              # Configuration settings for the backend
frontend/
    main.py                # Entry point for the Gradio frontend
    summarizer.py          # Logic for interfacing with the backend API
    home.py                # Frontend routing and UI components
notebooks/
    inference_notebook.ipynb  # Jupyter notebook for inference examples
    training_notebook.ipynb   # Jupyter notebook for training the summarization model
environment.yaml            # Conda environment definition file
```

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/zeeshan-akram/Text-Summarization.git
cd Text-Summarization
```

### 2. Create a Conda Environment
Create a Conda environment using the `environment.yaml` file included in the repository:
```bash
conda env create -f environment.yaml
conda activate nlp
```

## Running the Application

### 1. Start the FastAPI Backend
The FastAPI backend handles summarization requests. It uses the Hugging Face Transformers library and the Google T5-small model for summarization. To start the server, navigate to the `backend` directory and run:
```bash
python app.py
or
uvicorn app:app --host 0.0.0.0 --port 8088
```
- Replace `app:app` with the path to your FastAPI app if necessary.
- The backend will be accessible at `http://0.0.0.0:8088`.

### 2. Run the Gradio Frontend
Navigate to the `frontend` directory and start the Gradio frontend by running:
```bash
python main.py
```
This launches the Gradio interface in your web browser. You can interact with the application to summarize text articles.

## Application Workflow
1. Input your article, username, and password into the Gradio app.
2. The frontend sends the data to the FastAPI backend via a POST request.
3. The backend uses the Hugging Face Transformers library with the Google T5-small model to generate a summary of the article.
4. The Gradio app displays the summary.

## Example
1. Start the backend:
   ```bash
   python app.py
   or
   uvicorn app:app --host 0.0.0.0 --port 8088
   ```
2. Start the Gradio app:
   ```bash
   python main.py
   ```
3. Open the Gradio interface and enter your details:
   - **Article**: Paste the article text.
   - **Username**: Your username.
   - **Password**: Your password (masked).
4. Click "Submit" to get the summary.

## Contributing
Feel free to submit issues or pull requests to improve this project. Contributions are always welcome!