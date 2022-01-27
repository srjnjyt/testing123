
def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

def main():
    fruit = 'bananab'
    print(is_palindrome(fruit))

if __name__ == "__main__":
    main()