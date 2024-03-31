import math

def solve_cubic_equation(a, b, c, d):
    p = c / a - (b**2) / (3 * a**2)
    q = d / a + (2 * b**3) / (27 * a**3) - (b * c) / (3 * a**2)
    delta = (q**2) / 4 + (p**3) / 27

    if delta > 0:
        u = (-q / 2 + math.sqrt(delta))**(1 / 3)
        v = (-q / 2 - math.sqrt(delta))**(1 / 3)
        root = u + v
    elif delta == 0:
        u = (-q / 2)**(1 / 3)
        v = (-q / 2)**(1 / 3)
        root = u + v
    else:
        theta = math.acos(-q / (2 * math.sqrt(-(p**3) / 27)))
        u = 2 * math.sqrt(-p / 3) * math.cos(theta / 3)
        v = 2 * math.sqrt(-p / 3) * math.cos((theta + 2 * math.pi) / 3)
        w = 2 * math.sqrt(-p / 3) * math.cos((theta + 4 * math.pi) / 3)
        root = u, v, w

    return root

def solve_quartic_equation(a, b, c, d, e):
    p = (8 * a * c - 3 * b**2) / (8 * a**2)
    q = (b**3 - 4 * a * b * c + 8 * a**2 * d) / (8 * a**3)
    r = (-3 * b**4 + 256 * a**3 * e - 64 * a**2 * b * d + 16 * a * b**2 * c) / (256 * a**4)
    delta = (q**2 - 4 * p**3) / 27 + r**2 / 4

    if delta > 0:
        s = (r + math.sqrt(delta))**(1 / 3) if r >= 0 else -(abs(r) + math.sqrt(delta))**(1 / 3)
        t = (r - math.sqrt(delta))**(1 / 3) if r >= 0 else -(abs(r) - math.sqrt(delta))**(1 / 3)
        root1 = -b / (4 * a) - (s + t) / 2
        root2 = -b / (4 * a) + (s + t) / 2
        return root1, root2
    elif delta == 0:
        s = (r + math.sqrt(delta))**(1 / 3) if r >= 0 else -(abs(r) + math.sqrt(delta))**(1 / 3)
        t = (r - math.sqrt(delta))**(1 / 3) if r >= 0 else -(abs(r) - math.sqrt(delta))**(1 / 3)
        root1 = -b / (4 * a) - (s + t) / 2
        root2 = -b / (4 * a) + (s + t) / 2
        return root1,
    else:
        return "No real roots"

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root,
    else:
        return "No real roots"

def main():
    print("Choose the type of equation to solve:")
    print("1. Cubic Equation")
    print("2. Quartic Equation")
    print("3. Quadratic Equation")
    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        a = float(input("Enter the coefficient of x^3 (A): "))
        b = float(input("Enter the coefficient of x^2 (B): "))
        c = float(input("Enter the coefficient of x (C): "))
        d = float(input("Enter the constant term (D): "))
        roots = solve_cubic_equation(a, b, c, d)
        print("Roots of the cubic equation:", roots)
    elif choice == 2:
        a = float(input("Enter the coefficient of x^4 (A): "))
        b = float(input("Enter the coefficient of x^3 (B): "))
        c = float(input("Enter the coefficient of x^2 (C): "))
        d = float(input("Enter the coefficient of x (D): "))
        e = float(input("Enter the constant term (E): "))
        roots = solve_quartic_equation(a, b, c, d, e)
        print("Roots of the quartic equation:", roots)
    elif choice == 3:
        a = float(input("Enter the coefficient of x^2 (A): "))
        b = float(input("Enter the coefficient of x (B): "))
        c = float(input("Enter the constant term (C): "))
        roots = solve_quadratic_equation(a, b, c)
        print("Roots of the quadratic equation:", roots)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
