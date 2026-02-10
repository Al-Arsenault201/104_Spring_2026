# in-class coding from Monday, February 9

if __name__ == "__main__":

    pi = 3.14159
    tau = 2 * pi
    print ("tau = ", tau)

    i_n = 1/3
    print("irrational number = ", i_n)

    y = 2.4**3.1
    print("y is ", y)

    alpha = 2
    beta = 3
    gamma = 4

    print("addition ", alpha + beta + gamma)
    print("subtraction", gamma - beta)
    print("multiplication", alpha * beta)

    print("division", gamma//beta)

    print("floating point division", gamma/beta)

    print("modulus", gamma%beta)
    
    #ask the user to enter a number
    #print out 3 times that number

    num = input("enter a number I'll print out that number tripled")

    # to fix the problem, we'll cast the number to an integer
    num = int(num)


    print("your answer is ", num*3)
    
