import pyttsx3
from datetime import datetime

def speak(text):
    print("AI Bot:", text)
    # Create a fresh engine instance every time so Windows doesn't lock it up
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

print("Oliver: Hello! I am Python AI assistant. Type 'exit' to end.\n")

while True:
    user_input = input("You: ").lower()

    if "exit" in user_input:
        speak("Goodbye!")
        break

    elif "hello" in user_input or "hi" in user_input:
        speak("Hello! I am Oliver. How may I assist you today?")

    elif "how are you" in user_input:
        speak("I am just code but I feel Awesome helping you")

    elif "name" in user_input:
        speak("I am Oliver, your Python AI assistant")

    elif "time" in user_input:
        current_time = datetime.now().strftime("%H : %M : %S")
        speak(current_time)

    elif "calculate" in user_input:
        try:
            result = eval(user_input.replace("calculate", ""))
            speak(f"This is result {result}")
        except:
            speak("Sorry I couldn't understand this calculation")