import requests
import re


class Translator():

    def Actions(self):
        word = input('Введите слово: ')
        language = input(
            'На какой язык переводить? (Пример ввода - "английский")Если пропустить ,будет выбран русский: ')
        if len(language) == 0:
            language = 'русском'
        pattern = r'type="hidden"><input name="q" value="\w+" type="hidden">' \
                  r'<input value="(.+)" disabled="disabled" name="tlitett"'

        res = re.findall(pattern, str(requests.get(
            f'https://www.google.com/search?client=opera&q={word}+на+{language}&sourceid=opera&ie=UTF-8&oe=UTF-8').text))
        if len(res) == 0:
            return 'ERROR'
        else:
            return word + ' - ' + str(*res)

    def WhriteIn(self, res):
        file = open(r'/home/eugenii/my apps/tran/data/words.txt', mode='a', encoding='utf-8')
        file.write(f'{res}' + '\n')
        file.close()
