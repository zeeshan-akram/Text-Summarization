
import gradio as gr
from home import welcome
from interface import iface2
demo = gr.TabbedInterface([welcome(), iface2], ["Home", "image-to-text"])

demo.launch()