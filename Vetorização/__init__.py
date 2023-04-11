from pandas import DataFrame
from pprint import pprint
# from numpy import array
#
# Array = array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#

other_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

myDataFrame = DataFrame(other_array,
                        columns=['Coluna A', 'Coluna B', 'Coluna C'],
                        index=['Linha 1', 'Linha 2', 'Linha 3'],
                        )

pprint(myDataFrame)