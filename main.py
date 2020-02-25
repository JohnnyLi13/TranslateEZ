
import General

from googletrans import Translator
translator = Translator()
languages_dict = General.get_language_dict()
personal_languages = ['english','french','german', 'spanish']   #detect inputs


language_codes = General.get_language_codes()
languages = General.get_languages()


#text = "Nice to meet you"   #detect input

def google_translate(text):
    translation_result = translator.detect(text)
    src_lang_code = translation_result.lang
    src_lang_confidence = translation_result.confidence    #ignore the confidence for now

    src_language = languages[language_codes.index(src_lang_code)]

    personal_languages.remove(src_language)

    print( src_language + ": " + text + " (" + "confidence=" + str(src_lang_confidence) + ")" )
    for dest_language in personal_languages:
        translation = translator.translate(text, dest=dest_language)
        print(dest_language + ": " + translation.text)


