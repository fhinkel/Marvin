import gradio as gr

def echo(message, history):
    return message  # Just return the user's message

iface = gr.ChatInterface(
    fn=echo,
    textbox=gr.Textbox(placeholder="Type your message here..."),
    title="My Echo Bot"
)

iface.launch()