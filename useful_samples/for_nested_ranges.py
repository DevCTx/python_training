"""
    For with nested ranges
"""
val = [[i for  i  in  range(2)]  for  j  in  range(5)]
print(val)  # [[0, 1], [0, 1], [0, 1], [0, 1], [0, 1]]

val = [i for  i  in  range(2)  for  j  in  range(5)]
print(val)  # [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

val = [i for  j  in  range(5) for  i  in  range(2)]
print(val)  # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

val = [[i for  j  in  range(5)] for  i  in  range(2)]
print(val)  # [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1]]

val = [i for  i  in  range(2)  for  i  in  range(5)]
print(val)  # [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]

val = [i for  i  in  range(5)  for  i  in  range(2)]
print(val)  # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

val = [[i for  i  in  range(5)] for  i  in  range(2)]
print(val)  # [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]

val = [[i for  i  in  range(2)] for  i  in  range(5)]
print(val)  # [[0, 1], [0, 1], [0, 1], [0, 1], [0, 1]]

val = [i for  i  in  range(5)  for  j  in  range(2)]
print(val)  # [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]
