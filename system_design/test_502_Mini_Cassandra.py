"""
Cassandra is a NoSQL storage. The structure has two-level keys.

Level 1: raw_key. The same as hash_key or shard_key.
Level 2: column_key.
Level 3: column_value
raw_key is used to hash and can not support range query. let's simplify this to a string.
column_key is sorted and support range query. let's simplify this to integer.
column_value is a string. you can serialize any data into a string and store it in column value.

implement the following methods:

insert(raw_key, column_key, column_value)
query(raw_key, column_start, column_end) // return a list of entries
"""

"""
Definition of Column:
class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value
"""


class MiniCassandra:

    def __init__(self):
        # do intialization if necessary
        self.vals = {}

    """
    @param: raw_key: a string
    @param: column_key: An integer
    @param: column_value: a string
    @return: nothing
    """

    def insert(self, raw_key, column_key, column_value):
        # write your code here
        newdata = Column(column_key, column_value)
        if raw_key not in self.vals:
            self.vals[raw_key] = [newdata]
        else:
            val_row = self.vals[raw_key]
            lo, hi = 0, len(val_row) - 1
            while lo <= hi:
                mid = lo + (hi - lo) / 2
                if self.vals[raw_key][mid].key == column_key:
                    self.vals[raw_key][mid] = newdata
                    return
                elif self.vals[raw_key][mid].key > column_key:
                    hi = mid - 1
                else:
                    lo = mid + 1
            self.vals[raw_key].insert(lo, newdata)

    """
    @param: raw_key: a string
    @param: column_start: An integer
    @param: column_end: An integer
    @return: a list of Columns
    """

    def query(self, raw_key, column_start, column_end):
        # write your code here
        if raw_key in self.vals:
            return [i for i in self.vals[raw_key] \
                    if i.key >= column_start and i.key <= column_end]
        else:
            return []
