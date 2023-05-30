# 1. Открыть файл+
# 2. Показать все контакты+
# 3. Добавть контакт+
# 4. Найти контакт+
# 5. Изменить контакт+
# 6. Удалить контакт+
# 7. Выход+
# 8. Сохранить файл+


def open_file_read(path):
    with open(path, 'r') as file:
        main_list = file.readlines()
        main_list_str = [x.rstrip().split(':') for x in main_list]
    return main_list_str
        

def open_file_write(path, list_file):
    with open(path, 'w') as file:
        file.writelines([':'.join(x)+'\n' for x in list_file])


def look_for_list(path):
    with open(path, 'r') as file:
        print(open_file_read('info.txt'))

look_for_list('info.txt')

def add_contact(path):
    with open(path, 'a') as file:
        new_contact = input('Введите имя телефон и коментарий контакта через пробел ')
        file.write(new_contact + '\n')

add_contact('info.txt')

def find_contact(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        req_str = int(input('Введите номер строки необходимого контакта '))
        for i in range(req_str, req_str + 1 ):
            print(lines[i-1], end='')



find_contact('info.txt')



def change_contact(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        req_str = int(input('Введите номер строки контакта который хотите изменить '))
        new_cont = str(input('Введите новые данные контакта '))
        for i in range(req_str, req_str + 1 ):
            lines[i-1] = new_cont+'\n'
            file =lines[i-1].replace(lines[i-1],new_cont)
        file = open(path, 'w')
        file.writelines(lines)
        file.close()

change_contact('info.txt')

def del_cont(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        req_str = int(input('Введите номер строки контакта который необходимо удалить '))
        for i in range(req_str, req_str + 1 ):
            lines[i-1] = ''
        file = open(path, 'w')
        file.writelines(lines)
        file.close()

del_cont('info.txt')


def save_func(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        file = open(path, 'w')
        file.writelines(lines)
        file.close()

save_func('info.txt')