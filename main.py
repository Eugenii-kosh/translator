from data import actions
import time

print('Вас приветствует простой переводчик. Следуйте инструкциям!\n')
time.sleep(3)

while True:
    tr = actions.Translator().Actions()
    result = tr
    print(result + '\n')
    if result == 'ERROR':
        print('ОШИБКА!\nПроверьте правильность ввода данных или соединения с интернетом.\n'
              'Возможно стоит ввести другие данные. Если проблема остаётся - Приносим свои извинения!\n')
        error = input(
            'Если хотите продолжить паботу нажмите 1 затем Enter, либо просто Enter если хотите выйти из программы!')
    writing = input(f'Записать в словарь - нажать (1 зетем Enter),\nПропустить запись - нажать (Enter),\n'
                    f'Выйти из программы - нажать (0(ноль) затем Enter): ')
    if len(writing) == 0:
        print('\n')
        continue
    elif writing == '0':
        break
    elif writing == '1':
        actions.Translator().WhriteIn(result)
        print('Словарь дополнен.\n')
    else:
        print('Вы ввели несоответствующее инструкции комбинацию.\n')
