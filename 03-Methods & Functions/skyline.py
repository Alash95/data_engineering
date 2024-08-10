def myfunc(letters: str):
    result = ''
    for i, letter in  enumerate(letters):
        print(i)
        if i % 2 == 0:
            result += letter.lower()
        else:
            result += letter.upper()
    return result

if __name__ == "__main__":
    letters = 'Anthropomorphism'
    print(myfunc(letters))