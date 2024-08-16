from dashboard.rows.row_with_counts_of_columns_of_table_Generators \
    import row_with_counts_of_columns_of_table_Generators
from dashboard.rows.row_with_counts_of_rows_in_table_Generators \
    import row_with_counts_of_rows_in_table_Generators
from dashboard.rows.row_with_counts_of_rows_in_table_Generators_missing_system_ID \
    import row_with_counts_of_rows_missing_system_ID
from dashboard.rows.row_with_label_Statistics_For_Database import row_with_label_Statistics_For_Database
from dashboard.rows.row_with_numbers_of_generators_in_database_that_do_not_correspond_to_generators_in_other_database \
    import row_with_numbers_of_generators_in_database_that_do_not_correspond_to_generators_in_other_database
from dashboard.Table import Table


list_of_rows = [
    row_with_label_Statistics_For_Database,
    row_with_counts_of_columns_of_table_Generators,
    row_with_counts_of_rows_in_table_Generators,
    row_with_counts_of_rows_missing_system_ID,
    row_with_numbers_of_generators_in_database_that_do_not_correspond_to_generators_in_other_database
]


table_of_statistics_of_table_Generators = Table(
    children = list_of_rows,
    width = 100
)