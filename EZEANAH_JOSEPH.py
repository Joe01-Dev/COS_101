def a():
    input1 = float(input("Enter your first digit"))
    input2 = float(input("Enter your second digit"))
    calculation = input1+input2
    print(calculation)

def b():
    mass = float(input("Enter your mass number"))
    velocity = float(input("Enter your velocity"))
    Momentum = mass * velocity
    print(Momentum)

def c():
    mass = float(input("Enter your mass number"))
    volume = float(input("Enter your volume"))
    Density = mass/volume
    print(Density)

def d():
    length = float(input("Enter your length"))
    breath = float(input("Enter your breath"))
    height = float(input("Eneter your height"))
    Volume = length * breath * height
    print(Volume)

def e():
    mass = float(input("Enter your mass number"))
    gravity = float(input("Enter your gravity"))
    Weight = mass * gravity
    print(Weight )


def main():
    user=input("what operation do you want to perform")
    if user == "a":
         a()
    elif user == "b":
        b()
    elif user == "c":
        c()
    elif user == "d":
        d()
    elif user == "e":
        e()
if __name__ == '__main__':
    main()



