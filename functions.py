"""Задания по ветвлениям, итерациям и вводу данных."""

# напиши функцию, которая принимает на вход любое
# количество чисел и сообщает, есть ли среди них чётное
def even_or_odd(a):
    if a % 2 == 0:
        print('Четное число')
    else:
        print('Нечентное число')
even_or_odd(500)


# используй тернарный оператор, чтобы вызвать функцию
# если возраст больше 21 года, в противном случае верни
# сообщение "Мы не продаём алкоголь несовершеннолетним."
age = 17
print("Мы не продаём алкоголь несовершеннолетним.") if age < 21 else sell_alcohol()


# напиши функцию, которая проверит, является ли строка ключевым словом в Питоне
# тебе понадобится модуль keyword, импортируй его и изучи с помощью dir()
def function_keyword():
    import keyword
    string = input()
    print('String is indeed a keyword in Python') if keyword.iskeyword(string) else print('String is not a keyword')
import keyword
print(keyword.kwlist)
function_keyword()

# напиши функцию, которая возвращает тип данных на русском языке:
# число, строка, булевый, None, список, кортеж, множество, словарь
# пример: get_type("что-то") возвращает "Это строка."
# пример2: get_type(42) возвращает "Это словарь."
def get_type(my_var):                  
    if type(my_var) == int:    
        return 'Это число'                   
    elif type(my_var) == bool: 
        return 'Это булевый'                  
    elif type(my_var) == str:  
        return 'Это строка'                   
    elif type(my_var) == list: 
        return 'Это список'                  
    elif type(my_var) == tuple:
        return 'Это кортеж'  
    elif type(my_var) == float:
        return 'Это число'           
    elif type(my_var) == set:
        return 'Это множество'   
    elif type(my_var) == dict:
        return 'Это словарь'               
    else: 
        print("Что это?")