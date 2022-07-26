from translate import Translator

translator = Translator(to_lang="hi")

print(dir(translator))

try:
    with open('./sample.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        with open('./output.txt', mode='w') as out_file:
            out_file.write(translation)
except FileNotFoundError as err:
    print('check your file path!')