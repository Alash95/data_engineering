def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            return b
        else:
            return a
    elif a % 2 != 0 and b % 2 != 0:
        if a > b: 
            return a
        else:
            return b
    elif a % 2 == 0 and b % 2 !=0:
        return b
    elif a % 2 != 0 and b % 2 == 0:
        return a
    
if __name__ == "__main__":
    a = 2
    b = 4
    print(lesser_of_two_evens(a,b))
    a = 2
    b = 5
    print(lesser_of_two_evens(a,b))
    a = 5
    b = 3
    print(lesser_of_two_evens(a,b))
    a = 1
    b = 7
    print(lesser_of_two_evens(a,b))