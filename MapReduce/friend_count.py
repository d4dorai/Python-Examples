import MapReduce
import sys

"""
Problem 3 - Friend Count
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    personA = record[0]
    # personB = record[1]
    mr.emit_intermediate(personA, 1)


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    for v in list_of_values:
        total += v
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
