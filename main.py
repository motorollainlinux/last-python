def task1():
    Summ = 0
    NumsArr = []
    for i in range(10):
        NumsArr.append(int(input(f'Enter a {i+1} number:')))
    for i in range(10):
        Summ += NumsArr[i]
    print("Summ: ", Summ)
def task2():
    Words = []
    for i in range(6):
        Words.append(str(input(f'Enter a {i+1} string:')))
    for i in range(len(Words)-1, 0, -1):
        print(Words[i], end=' ')
    print()
def task3():
    NumsArr = []
    for i in range(10):
        NumsArr.append(int(input(f'Enter a {i+1} number:')))
    SmalNum = NumsArr[0]
    for i in range(10):
        if NumsArr[i] < SmalNum:
            SmalNum = NumsArr[i]
    print("SmalNum: ", SmalNum)
def task4():
    NumsArr = []
    for i in range(5):
        NumsArr.append(int(input(f'Enter a {i+1} number:')))
    for i in NumsArr:
        if i % 2 == 0:
            print(i, end=' ')
    print()
def task5():
    Multiply = 1
    NumsArr = []
    for i in range(5):
        NumsArr.append(int(input(f'Enter a {i+1} number:')))
    for i in range(5):
        Multiply *= NumsArr[i]
    print("Multiply: ", Multiply)
def task6():
    Words = []
    alphebet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(5):
        Words.append(str(input(f'Enter a {i+1} string:')).lower())
    for i in range(4):
        if Words[i][0] != Words[i+1][0] and alphebet.find(Words[i][0]) > alphebet.find(Words[i+1][0]):
            buff = Words[i]
            Words[i] = Words[i+1]
            Words[i+1] = buff
    for i in Words:
        print(i, end=" ")
    print()
def task7():
    Numbers = [12, 45, 79, 35, 27]
    BiggersNum = 0
    for i in Numbers:
        if i > BiggersNum:
            BiggersNum = i
    print("BiggersNum: ", BiggersNum)
def task8():
    Arr = [12, 30, "0x21345AF1274B10", "some text", 45, 90, task1, True, False]
    buff = Arr[0]
    Arr[0] = Arr[len(Arr)-1]
    Arr[len(Arr)-1] = buff
    print(Arr)
def task9():
    Maxim = 0
    Arr = [12, 30, 45, 32, -17, -28, -345, 21]
    for i in Arr:
        if abs(i) > Maxim:
            Maxim = abs(i)
    print("Maxim per module num: ", Maxim)
def task10():
    Arr = [12, 30, 45, 32, -17, -28, -345, 21]
    Summ = 0
    count = 0
    for i in Arr:
        if i > 0:
            Summ += i
            count += 1
    Summ /= count
    print("arithmetical mean of pasitiv nums: ", Summ)
def __main__():
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()
    task8()
    task9()
    task10()
if __name__ == "__main__":
    __main__()
    