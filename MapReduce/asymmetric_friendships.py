import MapReduce
import sys

"""
Problem 4 - asymmetric friendships
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    personA = record[0]
    personB = record[1]
    mr.emit_intermediate((personA, personB), 1)
    mr.emit_intermediate((personB, personA), 0)


def reducer(key, list_of_values):
    if sum(list_of_values) == 0:
        mr.emit(key)
        mr.emit(tuple(reversed(key)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
