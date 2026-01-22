# -----------------------------
# test_api.py (Interactive + Fake API)
# -----------------------------

# Flag to toggle between real and fake API
USE_FAKE_API = False  # Set True while quota is 0, False when quota is available

# Mock function to simulate API response
def fake_api_call(prompt):
    return {
        "choices": [{"text": f"Fake response for prompt: {prompt}"}]
    }

# Function to get response (real or fake)
def get_response(prompt):
    if USE_FAKE_API:
        response = fake_api_call(prompt)
    else:
        import openai
        openai.api_key = "YOUR_REAL_API_KEY"  # Replace with your real API key
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
    return response["choices"][0]["text"]

# -----------------------------
# Interactive prompt input
# -----------------------------
if __name__ == "__main__":
    print("Welcome to Test API Interactive Mode!")
    print("Type your prompt and press Enter. Type 'exit' to quit.\n")

    while True:
        prompt = input("Enter prompt: ")
        if prompt.lower() == "exit":
            print("Exiting. Goodbye!")
            break
        result = get_response(prompt)
        print(f"Response: {result}\n")