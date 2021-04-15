import random
from array import *


def menu(list_temp, chosen_temp):
    print("\n1. Создание массива\n"
          "2. Удалить определенные числа\n"
          "3. Удалить один элемент по индексу\n"
          "4. Сортировать(по убыванию/возрастанию)\n"
          "5. Вывести список\n"
          "6. Вывести количество элементов\n"
          "7. Сбросить все\n"
          "8. Закончить")
    case_temp = int(input())

    if case_temp == 1 and chosen_temp == 0:
        list_temp = hand_input()
        chosen_temp = 1
    elif case_temp == 2 and chosen_temp == 1:
        list_temp = delete_group(list_temp)
    elif case_temp == 3 and chosen_temp == 1:
        list_temp = delete_element(list_temp)
    elif case_temp == 4 and chosen_temp == 1:
        list_temp = sort(list_temp)
    elif case_temp == 5 and chosen_temp == 1:
        list_the_list(list_temp)
    elif case_temp == 6:
        count_list(list_temp)
    elif case_temp == 7:
        chosen_temp = 0
    elif case_temp == 8:
        print("Спасибо за работу со мной")
        return
    else:
        print("Ошибка\n\n")
    menu(list_temp, chosen_temp)


def delete_group(list_temp):
    chosen_temp = 0
    while chosen_temp != 1:
        case_temp = int(input("\n1. Удалить четные числа\n"
                              "2. Удалить нечетные числа\n"))
        if case_temp == 1:
            for i in range(len(list_temp))[::-1]:
                if not list_temp[i] % 2:
                    del list_temp[i]
            print("Удаление прошло успешно!\n")
            return list_temp
        elif case_temp == 2:
            for i in range(len(list_temp))[::-1]:
                if list_temp[i] % 2:
                    del list_temp[i]
            print("Удаление прошло успешно!\n")
            return list_temp
        else:
            print("Ошибка при выборе\n\n")
            continue


def delete_element(list_temp):
    chosen_temp = 0

    while chosen_temp != 1:
        case_temp = int(input("\n1. Удалить число по индексу\n"
                              "2. Удалить число по значению\n"))
        if case_temp == 1:
            list_temp.pop(int(input("Введите индекс элемента:\n")))
            print("Удаление прошло успешно!\n")
            return list_temp
        elif case_temp == 2:
            list_temp.remove(int(input("Введите значение элемента элемента:\n")))
            print("Удаление прошло успешно!\n")
            return list_temp
        else:
            print("Ошибка при выборе\n\n")
            continue


def sort(list_temp):
    chosen_temp = 0

    while chosen_temp != 1:
        case_temp = int(input("\n1. Сортировать по убыванию\n"
                              "2. Сортировать по возрастанию\n"))
        if case_temp == 1:
            for i in range(len(list_temp) - 1):
                for j in range(len(list_temp) - i - 1):
                    if list_temp[j] < list_temp[j + 1]:
                        list_temp[j], list_temp[j + 1] = list_temp[j + 1], list_temp[j]
            print("Отсортировано!\n")
            return list_temp
        elif case_temp == 2:
            for i in range(len(list_temp) - 1):
                for j in range(len(list_temp) - i - 1):
                    if list_temp[j] > list_temp[j + 1]:
                        list_temp[j], list_temp[j + 1] = list_temp[j + 1], list_temp[j]
            print("Отсортировано!\n")
            return list_temp
        else:
            print("Ошибка при выборе\n\n")
            continue


def list_the_list(list_temp):
    for i in range(len(list_temp)):
        print(str(list_temp[i]), end=' ')


def count_list(list_temp):
    print("Количество элементов массива: ", len(list_temp))


def hand_input():
    size = int(input("Введите размер массива:\n"))
    list_temp = array('i', [])

    chosen_temp = 0

    while chosen_temp != 1:
        case_temp = int(input("1. Случайные элементы массива\n"
                              "2. Ввести вручную\n"))
        if case_temp == 1:
            a = int(input("Введите нижнюю границу рандома:\n"))
            b = int(input("Введите верхнюю границу рандома:\n"))
            for i in range(size):
                list_temp.append(random.randint(a, b))
            chosen_temp = 1
        elif case_temp == 2:
            for i in range(size):
                list_temp.append(int(input("Введите элемент массива " + str(i+1) + ":\n")))
            chosen_temp = 1
        else:
            print("Ошибка при выборе\n\n")
            continue
    print("Массив создан успешно!")
    return list_temp


print("Приветствую! Я кривая программа, написанная красноглазым shitty-кодером.\n"
      "Выбери следующее действие:")

list_end = []
chosen = 0
menu(list_end, chosen)
