from dashboard.tables.table_of_samples_of_table_Generators import table_of_samples_of_table_Generators
from dashboard.tables.table_of_statistics_of_table_Generators import table_of_statistics_of_table_Generators
from dashboard.tables.table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID import table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID
from dashboard.class_Details import Details


details_with_table_of_samples_of_table_Generators = Details(
    summary = "Table Of Samples Of Table Generators",
    table = table_of_samples_of_table_Generators
)

details_with_table_of_statistics_of_table_Generators = Details(
    summary = "Table Of Statistics Of Table Generators",
    table = table_of_statistics_of_table_Generators
)

details_with_table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID = Details(
    summary = "Table Of Indices Of Rows In Table Generators With Missing GATS ID",
    table = table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID
)