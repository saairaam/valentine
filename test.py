import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices');
print(voices[1].id)
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate', 150)

for voice in voices:
  print("ID: %s" % voice.id)
  print("Name: %s" % voice.name)
  print("Age: %s" % voice.age)
  print("Gender: %s" % voice.gender)
  print("Languages Known: %s" % voice.languages)