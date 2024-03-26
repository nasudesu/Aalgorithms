def check_balance(text):
    my_stack = []
    matches = 0
    counter = 0
    for i in text:
        if i == "(" or i == "{" or i == "[":
            my_stack.append(i)
        if i == ")" or i == "}" or i == "]":
            try:
                pre = my_stack.pop()
            except IndexError:
                return f"Match error at position {counter}"
            if pre + i == "()" or pre + i == "{}" or pre + i == "[]":
                matches += 1
            else:
                return f"Match error at position {counter}"
        counter += 1
    if my_stack.__len__() != 0: return f"Match error at position {counter - 1}"
    return f"Ok - {matches}"


input = input("Try: ")
print(check_balance(input))