# def is_leap(year):
#     leap = False
    
#     # Write your logic here

#     if 1900 <= year <= (10 ** 5):

#         if year % 4 == 0: #or year % 400 == 0:
#             leap = True
#             if year % 100 == 0:
#                 leap = False
#                 if year % 400 == 0:
#                     leap = True
#     return leap

# year = int(input())
# print(is_leap(year))

def myfunc(*args):
    even_numbers = []
    for num in args:
        if num%2==0:
            even_numbers.append(num)
        else:
            pass
    return even_numbers


if __name__ == "__main__":
    multiline = [2,1,3,4,6]
    print(myfunc(*multiline))

# args = [int(input().split(","))] 
# print(myfunc(*args))

# result = [int(num) for num in input("Enter numbers (separated by commas): ").split(",") if int(num) % 2 == 0]
# print(f"Even numbers: {result}")



