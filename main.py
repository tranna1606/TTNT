# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_name(name):
    for a in name:
        print(a)

def print_odd():
    for i in range(1,10):
        if i % 2 !=0:
            print(i)

def sum_range():
    sum =0
    i=0
    while i <=5:
        i += 1
        sum = sum +i
        print(sum)

    return sum

def print_dic():
    dic = {"a": 1, "b": 2, "c": 3,"d": 4}

    for key in dic.keys():
        print(key)

    for value in dic.values():
        print (value)

    for key,value in dic.items():
        print (key,value)


def print_tuples():
    # courses = [131, 141, 142, 212]
    # print("Maths {},Physic {}, Chems {}, Bio {}".format(*courses))
    a = (131,141,142,212)
    b = ("Maths","Physic","Chems","Bio")

    for i, x in enumerate(a):
        print (x, b[i])


def print_try():
    for a in range(-2,3):
        if (a == 0):
            print ("Can't divided by zero")
        else:
            try:
                print(10 / a)
            except:
                print(" Can't divide")

def sort_lamda():
    ages = [23, 10, 80]
    names = ["Hoa", "Lam", "Nam"]
    sorted_ages = sorted(ages, key=lambda x: x)
    print(sorted_ages)


    for i, x in enumerate(sorted_ages):
        print(x, names[i])

def create_file():
     with open('D:/readme.txt', 'w') as f:
        f.write('Create a new text file!')

def open_file():
    f = open("D:/readme.txt", "r")
    print(f.read())

def define_function(a,b):
    print(a+b)

def matrix_multi():


if __name__ == '__main__':
    #print_name("Tran Na")
    #print_odd()
    #sum_range()
    # print_dic()
    # print_tuples()
    # print_try()
    # sort_lamda()
    # create_file()
    # open_file()
    # define_function(3,4)
    matrix_multi()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
