from morse import MorseCodeTranslator

translator = MorseCodeTranslator()

# text = "This string has been translated to morse code and back again"
text = input("Please enter a text string : ")

# Translate text to morse code
morse = translator.translate_text(text)

# Translate morse code to text
translated_text = translator.translate_morse(morse)

print("Morse code of the string :", morse)
print("Text for the morse code :", translated_text)
