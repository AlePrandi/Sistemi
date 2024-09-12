# si creano con il costruttore set
# si possono unire con |
# si possono prendere gli el comuni con &
a = set([1, 2, 3, 4])
b = set([3, 5, 6])

print(a | b)
print(a & b)
b.remove(5)
print(b)
