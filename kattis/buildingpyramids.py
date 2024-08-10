x = int(input())
layers = 0
k = 1

while x >= 0:
    layers += 1
    x -= k**2
    k += 2


print(layers-1)
