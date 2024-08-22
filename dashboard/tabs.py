from dash import dcc, html
from dashboard.tables.table_of_samples_of_table_Generators import table_of_samples_of_table_Generators
from dashboard.tables.table_of_statistics_of_table_Generators import table_of_statistics_of_table_Generators
from dashboard.tables.table_of_visualizations_of_Nameplate_and_nominal_power_of_tables_Generators import \
    table_of_visualizations_of_Nameplate_and_nominal_power_of_tables_Generators
from dashboard.tables.table_of_visualizations_of_AC_Capacity_of_tables_Generators import \
    table_of_visualizations_of_AC_Capacity_of_tables_Generators
from dashboard.tables.table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID import \
    table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID
from dashboard.tables.table_of_visualizations_of_AP_to_Date_of_tables_Generators import \
    table_of_visualizations_of_AP_to_Date_of_tables_Generators

tab_Contracts = dcc.Tab(
    label = "Contracts",
    value = "Contracts"
)

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
    ]
)

details_with_table_of_visualizations_of_AP_to_Date_of_tables_Generators = html.Details(
    children = [
        html.Summary("Table Of Visualizations Of AP to Date Of Tables Generators"),
        table_of_visualizations_of_AP_to_Date_of_tables_Generators
    ]
)

details_with_table_of_visualizations_of_Nameplate_and_nominal_power_of_tables_Generators = html.Details(
    children = [
        html.Summary("Table Of Visualizations Of Nameplate / Nominal Power Of Tables Generators"),
        table_of_visualizations_of_Nameplate_and_nominal_power_of_tables_Generators
    ]
)

details_of_details_of_visualizations = html.Details(
    children = [
        html.Summary("Details Of Details Of Visualizations"),
        details_with_table_of_visualizations_of_AC_Capacity_of_tables_Generators,
        details_with_table_of_visualizations_of_AP_to_Date_of_tables_Generators,
        details_with_table_of_visualizations_of_Nameplate_and_nominal_power_of_tables_Generators
    ]
)

tab_Generators = dcc.Tab(
    label = "Generators",
    value = "Generators",
    children = [
        details_with_table_of_samples_of_table_Generators_Of_database,
        details_with_table_of_statistics_of_table_Generators_of_database,
        details_with_table_of_indices_of_rows_in_table_Generators_of_database_with_missing_GATS_ID,
        details_of_details_of_visualizations
    ]
)