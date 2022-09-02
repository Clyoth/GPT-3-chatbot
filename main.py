import openai
import pyttsx3
import speech_recognition as sr


openai.api_key = "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"

engine = pyttsx3.init()


conversation = ""
user_name = "James"

while True:

    try:
        user_input = input('User Input:')
    except:
        continue

    prompt = user_name + ": " + user_input + "\n Jarvis:"

    conversation += prompt

    response = openai.Completion.create(engine='text-davinci-002', prompt=conversation, max_tokens=100)
    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split(user_name + ": ", 1)[0].split("Ava: ", 1)[0]


    conversation += response_str + "\n"
    print(response_str)

    engine.say(response_str)
    engine.runAndWait()