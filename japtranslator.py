from translate import Translator

translator = Translator(to_lang="es")


with open("practice.txt", mode='r+')as my_file:
    translate_espanol = (translator.translate(my_file.read()))
    with open('./translatetest.txt', mode='w') as my_file2:
        my_file2.write(translate_espanol)
# print(translate_espanol)
