import random

def guess_number():
       secret_number = random.randint(1, 100)
       attempts = 0

       print("Добро пожаловать в игру 'Угадай число'!")
       print("Я загадаю тебе число от 1 до 100. Попробуй угадать его!")

       while True:
              user_guess = input('Твой ответ: ')

              try:
                     user_guess = int(user_guess)
              except ValueError:
                     print('Пожалуйста, введите число.')
                     continue
              attempts += 1

              if user_guess < secret_number:
                     print('Число больше, попробуй еще')
              elif user_guess > secret_number:
                     print('Число меньше, попробуй еще')
              else:
                     print(f"Поздравляем! Вы угадали число. Вы потратили попыток: {attempts}")
                     break
if __name__ == "__main__":
       guess_number()



       