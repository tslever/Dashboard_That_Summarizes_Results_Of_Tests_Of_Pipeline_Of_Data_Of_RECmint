from dash import dash_table, html
from dashboard.Table import Table
from dashboard.tables.table_of_samples_of_table_Generators import table_of_samples_of_table_Generators
from dashboard.tables.table_of_statistics_of_table_Generators import table_of_statistics_of_table_Generators
from dashboard.tables.table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID import table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID
from dashboard.Creator_Of_Table import create_of_table


class Details(html.Details):

    def __init__(self, summary: str, table: Table | dash_table.DataTable, indentation: int = None):

        super().__init__(
            children = [
                html.Summary(summary),
                table
            ],
            style = {} if indentation == None else {"margin-left": f"{indentation}px"}
        )


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

details_with_table_of_visualizations_of_AC_Capacity_of_table_Generators = Details(
    summary = "Table Of Visualizations Of AC Capacity Of Tables Generators",
    table = create_of_table.create_table_of_visualizations_of_quantity(quantity_in_AirTable = "AC Capacity (kW AC)", quantity_in_RECBus = "nominal-power-AC", log_should_be_applied = True),
    indentation = 20
)

details_with_table_of_visualizations_of_AP_to_Date_of_table_Generators = Details(
    summary = "Table Of Visualizations Of AP to Date Of Tables Generators",
    table = create_of_table.create_table_of_visualizations_of_quantity(quantity_in_AirTable = "AP to Date", quantity_in_RECBus = None, log_should_be_applied = True),
    indentation = 20
)

details_with_table_of_visualizations_of_Average_Cost_Per_REC_of_table_Generators = Details(
    summary = "Table Of Visualizations Of Average Cost Per REC Of Tables Generators",
    table = create_of_table.create_table_of_visualizations_of_quantity(quantity_in_AirTable = "Average Cost/REC", quantity_in_RECBus = None, log_should_be_applied = True),
    indentation = 20
)

details_with_table_of_visualizations_of_Count_Of_Contracts_of_table_Generators = Details(
    summary = "Table Of Visualizations Of Count Of Contracts Of Tables Generators",
    table = create_of_table.create_table_of_visualizations_of_quantity(quantity_in_AirTable = "COUNT - Contracts", quantity_in_RECBus = None, log_should_be_applied = False),
    indentation = 20
)

# Contract Term Length

details_with_table_of_visualizations_of_Count_Of_Generators_of_table_Generators = Details(
    summary = "Table Of Visualizations Of Count Of Generators Of Tables Generators",
    table = create_of_table.create_table_of_visualizations_of_quantity(quantity_in_AirTable = "Count - Gen Sync Not Computed", quantity_in_RECBus = None, log_should_be_applied = False),
    indentation = 20
)

details_with_table_of_visualizations_of_Number_Of_Lifetime_RECs_of_table_Generators = Details(
    summary = "Table Of Visualizations Of Number Of Lifetime RECs Of Tables Generators",
    table = create_of_table.create_table_of_visualizations_of_quantity(quantity_in_AirTable = "Lifetime RECs", quantity_in_RECBus = None, log_should_be_applied = True),
    indentation = 20
)

details_with_table_of_visualizations_of_Annuity_Rate_of_table_Generators = Details(
    summary = "Table Of Visualizations Of Annuity Rate Of Tables Generators",
    table = create_of_table.create_table_of_visualizations_of_quantity(quantity_in_AirTable = "Locked Annuity Rate for Current Contract", quantity_in_RECBus = None, log_should_be_applied = False),
    indentation = 20
)

details_with_table_of_visualizations_of_MS_of_table_Generators = Details(
    summary = "Table Of Visualizations Of MS Of Tables Generators",
    table = create_of_table.create_table_of_visualizations_of_quantity(quantity_in_AirTable = "M&S - Fee%", quantity_in_RECBus = None, log_should_be_applied = False),
    indentation = 20
)

details_with_table_of_visualizations_of_Nameplate_and_nominal_power_of_table_Generators = Details(
    summary = "Table Of Visualizations Of Nameplate And Nominal Power Of Tables Generators",
    table = create_of_table.create_table_of_visualizations_of_quantity(quantity_in_AirTable = "Nameplate (kW DC)", quantity_in_RECBus = "nominal-power", log_should_be_applied = True),
    indentation = 20
)

details_with_table_of_visualizations_of_Quantity_Of_Unpurchased_RECs_of_table_Generators = Details(
    summary = "Table Of Visualizations Of Quantity Of Unpurchased RECs Of Tables Generators",
    table = create_of_table.create_table_of_visualizations_of_quantity(quantity_in_AirTable = "Qty Unpurchased RECs", quantity_in_RECBus = None, log_should_be_applied = True),
    indentation = 20
)

details_with_table_of_visualizations_of_STT1_Revenue_of_tables_Generators = Details(
    summary = "Table Of Visualizations Of STT1 Revenue Of Tables Generators",
    table = create_of_table.create_table_of_visualizations_of_quantity(quantity_in_AirTable = "STT1 Revenue", quantity_in_RECBus = None, log_should_be_applied = False),
    indentation = 20
)

details_with_table_of_visualizations_of_Specific_Yield_of_tables_Generators = Details(
    summary = "Table Of Visualizations Of Specific Yield Of Tables Generators",
    table = create_of_table.create_table_of_visualizations_of_quantity(quantity_in_AirTable = "Specific Yield (given)", quantity_in_RECBus = None, log_should_be_applied = False),
    indentation = 20
)

details_with_table_of_visualizations_of_Number_Of_Mismatches_of_table_Generators = Details(
    summary = "Table Of Visualizations Of Number Of Mismatches Of Tables Generators",
    table = create_of_table.create_table_of_visualizations_of_quantity(quantity_in_AirTable = "TEMP - GenSync row mismatch (expected RECs", quantity_in_RECBus = None, log_should_be_applied = False),
    indentation = 20
)

details_with_table_of_visualizations_of_Calculated_Y1_RECs_of_table_Generators = Details(
    summary = "Table Of Visualizations Of Calculated Y1 RECs Of Tables Generators",
    table = create_of_table.create_table_of_visualizations_of_quantity(quantity_in_AirTable = "Y1 RECs (calc)", quantity_in_RECBus = None, log_should_be_applied = True),
    indentation = 20
)

details_with_table_of_visualizations_of_Year_Contract_Signed_of_table_Generators = Details(
    summary = "Table Of Visualizations Of Year Contract Signed Of Tables Generators",
    table = create_of_table.create_table_of_visualizations_of_quantity(quantity_in_AirTable = "Year Contract Signed", quantity_in_RECBus = None, log_should_be_applied = False),
    indentation = 20
)

details_with_table_of_visualizations_of_Zip_Code_of_table_Generators = Details(
    summary = "Table Of Visualizations Of Zip Code Of Tables Generators",
    table = create_of_table.create_table_of_visualizations_of_quantity(quantity_in_AirTable = "Zip Code", quantity_in_RECBus = None, log_should_be_applied = False),
    indentation = 20
)

details_with_table_of_visualizations_of_Modeled_Y1_RECs_of_table_Generators = Details(
    summary = "Table Of Visualizations Of Modeled Y1 RECs Of Tables Generators",
    table = create_of_table.create_table_of_visualizations_of_quantity(quantity_in_AirTable = "Modeled Y1 RECs", quantity_in_RECBus = None, log_should_be_applied = True),
    indentation = 20
)

details_with_table_of_visualizations_of_VA_LIQP_of_table_Generators = Details(
    summary = "Table Of Visualizations Of VA LIQP Of Tables Generators",
    table = create_of_table.create_table_of_visualizations_of_quantity(quantity_in_AirTable = "VA LIQP", quantity_in_RECBus = None, log_should_be_applied = False),
    indentation = 20
)

details_of_details_of_visualizations = html.Details(
    children = [
        html.Summary("Details Of Details Of Visualizations"),
        details_with_table_of_visualizations_of_AC_Capacity_of_table_Generators,
        details_with_table_of_visualizations_of_AP_to_Date_of_table_Generators,
        details_with_table_of_visualizations_of_Average_Cost_Per_REC_of_table_Generators,
        details_with_table_of_visualizations_of_Count_Of_Contracts_of_table_Generators,
        details_with_table_of_visualizations_of_Count_Of_Generators_of_table_Generators,
        details_with_table_of_visualizations_of_Number_Of_Lifetime_RECs_of_table_Generators,
        details_with_table_of_visualizations_of_Annuity_Rate_of_table_Generators,
        details_with_table_of_visualizations_of_MS_of_table_Generators,
        details_with_table_of_visualizations_of_Quantity_Of_Unpurchased_RECs_of_table_Generators,
        details_with_table_of_visualizations_of_Nameplate_and_nominal_power_of_table_Generators,
        details_with_table_of_visualizations_of_STT1_Revenue_of_tables_Generators,
        details_with_table_of_visualizations_of_Specific_Yield_of_tables_Generators,
        details_with_table_of_visualizations_of_Number_Of_Mismatches_of_table_Generators,
        details_with_table_of_visualizations_of_Calculated_Y1_RECs_of_table_Generators,
        details_with_table_of_visualizations_of_Year_Contract_Signed_of_table_Generators,
        details_with_table_of_visualizations_of_Zip_Code_of_table_Generators,
        details_with_table_of_visualizations_of_Modeled_Y1_RECs_of_table_Generators,
        details_with_table_of_visualizations_of_VA_LIQP_of_table_Generators
    ]
)