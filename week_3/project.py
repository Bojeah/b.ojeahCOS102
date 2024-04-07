def quadratic(a, b, c):
    discriminant = (b ** 2) - (4.0 * a * c)

    if discriminant > 0:
        root_1 = round((-b + (((b ** 2) - (4.0 * a * c)) ** 0.5)) / (2 * a),2)
        root_2 = round((-b - (((b ** 2) - (4.0 * a * c)) ** 0.5)) / (2 * a),2)
        return root_1, root_2

    elif discriminant == 0:
        root_1 = -b / (2 * a)
        root_2 = -b / (2 * a)
        return root_1, root_2

    else:
        print("No real roots")


def cubic(a, b, c, d):
    q = ((3.0 * a * c) - (b ** 2)) / (9.0 * (a **2))
    r = ((9.0 * a * b * c) - (27.0 * d * (a ** 2)) - (2.0 * (b ** 3))) / (54 * (a ** 3))
    s = (r + (((q ** 3) + (r ** 2)) ** (0.5))) ** (1 / 3)
    t = (r - (((q ** 3) + (r ** 2)) ** (0.5))) ** (1 / 3)
    root_1 = (s + t) - (b / (3 * a))
    root_2 = (-1.0 * ((s + t) / 2.0)) - (b / (3.0 * a)) + (((3.0 ** (0.5)) * 1j / 2) * (s - t))
    root_3 = (-1.0 * ((s + t) / 2.0)) - (b / (3.0 * a)) - (((3.0 ** (0.5)) * 1j / 2) * (s - t))
    return root_1, root_2, root_3

pick = int(input("pick 1/2/3\n"))

if pick == 1:
    a = float(input("A = "))
    b = float(input("B = "))
    c = float(input("C = "))

    roots = quadratic(a, b, c)

    print("The roots are", roots)

elif pick == 2:
    a = float(input("A = "))
    b = float(input("B = "))
    c = float(input("C = "))
    d = float(input("D = "))

    roots = cubic(a, b, c, d)
    print("The roots are ", roots)

else:
    print("invalid input")