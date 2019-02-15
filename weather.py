import json
import gzip
import urllib.request
import urllib.error
import os
import sqlite3
from datetime import datetime
import requests

CURENT_DIR = os.getcwd()

def get_path(name_file):
    return os.path.join(CURENT_DIR + delimiter(), name_file)

class City_DB:
    def __init__(self):
        name_gz = 'city.gz'
        name_json = 'city.json'
        self.city_url = 'http://bulk.openweathermap.org/sample/city.list.json.gz'
        self.full_name = get_path(name_gz)
        self.full_name_json = get_path(name_json)

    def _check_file(self):
        if not os.path.isfile(self.full_name):
            self._request_file()

    def _request_file(self):
        try:
            print('Загрузка архива из интернета...')
            urllib.request.urlretrieve(self.city_url, self.full_name)
        except urllib.error.URLError: \
                print('Ошибка: не удалось загрузить архив')
        else:
            print('Архив успешно загружен')
        if not os.path.isdir(self.full_name_json):
            with gzip.open(self.full_name, 'rb') as in_file:
                self.s = in_file.read()
            with open(self.full_name_json, 'wb') as out_file:
                out_file.write(self.s)
            print('Архив успешно распакован')

    def find_city(self, fields):
        self._check_file()
        with open(self.full_name_json, encoding='utf-8') as file:
            city_dict = json.load(file)
            file.close()
        return [x for x in city_dict if all([(k, v) in x.items() for k, v in fields.items()])]

class Request_api:
    APP_ID = 'app.id'
    REQUEST_URL = r'https://api.openweathermap.org/data/2.5/weather?'

    def appid(self):
        with open(get_path(self.APP_ID), encoding="utf-8") as appid:
            result = appid.read()
            return result

    def get_data(self, city_id):
        request = 'http://api.openweathermap.org/data/2.5/weather?id={}&units=metric&appid={}'.format(city_id,
                                                                                                      self.appid())
        response = requests.get(request)
        return json.loads(response.content)

class SqlDB:
    DB_NAME = 'weather.db'
    def __init__(self):
        self._check_db_file_exist()

    def _execute_command(self, command, need_commit):
        connect = sqlite3.connect(get_path(self.DB_NAME))
        if command == 0:
            print('Создаем базу данных')
            answer = connect.cursor().execute('CREATE TABLE weather'
                                              '(city_id	INTEGER NOT NULL,'
                                              'city VARCHAR(255) NOT NULL,'
                                              'date	DATE NOT NULL,'
                                              'temperature	INTEGER NOT NULL,'
                                              'weather_id	INTEGER NOT NULL,'
                                              'weather_icon  VARCHAR(4) NOT NULL,'
                                              'PRIMARY KEY(city_id))')
        else: answer = list(connect.cursor().execute(command))
        if need_commit:
            connect.commit()
        connect.close()
        return answer

    def _check_data_exist(self, city_id):
        rows = self.get_data({'city_id': city_id})
        return len(rows) != 0

    def _check_db_file_exist(self):
        if not os.path.isfile(get_path(self.DB_NAME)):
            command = 0
            self._execute_command(command, True)

    def get_columns(self):
        connect = sqlite3.connect(get_path(self.DB_NAME))
        cursor = connect.execute('select * from weather')
        columns = [desc[0] for desc in cursor.description]
        connect.close()
        return columns

    def get_data(self, i_=None, o_=None):
        if o_:
            columns = ",".join(o_)
        else:
            columns = '*'
        command = f'SELECT {columns} FROM weather '

        if i_:
            return self._execute_command(command, False)

    def set_data(self, values):
        if self._check_data_exist(values[0]):
            command = f'UPDATE weather SET temperature="{values[3]}", date="{values[2]}", weather_icon="{values[5]}"' \
                f' WHERE city_id="{values[0]}"'
        else:
            values = map(lambda x: f'"{str(x)}"', values)
            command = f'INSERT INTO weather VALUES({",".join(values)})'
            self._execute_command(command, True)

def delimiter():
    if os.name == 'posix':
        delimiter = '/'
    else:
        delimiter = '\\'
    return delimiter

def search_city(country, city):
    print('Поиск города')
    cities = City_DB()
    result = cities.find_city({'name': city, 'country': country.upper()})
    if len(result) == 0:
        print('Город не найден!')
        return None
    if len(result) > 1:
        print('\n'.join([f'{i}. {str(x)}' for i, x in enumerate(result)]))
        index = int(input('Город введен не корректно:\n'))
        return result[index]
    return result[0]

def get_json_data(city_json):
    api = Request_api()
    json_data = api.get_data(city_json['id'])
    return json_data

def update_db(json_data):
    weather = SqlDB()
    weather.set_data([json_data['id'], json_data['name'], datetime.now().strftime('%Y-%m-%d'), json_data['main']['temp'],
                      json_data['weather'][0]['id'], json_data['weather'][0]['icon']])
    print(datetime.now().strftime('%Y-%m-%d '), json_data['name'], ' ', json_data['main']['temp'], 'C')

def main():
    print('Введите страну и город:')
    country = input('Страна: ')
    city = input('Город: ')
    city_json = search_city(country, city)
    if city_json:
        json_data = get_json_data(city_json)
        if json_data:
            update_db(json_data)

if __name__ == '__main__':
    main()