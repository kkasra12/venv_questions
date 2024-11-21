from googletrans import Translator
translator = Translator()
text = ("Hello, world!\n"
"I am a student in the university of luxembourg")
result = translator.translate(text, src="en", dest="fr")
print(result.text)
