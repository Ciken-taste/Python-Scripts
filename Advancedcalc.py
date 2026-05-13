

def add(num1: str, num2: str) -> float:
    return float(num1) + float(num2)


def subtract(num1: str, num2: str) -> float:
    return float(num1) - float(num2)


def multiply(num1: str, num2: str) -> float:
    return float(num1) * float(num2)


def divide(num1: str, num2: str) -> float:
    return float(num1) / float(num2)


def main(user_input) -> float:
    # Returns the calculated result from user_input
    user_input = user_input.split()
    if len(user_input) < 3:
        raise Exception("Bad input!")
    priority_list = user_input.copy()
    for i in range(len(user_input)):
        for j in range(len(user_input[i])):
            # Iterates through every character
            if user_input[i][j] in "+-":
                priority_list[i] = 1
            elif user_input[i][j] in "*/":
                priority_list[i] = 2
            elif user_input[i][j] in "()":
                priority_list[i] = 3
            else:
                if priority_list[i] != 3:
                    priority_list[i] = 0

    # Priority list is done, now we need to check for 2 number 3s in the prio list
    val_3s = []
    for i in range(len(user_input)):
        if priority_list[i] == 3:
            val_3s.append(i)
    if len(val_3s) >= 2:
        start = min(val_3s)
        end = max(val_3s)
        bracketed_expression = ""
        user_input[start] = user_input[start][1:]
        user_input[end] = user_input[end][:-1]
        while start <= end:
            bracketed_expression += user_input[start]
            bracketed_expression += " "
            start += 1
        iteration = 0
        start = min(val_3s)
        while start + iteration <= end:
            user_input.pop(end - iteration)
            iteration += 1
        user_input.insert(min(val_3s), main(bracketed_expression))

    # Value 2
    for i in range(len(user_input)):
        try:
            if priority_list[i] == 2 and priority_list[i - 1] == 0 and priority_list[i + 1] == 0:
                if user_input[i] == '*':
                    result = multiply(user_input[i - 1], user_input[i + 1])
                    for a in range(3):
                        user_input.pop(i + 1 - a)
                    user_input.insert(i - 1, result)
                elif user_input[i] == '/':
                    result = divide(user_input[i - 1], user_input[i + 1])
                    for a in range(3):
                        user_input.pop(i + 1 - a)
                    user_input.insert(i - 1, result)
        except IndexError:
            pass

    # Value 1
    for i in range(1, len(user_input)):
        try:
            if priority_list[i] == 1 and priority_list[i - 1] == 0 and priority_list[i + 1] == 0:
                if user_input[i] == '+':
                    result = add(user_input[i - 1], user_input[i + 1])
                    for a in range(3):
                        user_input.pop(i + 1 - a)
                    user_input.insert(i - 1, result)
                elif user_input[i] == '-':
                    result = subtract(user_input[i - 1], user_input[i + 1])
                    for a in range(3):
                        user_input.pop(i + 1 - a)
                    user_input.insert(i - 1, result)
        except IndexError:
            pass


    print(user_input)

    if len(user_input) == 1:
        return user_input[0]
    else:
        new_iteration = ""
        for i in range(len(user_input)):
            new_iteration += str(user_input[i])
            new_iteration += " "
        return main(new_iteration)


if __name__ == '__main__':
    assert main("5 * (6 - 1)") == 25, "Mathematical error"
    print("Supported expressions + - / *")
    print(main(input("Enter an mathematical expression separated by spaces: ")))