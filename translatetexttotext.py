from googletrans import Translator, LANGUAGES

translator = Translator()

# Extract language codes and names from LANGUAGES dictionary
language_codes = list(LANGUAGES.keys())
language_names = [lang.lower() for lang in LANGUAGES.values()]

def display_language_options():
    print('Unknown Language. Wisely choose from this')
    print(f"Language Codes: {language_codes}\n")
    print(f'Or from Language Names:\n{language_names}')

# Main translation function
def translate_text():
    translating_from = input("Enter the language you want to translate from: ").strip().lower()
    word = input('Enter the word or phrase: ').strip().lower()
    translating_to = input("Enter the language you want to translate to: ").strip().lower()

    try:
        if translating_from in language_codes or translating_from in language_names:
            if translating_to in language_codes or translating_to in language_names:
                translation = translator.translate(word, src=translating_from, dest=translating_to).text
                print(f"Translated text: {translation.capitalize()}")
            else:
                display_language_options()
        else:
            display_language_options()
    except Exception as e:
        print(f"Translation failed. Error: {e}")
        display_language_options()

# Run the translation function
if __name__ == "__main__":
    translate_text()
