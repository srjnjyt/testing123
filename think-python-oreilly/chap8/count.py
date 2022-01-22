def count(word, letter):
    count = 0
    for lettr in word:
        if lettr == letter:
            count = count + 1
    return count

def main():
    w = input('enter a word: ')
    l = input('enter a letter: ')
    print(count(w, l))

if __name__ == "__main__":
    main()