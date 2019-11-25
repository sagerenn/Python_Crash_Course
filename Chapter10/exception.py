try:
    print(5/6)
    # a=0
    # print(len(a))
    print(5/0)
    print(5/6)
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("some error!")


try:
    filename = 'alice.txt'

    with open(filename, encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print(f"The file {filename} is missing.")


print("input 'q' to quit")
while True:
    try:
        first_number = input("First number: ")
        if first_number == 'q':
            break
        second_number = input("Second number: ")
        if second_number == 'q':
            break
    except EOFError:
        print("The string is empty!")
        break

    try:
        anwser = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("The number divided cannot be zero!")
    except ValueError:
        print("Please input valid number!")
    except NameError:
        print("some number is not input!")
    else:
        print(anwser)

