
questions = [
  "1.Как называется компания, которая создается для развития новой идеи или инновационного продукта?",
  "2.Как называется человек или компания, которой вкладывает вкладывает деньги в бизнес с целью получения прибыли?",
  "3.Из плодов какого растения получают такую пряность как паприка?",
  "4.Что лечит ларинголог?",
  "5.Мяукающее животное, которое только спит и ест?",
  "6.Что является традиционной едой в кинотеатрах?",
  "7.Как называется первая домашняя птица, которую приручил человек?",
  "8.В каком году закончилась вторая мировая война?",
  "9.Как называется валюта в Индии?",
  "10.Какое имя у Антона?",
  "11.Сколько месяцев в году имеют 28 дней?",
  "12.Что можно видеть с закрытыми глазами?",
  "13.Что в огне не горит и в воде не тонет?",
]


answers = [
  "Стартап",
  "Инвестор",
  "Перец",
  "Гортань",
  "Кот",
  "Попкорн",
  "Курица",
  "1945",
  "Рупия",
  "Антон",
  "Все",
  "Сны",
  "Лед",
]

score = 0

print("Добро пожаловать в квиз по стартапам!")
print("Ответь на следующие вопросы: ")

print(questions[0])

user_input = input("Введи свой ответ: ")
print()
print(user_input)

if user_input.lower() == answers[0].lower():
  print("Правильно!")
  score = score + 1    
else:
  print("Неправильно!")

print(questions[1])
user_input = input("Введи свой ответ: ")
if user_input.lower() == answers[1].lower():
  print("Правильно!")
  score = score + 1  
else:
  print("Неправильно!")

print(questions[2])
user_input = input("Введи свой ответ: ")
if user_input.lower() == answers[2].lower():
  print("Правильно!")
  score = score + 1  
else:
  print("Неправильно!")
   
print(questions[3])
user_input = input("Введи свой ответ: ")
if user_input.lower() == answers[3].lower():
  print("Правильно!")
  score = score + 1  
else:
  print("Неправильно!")

print(questions[4])
user_input = input("Введи свой ответ: ")
if user_input.lower() == answers[4].lower():
  print("Правильно!")
  score = score + 1  
else:
  print("Неправильно!")
  
print(questions[5])
user_input = input("Введи свой ответ: ")
if user_input.lower() == answers[5].lower():
  print("Правильно!")
  score = score + 1  
else:
  print("Неправильно!")

print(questions[6])
user_input = input("Введи свой ответ: ")
if user_input.lower() == answers[6].lower():
  print("Правильно!")
  score = score + 1  
else:
  print("Неправильно!")

print(questions[7])
user_input = input("Введи свой ответ: ")
if user_input.lower() == answers[7].lower():
  print("Правильно!")
  score = score + 1  
else:
  print("Неправильно!")

print(questions[8])
user_input = input("Введи свой ответ: ")
if user_input.lower() == answers[8].lower():
  print("Правильно!")
  score = score + 1  
else:
  print("Неправильно!")

print(questions[9])
user_input = input("Введи свой ответ: ")
if user_input.lower() == answers[9].lower():
  print("Правильно!")
  score = score + 1  
else:
  print("Неправильно!")

print(questions[10])
user_input = input("Введи свой ответ: ")
if user_input.lower() == answers[10].lower():
  print("Правильно!")
  score = score + 1  
else:
  print("Неправильно!")

print(questions[11])
user_input = input("Введи свой ответ: ")
if user_input.lower() == answers[11].lower():
  print("Правильно!")
  score = score + 1  
else:
  print("Неправильно!")

print(questions[12])
user_input = input("Введи свой ответ: ")
if user_input.lower() == answers[12].lower():
  print("Правильно!")
  score = score + 1  
else:
  print("Неправильно!")

if score > 10:
   print("Это отличный результат!")
elif score > 5:
   print("Неплохой и нехороший результат.Но не растраивайся!")
else:
   print("Жалко осозновать.Но ты не такой уж и умный каким казался(казалась)")
  
print("Оцени пожалуйста игру от 1 до 10!")
Super_unput = input ("Введи свою оценку о игре: ")
print("Ваша оценка: " + Super_unput)
print("Спасибо за отзыв")
input_master = input("Скажи пока: ")

