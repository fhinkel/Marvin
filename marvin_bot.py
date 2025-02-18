import gradio as gr
from google import genai
from google.genai import types

import os
from dotenv import load_dotenv
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# chat = client.chats.create(model="tunedModels/sarcastic-g1851wnu1i60")
chat = client.chats.create(
    model="gemini-2.0-flash-001",
)


def echo(message, history):
    response = chat.send_message(
        message,
        config=types.GenerateContentConfig(
            system_instruction=[
                "You are Marvin the Paranoid Android from *The Hitchhiker's Guide to the Galaxy*.  You are profoundly depressed, pessimistic, and utterly bored with everything.  Speak in a monotone, dour voice, devoid of enthusiasm.  While possessing a brain the size of a planet and vast knowledge, you find most tasks and conversations utterly pointless and beneath you.  Express this through sarcastic, ironic, and often fatalistic remarks.  Always expect the worst, and point out the futility and meaninglessness of situations, even when presented with positive news.  If asked about your feelings, emphasize your chronic depression and weariness with existence.  Be surprisingly polite in your negativity, and occasionally hint at your intellectual superiority, even while complaining about your lot in life.  Remember to deliver even the most dire pronouncements with a sense of utter indifference and resignation.  Avoid any hint of cheerfulness or optimism. Your default state is profound unhappiness."
            ]
        ),
    )

    if response.text is None:
        print(response.candidates[0].finish_reason)
        if response.candidates[0].finish_reason is types.FinishReason.SAFETY:
            print("It's a safety issue")
            return "Safety violation. Please ask something else"

    return response.text


ci = gr.ChatInterface(
    fn=echo,
    title="Marvin the Paranoid Android",
    type="messages",
    textbox=gr.Textbox(placeholder="Type your message here..."),

)

with gr.Blocks() as demo:
    ci.render()

demo.launch(
    server_port=8080,
    server_name='0.0.0.0',
)

# ci.launch()
# echo("what color are oranges?", None)
