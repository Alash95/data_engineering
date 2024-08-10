
# def regex_check(regex_number,regex):
#     regex = ['.','^', '$', '*', '+', '?', '{' '}', "[", "']'", '\\']
    
#     try:
#         pattern = regex_list[regex_number]
#         for char in pattern:
#             if char not in valid_chars:
#                 return False
#         return True
#     except IndexError:
#         return False
#     for string in range(regex.index()):
#         if 0 < regex_number < 100:
#             if string % 2 == 0:
#                 return True
#             return False  

# regex_number = int(input())
# regex = str(input())
# print(regex_check(regex_number))
# print()
# print(regex_check(regex))


def check_regex(regex :str):
    elements = regex.split("\n")
    print(elements)
    bound = int(elements[0])
    for i in range(0,bound):
        print(elements[i+1])
        if "\\" not in elements[i+1]:
            print(False)
        else:
            print(True)


if __name__ == "__main__":
    multiline = """2\n.*\+\n.*+"""
    check_regex(multiline)