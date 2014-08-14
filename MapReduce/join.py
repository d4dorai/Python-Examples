import MapReduce
import sys

"""
Problem 2 - Relational Join
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    orderId = record[1]
    mr.emit_intermediate(orderId, record)


def is_order(x):
    return x[0] == 'order'


def reducer(key, list_of_values):
    # key: orderId
    # value: list of record fields/values
    order_record = [x for x in list_of_values if is_order(x)][0]
    line_item_records = [x for x in list_of_values if not is_order(x)]
    for list_item_record in line_item_records:
        mr.emit(order_record + list_item_record)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
