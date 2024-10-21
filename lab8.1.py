import numpy as np

# 1) Дії з масивом N
b = float(input("Введіть число b: "))
num_el = int(input("Введіть кількість елементів масиву N: "))

N = np.random.randint(0, b, num_el)
rounded_N = np.round(N)
print(f"\nМасив N з випадкових чисел: {rounded_N}")

# 2) Дії з масивом M
user_ints = input("\nВведіть цілі числа для масиву M: ")

# Заміна символів на пробіл та ділення цифр по рядках
user_ints = user_ints.replace(","," ").replace(";"," ").replace(".", " ")
user_ints = user_ints.split()
user_ints = [int(x) for x in user_ints]

# Сортування масиву M за спаданням
user_ints.sort(reverse=True)
print(f"\nВідсортований масив M за спаданням: {user_ints}")