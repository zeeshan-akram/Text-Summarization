
import gradio as gr
from home import welcome
from summarize import summarize_interface
demo = gr.TabbedInterface([welcome(), summarize_interface], ["Home", "Summarize Article"])

demo.launch()