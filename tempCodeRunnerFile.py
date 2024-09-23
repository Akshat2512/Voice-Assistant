
    r = sr.Recognizer()
    with sr.AudioFile(file) as source:
       
        r.adjust_for_ambient_noise(source,duration=1)