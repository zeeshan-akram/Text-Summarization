import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

iface2 = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)