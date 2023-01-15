import random
candy = 101
player_1 = input('Игрок 1 введите имя: ')
player_2 = 'робот Игорь'
players = [player_1, player_2]
count = random.randint(1,6)
print(f'Ходит игрок {players[count%2]}')
while candy > 28:
    if count%2==0:
        candy_take = input(f'Игрок {players[count%2]} возьмите от 1 до 28 конфет: ')
        if candy_take.isdigit()==False:
            print('Введите цифру')
            continue
        candy_take = int(candy_take)
        if candy_take > 28 or candy_take < 1:
            print("Введите коректное число")
            continue
        candy-=candy_take
        count+=1
        print('осталось: ', candy)
    else:
        candy_take = random.randint(1,28)
        print(f'робот Игорь забрал {candy_take} конфет')
        candy-=candy_take
        count+=1
        print('осталось: ', candy)
print(f"Победа за игроком {players[count%2]}")
