def add_one(parameter):
    for i in range(len(parameter)):
        parameter[i] += 1
    print(parameter)
    # note that there is no return statement

if __name__ == '__main__':
    argument = [2,4,6, 8, 10]  #this is where the magic happens
    add_one(argument)
    print(argument)


