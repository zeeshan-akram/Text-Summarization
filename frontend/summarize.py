import gradio as gr

def get_summarization(Article):
    #TODO connect to backend
    return Article

summarize_interface = gr.Interface(
    fn=get_summarization,
    inputs=["text"],
    outputs=["text"],
    allow_flagging="never"
)