import speech_recognition as sr
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load pre-trained model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Function to generate a response
def generate_response(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=50)
    return tokenizer.decode(output[0], skip_special_tokens=True)

while True:
    prompt = input("Admin: ")
    if prompt == "vox tts":
        # Listening the speech and store in audio_text variable
        with sr.Microphone() as source:
            print("Talk")
            audio = r.listen(source)
            try:
                # using google speech recognition
                audio_text = r.recognize_google(audio)
                print("You: ", audio_text)
                response = generate_response(audio_text)
                print("Vox: " , response)
            except:
                print("Sorry, I did not get that")
    elif prompt == "vox die":
        break
    else:
        response = generate_response(prompt)
        print("Vox: " , response)
