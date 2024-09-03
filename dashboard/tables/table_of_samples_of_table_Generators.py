from dashboard.Creator_Of_Row import creator_of_row
from dashboard.Table import Table


list_of_rows = [
    creator_of_row.create_row_of_samples_of_table_Generators()
]


table_of_samples_of_table_Generators = Table(
    children = list_of_rows,
    width = 100
)