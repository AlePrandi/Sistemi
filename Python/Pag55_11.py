x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = x[0:(len(x)// 2) + 1]
z = x[(len(x)// 2 )+ 1:]
y.append(5)
print(y)