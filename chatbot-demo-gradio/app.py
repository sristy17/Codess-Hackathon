import gradio as gr
from openai import OpenAI
import os

# Initialize the OpenAI client with your API key
client = OpenAI(
    base_url="https://zukijourney.xyzbot.net/v1",
    api_key= os.getenv("ZUKI_API_KEY"),
)

def generate_advice(situation):
    # Construct the prompt for the AI model
    prompt = f"""
    You are an expert in personal safety, especially for women. A user has described a situation: '{situation}'.
    Provide detailed, practical advice on what they should do to stay safe.
    """

    # Send the prompt to the AI model to generate a response
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI expert in personal safety advice for women."},
            {"role": "user", "content": prompt},
        ],
    )

    # Return the generated advice
    return completion.choices[0].message.content

def respond(
    message,
    history: list[tuple[str, str]],
    system_message,
    max_tokens,
    temperature,
    top_p,
):
    # Add system message
    messages = [{"role": "system", "content": system_message}]

    # Add conversation history
    for val in history:
        if val[0]:
            messages.append({"role": "user", "content": val[0]})
        if val[1]:
            messages.append({"role": "assistant", "content": val[1]})

    # Add current user message
    messages.append({"role": "user", "content": message})

    # Generate response
    response = generate_advice(message)

    # Yield response as chunks if using streaming (for large responses)
    yield response

# Set up Gradio interface
demo = gr.ChatInterface(
    respond,
    additional_inputs=[
        gr.Textbox(value="You are an expert in personal safety, especially for women.", label="System message"),
        gr.Slider(minimum=1, maximum=2048, value=512, step=1, label="Max new tokens"),
        gr.Slider(minimum=0.1, maximum=4.0, value=0.7, step=0.1, label="Temperature"),
        gr.Slider(
            minimum=0.1,
            maximum=1.0,
            value=0.95,
            step=0.05,
            label="Top-p (nucleus sampling)",
        ),
    ],
)

# Launch the Gradio interface
if __name__ == "__main__":
    demo.launch()
