import openai

openai.api_key = "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"

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = completions.choices[0].text
    return message.strip()


while True:
    prompt = input("Admin: ")
    if prompt == "vox die":
        break
    elif prompt == "vox tts":
        # code for voice input goes here
        pass
    else:
        response = generate_response(prompt)
        print("Vox: ", response)
