
from tkinter import *
from googletrans import Translator
import General

###
default_language = 'English'
translator = Translator()
language_codes = General.get_language_codes()
languages_pool = General.get_languages()
###
add_lan_row = 3
new_language = ''
languages = { 'English','French','German','Spanish','Italian',
            'Latin','Greek','Dutch','Danish','Russian','Swedish'}
personal_languages = []
popups = []
###

def get_entry():
    #print(input_text.get())
    return input_text.get()

def get_personal_languages():
    if not (new_language in personal_languages):
        personal_languages.append(new_language)
        languages.remove(new_language)
    print(personal_languages)

def change_dropdown_source(*args):
    #print(tkvar_source.get())
    return

def change_dropdown_lan1(*args):
    #print(tkvar_lan1.get())
    global new_language
    new_language = tkvar_lan1.get()

def add_language_displayed():
    global add_lan_row, personal_languages, new_language
    if not (new_language in personal_languages):
        personal_languages.append(new_language)
        languages.remove(new_language)
    tkvar_newlan = StringVar(master)
    tkvar_newlan.set('select language')
    popupMenu = OptionMenu(mf, tkvar_newlan, *languages)
    popupMenu.grid(row=add_lan_row, column=0)
    popups.append(popupMenu)
    def change_dropdown_newlan(*args):
        #print(tkvar_newlan.get())
        global new_language
        new_language = tkvar_newlan.get()
    tkvar_newlan.trace('w', change_dropdown_newlan)
    Label(mf).grid(row=add_lan_row, column=1)
    add_lan_row+=1
    print(personal_languages)
    Button(mf, text='add language', command=add_language_displayed). \
        grid(row=add_lan_row, column=0)

def get_input_text():
    #print(input_text.get())
    return input_text.get()

def format_GUI():
    for popup in popups:
        popup.configure(state="disabled")
    return

def translate():
    get_personal_languages()
    get_input_text()
    format_GUI()
    translations = translate_text()
    display(translations)

def display(translations):
    for i in range(len(translations)):
        row_index = i + 2
        Label(mf, text = translations[i],).grid(row=row_index, column=1 )

def google_translate(text):
    translations = []
    translation_result = translator.detect(text)
    src_lang_code = translation_result.lang
    src_lang_confidence = translation_result.confidence    #ignore the confidence for now

    src_language = languages_pool[language_codes.index(src_lang_code)]

    #print( src_language + ": " + text)
    for dest_language in personal_languages:
        translation = translator.translate(text, dest=dest_language)
        print(dest_language + ": " + translation.text)
        translations.append(translation.text)
    return translations

def translate_text():
    return google_translate(get_input_text())

###

master = Tk()
master.title('LinguaEZ')
mf = Frame(master)
mf.grid(column=0,row=0)
input_text = StringVar(master)
tkvar_source = StringVar(master)
tkvar_source.set(default_language)
tkvar_source.trace('w', change_dropdown_source)
popupMenu = OptionMenu(mf, tkvar_source, *languages)
popupMenu.grid(row = 0, column =0)
text_entry = Entry(mf, textvariable=input_text).grid(row = 0, column = 1)
languages.remove(default_language)

Label(mf, text="translated into").grid(row = 1, column=0);
Button(mf, text="transalte", command = translate).grid(row = 1, column = 1)

tkvar_lan1 = StringVar(master)
tkvar_lan1.set('select language')
tkvar_lan1.trace('w', change_dropdown_lan1)
popupMenu = OptionMenu(mf, tkvar_lan1, *languages)
popupMenu.grid(row=2, column=0)
popups.append(popupMenu)




Button(mf, text='add language', command=add_language_displayed).\
    grid(row=3,column=0)


mainloop()

