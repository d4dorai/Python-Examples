import MapReduce
import sys

"""
Problem 6 - matrix mulitplication
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    matrix = record[0]
    i = record[1]
    j = record[2]
    val = record[3]
    if matrix == "a":
        key = (i, j)
    else:
        key = (j, i)
    mr.emit_intermediate(key, val)


def reducer(key, list_of_values):
    # print key, list_of_values
    if len(list_of_values) == 2:
        prod = list_of_values[0] * list_of_values[1]
    elif len(list_of_values) == 1:
        prod = list_of_values[0]
    else:
        prod = 0
    mr.emit((key[0], key[1], prod))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
