# Рівень 1 (Легкий)
# Вивести всі парні числа, кратні 4, від 1 до 40.
# def even_numb():
#     for i in range(1,40):
#         if i%4==0:
#             print(i,end=",")
# even_numb()
# Перевірити, чи всі символи в рядку — цифри.
# def is_digit_all():
#     str2 = '1231231231ddd231231'
#     if not str2.isdigit():
#         return "BAD"
#     return "GOOOOD"
# print(is_digit_all())
# Створити список довжин слів у реченні.
# def lenght_of_words():
#     str = 'awdasdawd ww dwadsadw dd wdawsd dd wwas'
#     lenOfWords = []
#     for i in str.split():
#         lenOfWords.append(len(i))
#     return lenOfWords
# print(lenght_of_words())



#
# Рівень 2 (Середній)
# Створити функцію, яка визначає, чи список чисел відсортований за зростанням.
# def list_is_sorted(lst):
#     for i in range(len(lst)):
#         if lst[i+1]<lst[i]:
#             return "List isn`t sorted"
#         else:
#             return "List is sorted"
#
# lst = [1,2,3,4,5,6,7,8,9]
# print(list_is_sorted(lst))
# # Побудувати словник: цифра → кількість входжень у тексті.
# def dict_with_nums():
#     str = 'da ad da ad da ad ff ff ff ff gg gg gg rrt rrt rrt'
#     dict = {}
#     for i in str.split():
#         dict[i] = dict.get(i,0)+1
#     return dict
# print(dict_with_nums())

# Написати функцію, яка повертає список слів, у яких немає голосних.
# def without_vowels():
#     s = 'da ad da ad da ad ff ff ff ff gg gg gg rrt rrt rrt'
#     str2 = []
#     vowels = 'aeiouyауоыиэяюёе'
#     for i in s.split():
#         isVowel = False
#         for k in i:
#             if k in vowels:
#                 isVowel = True
#                 break
#         if not isVowel:
#             str2.append(i)
#     return str2
# print(without_vowels())


# Рівень 3 (Складний)
# Зчитати файл і вивести найкоротші рядки (за кількістю символів).
# Створити функцію, яка приймає шлях до JSON-файлу і повертає відсортований список за певним параметром.
# Типізована функція: приймає словник {рік: список продажів} і повертає рік з найбільшим продажем.
# def work_with_dict(dct:dict) ->int:
#     maxYear = 0
#     maxtotal = -1
#     for y in dct:
#         total = sum(dct[y])
#         if total>maxtotal:
#             maxtotal = total
#             maxYear = y
#     return  maxYear
# print(work_with_dict({1231:[1,2],2222:[1111,2222]}))