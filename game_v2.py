import numpy as np
def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: количество попыток
    """
    count = 0
    
    while True:
        count+=1
        predict_number=np.random.randint(1,101) #предполагаемое число
        if number == predict_number:
            break
    return(count)
print(f"Количество попыток:{random_predict()}")

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее число попыток
    """
    count_ls =[] #список для сохранения числа попыток
    np.random.seed(1) #фиксируем сид для воспроизводимости
    random_array = np.random.randint(1,101,size=(1000)) #загадали список целых чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls)) #среднее число попыток
    
    print(f"Ваш алгоритм угадывает угадывает число в среднем за: {score} попыток")
    return(score)

#RUN
if __name__ == '__main__':
    score_game(random_predict)