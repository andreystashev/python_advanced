from datetime import datetime, timedelta
from random import choice
from flask import Flask

app = Flask(__name__)
cats = ['Корниш рекс', 'Русская голубая', 'Шотландская вислоухая', 'Мэйн-Кун', 'Манчкин']
war_words = []


@app.route('/hello_world')
def test_function():
    return 'Привет мир!'


@app.route('/cars')
def test_function1():
    return 'Chevrolet, Renault, Ford, Lada'


@app.route('/cats')
def test_function2():
    return choice(cats)


@app.route('/get_time/now')
def test_function3():
    return "Точное время {}".format(datetime.strftime(datetime.now(), '%H.%M.%S'))


@app.route('/get_time/future')
def test_function4():
    return "Точное время через час будет {}".format((datetime.now() + timedelta(hours=1)).time())


def test_function5(file_name='war_and_peace.txt'):
    with open(file_name, 'r', encoding='cp1251') as file:
        global war_words
        for line in file:
            for word in line.split():
                war_words.append(word)


@app.route('/get_random_word')
def test_function6():
    if len(war_words) < 1:
        test_function5()
    return choice(war_words)

# Зачёт!
