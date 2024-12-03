import gradio as gr
import requests

def get_summarization(Article, username, password):
    data = {
        "article": Article, 
        "username": username, 
        "password": password
    }
    response = requests.post("http://0.0.0.0:8088/summarize_article", json=data)
    if response.status_code != 200:
        return "Server Error!"
    json_text = response.json()
    if json_text["success"]:
        return json_text["summary"]
    return json_text["message"]

summarize_interface = gr.Interface(
    fn=get_summarization,
    inputs=[
        gr.Textbox(label="Article", placeholder="Enter the article text here"),
        gr.Textbox(label="Username", placeholder="Enter your username"),
        gr.Textbox(label="Password", type="password", placeholder="Enter your password")
    ],
    outputs=["text"],
    allow_flagging="never"
)