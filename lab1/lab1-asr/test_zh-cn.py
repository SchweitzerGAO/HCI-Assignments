import speech_recognition as sr

if __name__ == '__main__':
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print('正在倾听')
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        audio = recognizer.listen(source,phrase_time_limit=3)
    sentence = recognizer.recognize_sphinx(audio,language='zh-CN')
    print(sentence)
