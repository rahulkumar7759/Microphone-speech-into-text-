# import library
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()
# myself Rahul kumar
with sr.Microphone() as source:
    print("Say something")
    audio_text = r.listen(source)
    print("Time over, Thank you")
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

    try:
        # using google speech recognition
        print("Text generation : " + r.recognize_google(audio_text))
    except:
        print("Sorry, I did not get that")
        
