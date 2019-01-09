# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def _mkdir(name_dir):
    if os.path.isdir(name_dir) != True:
        os.mkdir(name_dir, 777)
        print('Директория успешно создана:', name_dir)
    elif os.path.isdir(name_dir) == True:
        print('Директория уже существует:', name_dir)
    else:
        print('Невозможно создать директорию: ', name_dir)

#for i in range(1, 10):
#    name_dir = 'dir_' + str(i)
#    os.mkdir(name_dir, 777)

def _rmdir(name_dir):
    if os.path.isdir(name_dir) == True:
        os.rmdir(name_dir)
        print('Директория успешно удалена: ', name_dir)
    elif os.path.isdir(name_dir) != True:
        print('Директория для удаления не найдена: ', name_dir)
    else:
        print('Невозможно удалить директорию: ', name_dir)

#for i in range(1, 10):
#    name_dir = 'dir_' + str(i)
#    os.rmdir(name_dir)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def _listdir(dir_name):
    l = os.listdir(dir_name)
    for l in l:
        names = os.path.join(dir_name, l)
        if os.path.isdir(names):
            print(names)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def _file_copy(_path):
    dir_s = os.path.abspath(_path)
    filename = os.path.basename(__file__)
    file_content = open(__file__).read()
    if open(os.path.join(dir_s, 'copy_' + filename), 'w').write(file_content):
        print('Файл скопирован: ', 'copy_' + filename)


#_file_copy('.')