import time

# TODO
operator = {
    '+': lambda : None, # добавить функцию сложения по готовности
    '-': lambda : None, # добавить функцию вычитания по готовности
    '*': lambda : None, # добавить функцию умножения по готовности
    '/': lambda : None, # добавить функцию деления по готовности
    '//': lambda : None, # добавить функцию деления без остатка по готовности
    '**': lambda : None, # добавить функцию степень по готовности
    '%': lambda : None, # добавить функцию процент числа по готовности
    '|': lambda : None, # добавить функцию остаток от деления по готовности
}

print("Консольный калькулятор")

# TODO
# оформить это в функцию

for i in range(22):
    print('-', end='')
    #time.sleep(0.3)

print()

while True:
    ans = input("Введите выражение (формат - num1 operator num2):")

    for i in ans:
        if i in operator:
            c = ans.find(i)
            print(operator[i](int(ans[:c]), int(ans[c+1:])))
            break
