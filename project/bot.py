"""Подключаем библиотеки vk_api - для взаимодействия с вк,
request - для загрузки HTML документа, BeautifulSoup - для обработки
тегов HTML"""
from convertion import convert
import vk_api
import requests
from bs4 import BeautifulSoup
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

token = "31708ce0fc77f37c8e4b0ec34e8a942f965d5cb3fb421ef46df05f41c52ec261f416e390c99c9f0d24cd0"

# подключаемся к сообществу
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

# включаем бота в режим приема сообщений
longpoll = VkBotLongPoll(vk_session, "187720244")

# База данных бота
list_of_cities = [["погода в иркутске", "https://darksky.net/forecast/52.2826,104.3158/si12/en"],
                  ["погода в новосибирске", "https://darksky.net/forecast/55.0456,82.9321/si12/en"],
                  ["погода в москве", "https://darksky.net/forecast/55.7415,37.6156/si12/en"],
                  ["погода в твери", "https://darksky.net/forecast/56.854,35.9038/si12/en"],
                  ["погода в владивостоке", "https://darksky.net/forecast/43.1171,131.896/si12/en"]]

week1 = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
week2 = ['понедельник', 'вторник', 'среду', 'четверг', 'пятницу', 'субботу', 'воскресенье']

numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

list_of_numerals_and_signs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              "A", "B", "C", "D", "E", "F", "+", "-", "/", "*",
                              "(", ")", "." ]

list_of_nice_numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                         "A", "B", "C", "D", "E", "F"]
list_of_nice_signs = ["+", "-", "/", "*", "(", ")", "."]

list_of_nice_latters = ["A", "B", "C", "D", "E", "F"]


# Функции для обработки сообщений

def send_massage(text, event):
    '''
    Функция отправляет сообщение пользователю.
    :param text: текст сообщения
    :param event: событие сообщения
    :return: None
    '''
    vk.messages.send(
        user_id=event.obj.from_id,
        random_id=get_random_id(),
        message=text)


def check_weather(user_massage, list_of_cities):
    '''
    Функция проверяет, хочет ли пользователь узнать погоду в каком-то городе
    :param user_massage: Текст сообщения
    :param list_of_cities: Список городов и URL адресов этих городов с сайта darksky.net
    :return: None
    '''
    for i in list_of_cities:
        if user_massage.lower() == i[0]:
            return 1


def return_weather(user_massage):
    """
    Функция возвращает прогноз погоды в данном городе.
    :param user_massage: Текст сообщения пользователя.
    :return: None
    """
    for i in list_of_cities:
        if user_massage.lower() == i[0]:
            page = requests.get(i[1])  # загрузим веб-страницу по ссылке
            soup = BeautifulSoup(page.text, 'html.parser')  # загрузим ее в библиотеку
            return soup.find_all("span", class_='summary swap')[0].get_text()


def send_weather():
    '''
    Функция отправляет сообщение с прогнозом погоды.
    :return: None
    '''
    send_massage(return_weather(user_sent), event)


def check_timetable(user_message):
    '''
    Функция проверяет, есть ли в сообщении ключевые слова, связанные с расписанием.
    :param user_message: Текст сообщения пользователя.
    :return: True(если в сообщении есть слово <<расписание>>),
    False(если в сообщении его нет), day(если есть слово <<расписание>> и есть день недели,
     то возвращает номер дня недели.)
    '''
    list = user_message.split()
    bool = 0
    for i in range(len(list)):
        if list[i].lower() == 'расписание':
            bool += 1
            for j in range(len(list)):
                if list[j].lower() in week1:
                    day = list[j].lower()
                    print("True")
                    bool += 1
                    break
                if list[j].lower() in week2:
                    day = list[j].lower()
                    print("True")
                    bool += 1
                    break
    if bool == 2:
        return day
    if bool == 1:
        return True
    if bool == 0:
        return False


def return_timetable(request, file_with_timetable):
    """
    Функция обрабатывает результат check_timetable() и отправляет сообщение с расписанием.
    :param request: Результат функции check_timetable()
    :param file_with_timetable: txt файл с расписанием на неделю
    :return: None
    """
    timetable = []
    day = 0
    string = ""
    if str(type(request)) == "<class 'str'>":
        for i in range(len(week1)):
            if request == week1[i]:
                day = i
        for i in range(len(week2)):
            if request == week2[i]:
                day = i
        with open(file_with_timetable, 'r', encoding="utf-8") as file:
            for line in file:
                a = line.split(",")
                timetable.append(a)
            for i in range(len(timetable[day])):
                string += timetable[day][i] + "\n"
            send_massage(string, event)
    if request == True:
        send_massage("Чтобы бот выдал расписание, в сообщении должно"
                     " быть слово <<расписание>> и день недели, на который вы хотите узнать расписание.", event)
    if request == False:
        pass


def sport():
    """
    Функция выводит результат вчерашнего футбольного матча с сайта ставок на спорт.
    :return: None
    """
    page = requests.get("https://www.sport-express.ru/live/yesterday/football")  # загрузим веб-страницу по ссылке
    soup = BeautifulSoup(page.text, 'html.parser')
    time_of_start = soup.find_all("td", class_='match__time-start')[0].get_text()

    commands = soup.find_all("td", class_='match__commands')[0].get_text()
    true_commands = ""
    for i in range(len(commands)):
        true_commands += commands[i]
        if commands[i] == " ":
            if commands[i + 1] == " ":
                break

    score = soup.find_all("span")[26].get_text()
    true_score = ""
    for i in range(len(score)):
        if score[i] != " ":
            true_score += score[i]

    send_massage("Футбол: " + time_of_start + true_commands + true_score, event)


def calulator():
    '''
    Функция включает режим калькулятора.
    Функция обрабатывает сообщения пользователя.
    Сначала принимается система (от 2 до 16),
    потом арифметическое выражение, выполняется его парсеринг,
    перевод каждого числа в 10 систему, выполнение данного выражения,
    перевод его в изначальную систему и вывод результата.
    Проработана система ошибок:
    Ошибка 1: при вводе основания системы.
        Ошибка 1.1: В сообщении встречается не число,
            а набор недопустимых символов.
        Ошибка 1.2: Введенное основание больше 16 или меньше 2.
    Ошибка 2: при вводе выражения.
        Ошибка 2.1: Данное выражение содержит недопустимые символы.
        Ошибка 2.2: Данное выражение содержит цифры не для осования, введенного ранее.
        Ошибка 2.3: Данное выражение содержит арифметическую ошибку
            (деление на 0, неправильную постановку знаков арифметических действий).
    Для возвращения на шаг назад нужно ввести слово <<назад>>.
    :return: None
    '''
    send_massage("Введите основание системы счисления:", event)
    for eventx in longpoll.listen():  # вечно ждем новых сообщений
        if eventx.type == VkBotEventType.MESSAGE_NEW:  # если сообщение пришло
            if eventx.obj.text != '':  # и оно не пустое
                if eventx.from_user:  # да еще и от пользователя
                    user_sentx = eventx.obj.text  # возьмем его текст

                    exit_code = 0
                    if user_sentx.lower() == "назад":
                        exit_code = 3
                        send_massage("Выключен режим калькулятора", eventx)

                    if exit_code == 0:
                        for i in user_sentx:
                            if bool(i in numerals) == False:
                                send_massage("Ошибка 1.1: В сообщении не число", eventx)
                                exit_code = 1
                                break

                    if exit_code == 0:
                        if int(user_sentx) > 16 or int(user_sentx) < 2:
                            send_massage("Ошибка 1.2: Основание больше 16 или меньше 2", eventx)
                            exit_code = 1

                    if exit_code == 0:
                        base = int(user_sentx)
                        send_massage("Введите пример:", eventx)

                        for eventy in longpoll.listen():  # вечно ждем новых сообщений
                            if eventy.type == VkBotEventType.MESSAGE_NEW:  # если сообщение пришло
                                if eventy.obj.text != '':  # и оно не пустое
                                    if eventy.from_user:  # да еще и от пользователя
                                        user_senty = eventy.obj.text  # возьмем его текст

                                        exit_code = 0
                                        if user_senty.lower() == "назад":
                                            exit_code = 2

                                        if exit_code == 0:
                                            for i in user_senty:
                                                if bool(i in list_of_numerals_and_signs) == False:
                                                    exit_code = 1
                                                    send_massage(
                                                        "Ошибка 2.1: данное выражение содержит недопустимые символы.",
                                                        eventy)
                                                    break

                                        base_list = list_of_nice_numerals[:base]

                                        if exit_code == 0:
                                            for i in user_senty:
                                                if bool(i in base_list) == False:
                                                    if bool(i in list_of_nice_signs) == False:
                                                        print(bool(i in base_list))
                                                        print(bool(i in list_of_nice_signs))
                                                        print(i)
                                                        exit_code = 1
                                                        send_massage(
                                                            "Ошибка 2.2: данное выражение содержит цифры не для осования " + str(
                                                                base),
                                                            eventy)
                                                        break



                                        if exit_code == 0:
                                            list_of_signs = []
                                            list_of_numerals = []
                                            result = ''
                                            user_senty.split()
                                            print(user_senty)
                                            for i in range(len(user_senty)):
                                                if user_senty[i] in list_of_nice_numerals:
                                                    list_of_numerals.append([user_senty[i], i])
                                                if user_senty[i] in list_of_nice_signs:
                                                    list_of_signs.append([user_senty[i], i])

                                            print(list_of_numerals)
                                            list_of_true_numerals = []
                                            nomber = -1
                                            numeral = ""
                                            for i in list_of_numerals:
                                                if i[1] == nomber + 1:
                                                    numeral += i[0]
                                                    nomber += 1
                                                elif i[1] != nomber + 1:
                                                    list_of_true_numerals.append([numeral, nomber])
                                                    nomber = i[1]
                                                    numeral = i[0]
                                            list_of_true_numerals.append([numeral, nomber])
                                            print(list_of_true_numerals)

                                            for i in range(len(list_of_true_numerals)):
                                                list_of_true_numerals[i][0] = convert(list_of_true_numerals[i][0], base,
                                                                                      10)
                                            print(list_of_true_numerals)

                                            for i in range(len(user_senty)):
                                                for j in list_of_true_numerals:
                                                    if j[1] == i:
                                                        result += j[0]
                                                        del j
                                                        break
                                                for k in list_of_signs:
                                                    if k[1] == i:
                                                        result += k[0]
                                                        del k
                                                        break
                                            print(result)
                                            try:
                                                eval(result)
                                            except:
                                                exit_code = 1
                                                send_massage(
                                                    "Ошибка 2.3: данное выражение содержит арифметическую ошибку.",
                                                    eventy)
                                            if exit_code == 0:
                                                result = eval(result)
                                                result = convert(str(result), 10, base)
                                                result.split()
                                                if result[0] == ".":
                                                    result = "0" + result
                                                send_massage(result, eventy)

                                        if exit_code == 2:
                                            send_massage("Введите новую систему счисления:", eventy)
                                            break
                    if exit_code == 3:
                        break


# Обрабтка сообщений
for event in longpoll.listen():  # вечно ждем новых сообщений
    if event.type == VkBotEventType.MESSAGE_NEW:  # если сообщение пришло
        if event.obj.text != '':  # и оно не пустое
            if event.from_user:  # да еще и от пользователя
                user_sent = event.obj.text  # возьмем его текст
                if user_sent.lower() == "калькулятор":
                    calulator()
                elif check_weather(user_sent, list_of_cities) == 1:
                    send_weather()
                elif user_sent.lower() == "футбол":
                    sport()
                elif check_timetable(user_sent) != False:
                    return_timetable(check_timetable(user_sent), 'timetable.txt')
                else:
                    send_massage("Нічого не зрозуміло. Повтори будь ласка", event)
