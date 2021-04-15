class qudratic_equation:
    def __init__(self):
        try:
            print("please insert the cofficent of a")
            valueof_a = int(input())
            print("please insert the cofficent of b")
            valueof_b = int(input())
            print("please insert the cofficent of c")
            valueof_c = int(input())
            solution_checker = valueof_b ** 2 - (4 * valueof_a * valueof_c)
        except:
            print("please enter only number")
        if solution_checker == 0:
            print(for_one_root(valueof_a, valueof_b, valueof_c))
        elif solution_checker > 0:
            print(for_two_root(valueof_a, valueof_b, valueof_c))
        elif solution_checker < 0:
            print(for_no_root(valueof_a, valueof_b, valueof_c))


def for_two_root(valueof_a, valueof_b, valueof_c):
    if valueof_b ** 2 - (4 * valueof_a * valueof_c) > 0:
        root1 = ((- valueof_b) + (valueof_b ** 2 - (4 * valueof_a * valueof_c))) / 2 * valueof_a
        root2 = ((- valueof_b) + (valueof_b ** 2 - (4 * valueof_a * valueof_c))) / 2 * valueof_a
        roots = [root1, root2]
        print("The Equation Has two real roots : ")
        print(roots)
        return True
    else:
        print("the equation has not exactly one root")
        return False


def for_one_root(valueof_a, valueof_b, valueof_c):
    if valueof_b ** 2 - (4 * valueof_a * valueof_c == 0):
        root1 = -valueof_b / 2 * valueof_a
        print("The Equation Has one real root : ")
        print(root1)
        return True
    else:
        print("the equation has not exactly one root")
        return False


def for_no_root(valueof_a, valueof_b, valueof_c):
    if valueof_b ** 2 - (4 * valueof_a * valueof_c < 0):
        print("There is no real root")
        return True
    else:
        print("the equation has real root")
        return False

# qudratic_equation()
