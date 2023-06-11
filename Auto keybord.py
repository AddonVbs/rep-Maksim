from pynput.keyboard import Key, Controller
import time
from rich.console import Console
from rich.progress import track
from Faille import Password_haki


console = Console()

numpassword = 'h'

Keyboard = Controller()
Password = Faille

console.print("Ввидите какой ваш язык >> See what your language is", style="bold green")
console.print("напишите 'rus' если ваш язык Русский >> write 'eng' if your language is English", style="bold green")





translate = str(input(""))
if translate == int:
    print("Вы ввели число, а надо букву ")
    print('Попробуйте еще раз, перезагрузить программу!')
if translate == 'rus':
    print("ввидите пароль")
    num_password = str(input(""))
    
    for i in track(range(100),description='Загрузка...'):
        time.sleep(0.03)

    if not num_password == Password:
        print("Пароль не верный попробуй другой")
        print("перезагрузите программу!") 
        num = str(input(""))
    
    if num_password == int:
        print("вы ввели букву, а надо число")
        print("попробуйте еще раз, перезагрузить программу!")            #rus line

    if num_password == Password:
        print('Пароль верный !')
        print('Ввидите на какую кнопк убудет произвидится нажатия')
        num = str(input(""))
        if num == int:
            print("Вы ввели число, а надо букву ")
            print('Попробуйте еще раз, перезагрузить программу!')


        console.print(f'Введите сколько будет нажатий на [red]"{num}"[/red]')
        For = int(input(""))
        if For == str:
            print("Вы ввели букву, а надо число")
            print("Попробуйте еще раз, перезагрузить программу!")

        console.print(f"Введите  с каким интервалом будет нажиматся кнопка [red]'{num}'[/red], учитывается в СЕКУНДАХ. 0.5 милисекунды!!")
        print("Для GPO Haki v2 надо 120 секунд")
        time1 = int(input(""))
        if time1 == str:
            print("Вы ввели букву, а надо число")
            print("Попробуйте еще раз, перезагрузить программу!")
    
        console.print(f'Введите [red]"{numpassword}"[/red] чтобы начать')

        num1 = str(input(""))
        if num1 == numpassword:
            for i in range(0, For ):
                time.sleep(time1)
                Keyboard.press(num)
                Keyboard.release(num)

    else:
        print("Пароль не верный !")
        print("Перезагрузите программу")
            











if translate == 'eng':
    print("enter password")
    num_password = str(input(""))
    
    for i in track(range(100),description='Загрузка...'):
        time.sleep(0.03)
    
    if not num_password == Password:
        print("Password is not correct, try another")
        print("restart the program!") 
        num = str(input(""))
    
    if num_password == int:
        print("you entered a letter, but you need a number")
        print("try again, restart the program!")

    if num_password == Password:
        print('Password is correct!')
        print('See which button will be pressed')
        num = str(input(""))
        
        if num == int:
            print("You entered a number, but you need a letter ")
            print('Try again, restart the program!')


        console.print(f'Enter how many clicks to [red]"{num}"[/red]')
        For = int(input(""))
        if For == str:
            print("You entered a letter, but you need a number")
            print("Try again, restart the program!")

        console.print(f"Enter at what interval the [red]'{num}'[/red] button will be pressed, counted in SECONDS. 0.5 milliseconds!!")
        print("GPO Haki v2 needs 120 seconds")
        time1 = int(input(""))
        if time1 == str:
            print("You entered a letter, but you need a number")
            print("Try again, restart the program!")
    
        console.print(f'Enter [red]"{numpassword}"[/red] to start')

        num1 = str(input(""))
        if num1 == numpassword:
            for i in range(0, For ):
                time.sleep(time1)
                Keyboard.press(num)
                Keyboard.release(num)

    else:
        print("Wrong password !")
        print("Reload the program")
