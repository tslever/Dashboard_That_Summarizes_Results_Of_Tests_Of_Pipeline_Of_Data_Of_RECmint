from dash import html
from dashboard.tables.table_of_samples_of_table_Generators \
    import table_of_samples_of_table_Generators
from dashboard.tables.table_of_statistics_of_table_Generators \
    import table_of_statistics_of_table_Generators
from dashboard.tables.table_of_visualizations_of_Nameplate_and_nominal_power_of_tables_Generators import \
    table_of_visualizations_of_Nameplate_and_nominal_power_of_tables_Generators
from dashboard.tables.table_of_visualizations_of_AC_Capacity_of_tables_Generators import \
    table_of_visualizations_of_AC_Capacity_of_tables_Generators
from dashboard.tables.table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID import \
    table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID
from dashboard.tables.table_of_visualizations_of_AP_to_Date_of_tables_Generators import \
    table_of_visualizations_of_AP_to_Date_of_tables_Generators
from dashboard.tables.table_of_visualizations_of_Average_Cost_Per_REC_of_tables_Generators import \
    table_of_visualizations_of_Average_Cost_Per_REC_of_tables_Generators
from dashboard.tables.table_of_visualizations_of_Count_Of_Contracts_vs_Count import \
    table_of_visualizations_of_Count_Of_Contracts_vs_Count
from dashboard.tables.table_of_visualizations_of_Count_Of_Generators_vs_Count import \
    table_of_visualizations_of_Count_Of_Generators_vs_Count


details_with_table_of_samples_of_table_Generators_Of_database = html.Details(
    children = [
        html.Summary("Table Of Samples Of Table Generators Of Database"),
        table_of_samples_of_table_Generators
    ]
)

details_with_table_of_statistics_of_table_Generators_of_database = html.Details(
    children = [
        html.Summary("Table Of Statistics Of Table Generators Of Database"),
        table_of_statistics_of_table_Generators
    ]
)

details_with_table_of_indices_of_rows_in_table_Generators_of_database_with_missing_GATS_ID = html.Details(
    children = [
        html.Summary("Table Of Indices Of Rows In Table Generators Of Database With Missing GATS ID"),
        table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID
    ]
)

details_with_table_of_visualizations_of_AC_Capacity_of_tables_Generators = html.Details(
    children = [
        html.Summary("Table Of Visualizations Of AC Capacity Of Tables Generators"),
        table_of_visualizations_of_AC_Capacity_of_tables_Generators
    ],
    style={"margin-left": "20px"}
)

details_with_table_of_visualizations_of_AP_to_Date_of_tables_Generators = html.Details(
    children = [
        html.Summary("Table Of Visualizations Of AP to Date Of Tables Generators"),
        table_of_visualizations_of_AP_to_Date_of_tables_Generators
    ],
    style={"margin-left": "20px"}
)

details_with_table_of_visualizations_of_Average_Cost_Per_REC_of_tables_Generators = html.Details(
    children = [
        html.Summary("Table Of Visualizations Of Average Cost Per REC Of Tables Generators"),
        table_of_visualizations_of_Average_Cost_Per_REC_of_tables_Generators
    ],
    style={"margin-left": "20px"}
)

details_with_table_of_visualizations_of_Nameplate_and_nominal_power_of_tables_Generators = html.Details(
    children = [
        html.Summary("Table Of Visualizations Of Nameplate / Nominal Power Of Tables Generators"),
        table_of_visualizations_of_Nameplate_and_nominal_power_of_tables_Generators
    ],
    style={"margin-left": "20px"}
)

details_with_table_of_visualizations_of_Count_Of_Contracts_of_tables_Generators = html.Details(
    children = [
        html.Summary("Table Of Visualizations Of Count Of Contracts Of Tables Generators"),
        table_of_visualizations_of_Count_Of_Contracts_vs_Count
    ],
    style={"margin-left": "20px"}
)

details_with_table_of_visualizations_of_Count_Of_Generators_of_tables_Generators = html.Details(
    children = [
        html.Summary("Table Of Visualizations Of Count Of Generators Of Tables Generators"),
        table_of_visualizations_of_Count_Of_Generators_vs_Count
    ],
    style={"margin-left": "20px"}
)

details_of_details_of_visualizations = html.Details(
    children = [
        html.Summary("Details Of Details Of Visualizations"),
        details_with_table_of_visualizations_of_AC_Capacity_of_tables_Generators,
        details_with_table_of_visualizations_of_AP_to_Date_of_tables_Generators,
        details_with_table_of_visualizations_of_Average_Cost_Per_REC_of_tables_Generators,
        details_with_table_of_visualizations_of_Count_Of_Contracts_of_tables_Generators,
        details_with_table_of_visualizations_of_Count_Of_Generators_of_tables_Generators,
        details_with_table_of_visualizations_of_Nameplate_and_nominal_power_of_tables_Generators
    ]
)