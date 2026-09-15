# Поиск левой границы
x = 0
y = 0

while id(x) == id(y):
    x = x - 1
    y = y - 1

left_border = x + 1


# Поиск правой границы
x = 0
y = 0

while id(x) == id(y):
    x = x + 1
    y = y + 1

right_border = x - 1


M = -left_border
N = right_border

print("M =", M)
print("N =", N)
print("Диапазон:", left_border, "...", right_border)
