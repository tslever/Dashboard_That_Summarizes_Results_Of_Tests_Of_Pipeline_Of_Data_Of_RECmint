from dashboard.Creator_Of_Rows import creator_of_rows
from dashboard.Table import Table


list_of_rows = [
    creator_of_rows.create_row_of_samples_of_table_Generators()
]


table_of_samples_of_table_Generators = Table(
    children = list_of_rows,
    width = 100
)