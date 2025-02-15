import gradio as gr
from google import genai

import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def echo(message, history):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=message,
    )

    return response.text


iface = gr.ChatInterface(
    fn=echo,
    textbox=gr.Textbox(placeholder="Type your message here..."),
    title="My Echo Bot"
)

iface.launch()
