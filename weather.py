import json
import gzip
import urllib.request
import urllib.error
import os
import sqlite3
import time



class City_DB:
    def __init__(self):
        self.name_json = 'city.json'
        self.name_gz = 'city.gz'
        self.delimiter = _delimiter()
        self.city_url = 'http://bulk.openweathermap.org/sample/city.list.json.gz'
        self.full_name = os.getcwd() + self.delimiter + self.name_gz
        self.full_name_json = os.getcwd() + self.delimiter + self.name_json

    def city_list(self):
        if not os.path.isfile(self.full_name_json):
            if not os.path.isfile(self.full_name):
                print('Загрузка архива из интернета...')
                try:
                    urllib.request.urlretrieve(self.city_url, self.full_name)
                except urllib.error.URLError:\
                        print('Ошибка: не удалось загрузить архив')
                else:
                    print('Архив успешно загружен')
            if not os.path.isdir(self.full_name_json):
                with gzip.open(self.full_name, 'rb') as in_file:
                    self.s = in_file.read()
                with open(self.full_name_json, 'wb') as out_file:
                    out_file.write(self.s)
                print('Архив успешно распакован')

        with open(self.full_name_json, encoding='utf-8') as file:
            city_dict = json.load(file)
            file.close()
        return city_dict


class Creat_DB:
    def __init__(self):
        self.db_name = 'weather.db'
        self.delimiter = _delimiter()

    def weather_data(self, data, id_city, name, temp, id_weather):
        sql = sqlite3.connect(self.db_name)
        c = sql.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS weather '
                  '(data INTEGER, '
                  'id_city INTEGER, '
                  'name VARCHAR(128), '
                  'temp VARCHAR(45), '
                  'id_weather)')
        check = c.execute("SELECT * FROM weather WHERE data='{}' AND id_city='{}'".format(data, id_city))
        check = check.fetchall()

        if check:
            data = time.ctime(check[0][0])
            result_print = 'Дата: {} |ID: {} |Город: {} |Темература: {} |ID_погоды: {}'.format(data, check[0][1], check[0][2], check[0][3], check[0][4])
            sql.close()
            return result_print
        else:
            c.execute('INSERT INTO weather VALUES ({},  {}, "{}", {}, {})'.format(data, id_city, name, temp, id_weather))
            data = time.ctime(data)
            result_print = 'Дата: {} |ID: {} |Город: {} |Темература: {} |ID_погоды: {}'.format(data, id_city, name, temp, id_weather)
            sql.commit()
            sql.close()
            return result_print

class Weather_DB:
    def __init__(self):
        self.city = City_DB()
        self.sql_base = Creat_DB()
        self.city_dict = self.city.city_list()
        self.app_id = 'app.id'
        self.name = 'Mooreland'
        self.id_city = '4542994'

    def appid(self):
        with open(self.app_id, encoding="utf-8") as appid:
            self.result = appid.read()
            return self.result

    def start(self):
        url_weather = 'http://api.openweathermap.org/data/2.5/weather?id={}&units=metric&appid={}'.format(self.id_city, self.appid())
        with urllib.request.urlopen(url_weather) as buffer:
            weather = json.load(buffer)
            id_weather = weather['weather'][0]['id']
            data_time = weather['dt']
            temp = weather['main']['temp']
            result = self.sql_base.weather_data(data_time, self.id_city, self.name, temp, id_weather)


def _delimiter():
    if os.name == 'posix':
        delimiter = '/'
    else:
        delimiter = '\\'
    return delimiter

s = City_DB()
print(s.city_list())

w = Weather_DB()
w.start()