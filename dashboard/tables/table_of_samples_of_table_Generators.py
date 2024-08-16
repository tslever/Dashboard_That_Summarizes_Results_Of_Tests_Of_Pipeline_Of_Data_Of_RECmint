from dashboard.rows.row_with_samples_of_table_Generators import row_with_samples_of_table_Generators_of_database
from dashboard.Table import Table


list_of_rows = [
    row_with_samples_of_table_Generators_of_database
]


table_of_samples_of_table_Generators = Table(
    children = list_of_rows,
    width = 100
)