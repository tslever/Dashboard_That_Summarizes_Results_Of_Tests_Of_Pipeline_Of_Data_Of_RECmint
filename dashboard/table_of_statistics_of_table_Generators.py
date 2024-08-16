from dashboard.rows.row_with_label_Statistics_For_Database import row_with_label_statistics_for_database
from dashboard.rows.row_with_counts_of_columns_of_table_Generators \
    import row_with_counts_of_columns_of_table_Generators
from dashboard.rows.row_with_counts_of_rows_in_table_Generators \
    import row_with_counts_of_rows_in_table_Generators
from dashboard.rows.row_with_counts_of_rows_in_table_Generators_missing_system_ID \
    import row_with_counts_of_rows_missing_system_ID
from dashboard.Table import Table


list_of_rows = [
    row_with_label_statistics_for_database,
    row_with_counts_of_columns_of_table_Generators,
    row_with_counts_of_rows_in_table_Generators,
    row_with_counts_of_rows_missing_system_ID
]


table_of_statistics_of_table_Generators_of_database = Table(
    children = list_of_rows,
    width = 100
)