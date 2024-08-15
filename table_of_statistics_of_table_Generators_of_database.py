from row_with_label_statistics_for_database import row_with_label_statistics_for_database
from row_with_counts_of_columns_of_table_Generators_of_database \
    import row_with_counts_of_columns_of_table_Generators_of_database
from row_with_counts_of_rows_in_table_Generators_of_database \
    import row_with_counts_of_rows_in_table_Generators_of_database
from row_with_counts_of_rows_missing_sysID_and_sysid import row_with_counts_of_rows_missing_sysID_and_sysid
from Table import Table


list_of_rows = [
    row_with_label_statistics_for_database,
    row_with_counts_of_columns_of_table_Generators_of_database,
    row_with_counts_of_rows_in_table_Generators_of_database,
    row_with_counts_of_rows_missing_sysID_and_sysid
]


table_of_statistics_of_table_Generators_of_database = Table(
    children = list_of_rows,
    width = 100
)