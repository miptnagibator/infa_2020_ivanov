import random
import vk_api  # подключаем апи бота
import requests  # подключим библиотеку requests
from bs4 import BeautifulSoup  # и библиотеку BeautifulSoup
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

token = "31708ce0fc77f37c8e4b0ec34e8a942f965d5cb3fb421ef46df05f41c52ec261f416e390c99c9f0d24cd0"
zodiac = ["Рак", "Лев", "Дева", "Рыбы", "Стрелец", "Козерог", "Овен", "Скорпион", "Водолей", "Весы", "Близнецы",
          "Телец"]

# подключаемся к сообществу
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

# включаем бота в режим приема сообщений
longpoll = VkBotLongPoll(vk_session, "187720244")


def znak(Znak):
    l = ["Ты лол", "Ты кек", "Ты чебурек", ]
    i = random.randint(0, len(l) - 1)
    return l[i]


pogoda = [["Погода в Иркутске", "https://darksky.net/forecast/52.2826,104.3158/si12/en"],
          ["Погода в Новосибирске", "https://darksky.net/forecast/55.0456,82.9321/si12/en"],
          ["Погода в Москве", "https://darksky.net/forecast/55.7415,37.6156/si12/en"],
          ["Погода в Твери", "https://darksky.net/forecast/56.854,35.9038/si12/en"],
          ["Погода в Владивостоке", "https://darksky.net/forecast/43.1171,131.896/si12/en"]]


def proverka(l):
    for i in pogoda:
        if l == i[0]:
            return 1


def pogod(lol):
    for i in pogoda:
        if lol == i[0]:
            page = requests.get(i[1])  # загрузим веб-страницу по ссылке
            soup = BeautifulSoup(page.text, 'html.parser')  # загрузим ее в библиотеку
            return soup.find_all("span", class_='summary swap')[0].get_text()
    return "Такого города нет в базе"


def send_privet():
    vk.messages.send(
        user_id=event.obj.from_id,
        random_id=get_random_id(),
        message="И тебе привет, как тебя зовут?")
    for eventx in longpoll.listen():  # вечно ждем новых сообщений
        if eventx.type == VkBotEventType.MESSAGE_NEW:  # если сообщение пришло
            if eventx.obj.text != '':  # и оно не пустое
                if eventx.from_user:  # да еще и от пользователя
                    user_sent = eventx.obj.text  # возьмем его текст
                    vk.messages.send(
                        user_id=eventx.obj.from_id,
                        random_id=get_random_id(),
                        message="Привет, " + user_sent + ". Ты можешь узнать погоду, свое будущее или узнать результаты последнего спортивного матча")
                    break


def send_pogoda():
    vk.messages.send(
        user_id=event.obj.from_id,
        random_id=get_random_id(),
        message=pogod(user_sent))


def sport():
    page = requests.get("https://www.sport-express.ru/live/yesterday/football")  # загрузим веб-страницу по ссылке
    soup = BeautifulSoup(page.text, 'html.parser')
    z = soup.find_all("td", class_='match__time-start')[0].get_text()

    a = soup.find_all("td", class_='match__commands')[0].get_text()
    b = ""
    for i in range(len(a)):
        b += a[i]
        if a[i] == " ":
            if a[i + 1] == " ":
                break

    x = soup.find_all("span")[26].get_text()
    y = ""
    for i in range(len(x)):
        if x[i] != " ":
            y += x[i]

    vk.messages.send(
        user_id=event.obj.from_id,
        random_id=get_random_id(),
        message="Футбол: " + z + b + y)


# Обрабтка сообщений
for event in longpoll.listen():  # вечно ждем новых сообщений
    if event.type == VkBotEventType.MESSAGE_NEW:  # если сообщение пришло
        if event.obj.text != '':  # и оно не пустое
            if event.from_user:  # да еще и от пользователя
                user_sent = event.obj.text  # возьмем его текст
                if user_sent == "ПРИВЕТ":  # если текст равен "ПРИВЕТ"
                    send_privet()
                elif user_sent in zodiac:
                    vk.messages.send(
                        user_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message=znak(user_sent))
                elif proverka(user_sent) == 1:
                    send_pogoda()
                elif user_sent == "Спорт":
                    sport()
                else:
                    vk.messages.send(
                        user_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message="Нічого не зрозуміло. Повтори будь ласка")  # иначе вернем сообщение назад