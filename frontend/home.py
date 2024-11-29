import gradio as gr

def welcome():
    home_content = """
    # Welcome to the News Article Summarizer 🚀
    
    This is a **transformer-based model** that automatically summarizes news articles. It's built using cutting-edge natural language processing (NLP) techniques and is designed to handle news articles across various topics in English language.

    ## Key Features
    - **Transformer-based model**: Powered by state-of-the-art transformer model **Google T5**.
    - **Real-time Summarization**: Summarizes articles in near real-time.
    - **High Accuracy**: Generates concise, accurate, and coherent summaries.

    ## Designed and Developed By:
    - **Lead Developer**: Zeeshan Akram
    - **Technology**: Python, Hugging Face Transformers, PyTorch, Gradio
    
    ## How It Works:
    1. **Input**: You provide the article text (paste).
    2. **Processing**: The transformer model processes the input article to understand its content.
    3. **Output**: A concise summary of the article is generated based on the key points.

    ## Try It Out:
    - Paste a news article in the "Summarize Article" tab to see the model in action.

    ## Links & Social Media:
    - **GitHub Repository**: [Visit GitHub Repository](https://github.com/zeeshan-akram/Text-Summarization)
    - **LinkedIn**: [Connect with me on LinkedIn](https://www.linkedin.com/feed/)
    """    
    return gr.Markdown(home_content)
