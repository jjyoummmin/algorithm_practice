x = input()
result = " ".join([x[index:index+2] for index in list(range(0, len(x), 2))])
print(result)