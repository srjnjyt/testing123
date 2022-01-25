def main():
    word = 'banana'
    index1 = word.find('an', 2)
    index2 = word.find('an', 1, 3)
    index3 = word.count('a')
    index4 = word.replace('a', 'e')
    print(index1, index2, index3, index4)

if __name__ == "__main__":
    main()
