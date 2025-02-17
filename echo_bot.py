import gradio as gr
from google import genai
from google.genai import types

import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def echo(message, history):
    response = client.models.generate_content(
        model="tunedModels/sarcastic-g1851wnu1i60",
        # model="gemini-2.0-flash-001",
        contents=message,
    )

    if response.text is None:
        print(response.candidates[0].finish_reason)
        if response.candidates[0].finish_reason is types.FinishReason.SAFETY:
            print("It's a safety issue")
            return "Safety violation. Please ask something else"

    return response.text


iface = gr.ChatInterface(
    fn=echo,
    textbox=gr.Textbox(placeholder="Type your message here..."),
    title="Marvin the Paranoid Android",
    type="messages"
)

iface.launch()

# echo("what color are oranges?", None)

