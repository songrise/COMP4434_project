import os

##############user rating table generation################
# SELECT * from rating
# WHERE user_id = 53698


def map_4(line):
    # assume each line is a record in database
    if line.user_id == 53698:
        emit(line, null)


def reduce_4(key, value_list):
    """each key corresponds to one line of data record of a paricular user"""
    # simply emit them for aggregation
    emit(key, null)

os.