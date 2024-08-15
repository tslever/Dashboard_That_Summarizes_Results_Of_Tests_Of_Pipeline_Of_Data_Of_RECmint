from row_with_names_of_databases import row_with_names_of_databases
from row_with_statistics_of_table_Generators_of_database import row_with_statistics_of_table_Generators_of_database
from Table import Table


list_of_rows = [
    row_with_names_of_databases,
    row_with_statistics_of_table_Generators_of_database
]


table_of_statistics_of_table_Generators_of_database = Table(
    children = list_of_rows,
    width = 100
)