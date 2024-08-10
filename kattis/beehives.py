def listToFloat(xs):
    return [float(x) for x in xs]


def test_case(mindis, numhiv):
    hives = []
    for i in range(numhiv):
        hives.append(listToFloat(input().split()))

    def hivecheck(a, b):
        dis2 = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        return dis2 <= mindis ** 2

    sweet = 0
    sour = 0
    for a in hives:
        soured = False
        for b in hives:
            if a is not b:
                if hivecheck(a, b):
                    soured = True
        if soured:
            sour += 1
        else:
            sweet += 1

    print(sour, "sour,", sweet, "sweet")


while True:
    mindis, numhiv = input().split()
    mindis = float(mindis)
    numhiv = int(numhiv)

    if mindis == 0.0 and numhiv == 0:
        break

    test_case(mindis, numhiv)
