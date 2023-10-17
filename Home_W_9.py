N = int(input())
numbers = list(map(int, input().split()))

unique_numbers = set(numbers)
count = len(unique_numbers)

print(count)

                                       # Второе задание

# Ввод двух списков чисел
list1 = set(map(int, input().split()))
list2 = set(map(int, input().split()))

# Нахождение пересечения двух списков
intersection = list1 & list2

# Вывод количества чисел, содержащихся одновременно в обоих списках
print(len(intersection))
                                        # Задание третье

check = set()
arr = list(map(lambda x: int(x), input("NUMBERS: ").split(' ')))

for key in arr:
  is_yes = 'NO'
  if not (key in check):
    check.add(key)
  else: is_yes = 'YES'
  print(key, "Repeat: ", is_yes)