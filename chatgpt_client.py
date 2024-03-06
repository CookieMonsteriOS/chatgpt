import openai

# Set up your OpenAI API key
openai.api_key = 'your-api-key-here'

def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting...")
            break
        prompt = f"User: {user_input}\nChatGPT:"
        response = generate_response(prompt)
        print("ChatGPT:", response)

if __name__ == "__main__":
    main()
