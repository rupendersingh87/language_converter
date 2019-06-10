from translate import Translator
Englishtext= "hello my name is innaya how can i help you?"

translator_hindi = Translator(from_lang="English", to_lang="hindi")
translator_spanish = Translator(from_lang="English", to_lang="spanish")
translator_french = Translator(from_lang="English", to_lang="french")
translator_chinese = Translator(from_lang="English", to_lang="chinese")
translator_Arabic = Translator(from_lang="English", to_lang="Arabic")
translator_Russian = Translator(from_lang="English", to_lang="Russian")

translation_hindi = translator_hindi.translate(Englishtext)
translation_spanish = translator_spanish.translate(Englishtext)
translation_french = translator_french.translate(Englishtext)
translation_chinese = translator_chinese.translate(Englishtext)
translation_arabic = translator_Arabic.translate(Englishtext)
translation_russian = translator_Russian.translate(Englishtext)



print(translation_hindi)
print(translation_spanish)
print(translation_french)
print(translation_chinese)
print(translation_arabic)
print(translation_russian)

