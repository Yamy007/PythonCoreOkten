# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи

def notebook() -> callable:
    list_task = []
    def add_task(todo: str) -> None:
        list_task.append(str(len(list_task)+1) + ' - ' +  todo )

    def get_all() ->None:
        print(list_task)

    return add_task, get_all


add, get  = notebook()

add('task-2')
add('task-3')
add('task-4')


get()



# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)

def expanded_form(num):
    return ' + '.join([digit + '0' * (len(str(num)) - i - 1) for i, digit in enumerate(str(num)) if digit!= 0 ])
   




# Приклад:

# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

print(expanded_form(765423554634))



# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# та буде виводити це значення після виконання функцій


def decor(func:callable) -> callable:
    count = 0

    def inner() ->None:
        nonlocal count
        func()
        count+=1
        print(count)
    return inner

@decor
def test():
    print("hello")


test()
test()
test()
test()
test()

@decor
def test2():
    print("gfdgdfg")


test2()
test2()
test2()
test2()