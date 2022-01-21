cost = 24.95
disc = 40
shipping = 0.75
copies = 60
total = (1 - (disc/100)) * cost * copies + shipping * copies + 2.25
print(total)