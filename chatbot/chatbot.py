from openai import OpenAI

# Initialize the OpenAI client with your API key
client = OpenAI(
    base_url="https://zukijourney.xyzbot.net/v1",
    api_key="api_key",
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

def main():
    print("Welcome to the Personal Safety Advisor!")
    print("Type 'exit' to close the application.")
    
    while True:
        # Get user input
        situation = input('Describe your situation: ')
        
        # Check if the user wants to exit
        if situation.lower() == 'exit':
            print("Exiting the application. Stay safe!")
            break
        
        # Generate and print the safety advice
        response = generate_advice(situation)
        print(response)

# Run the application
if __name__ == "__main__":
    main()


