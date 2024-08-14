import ndjson


def create_list_of_values_in_column_Nameplate_of_table_Generators_of(name_of_database: str) -> list:

    list_of_values_in_column_nameplate_of_table_Generators_of_AirTable = []
    with open(f"C:/Users/Tom/Documents/RecMint/data/{name_of_database}/Generators.ndjson", 'r') as file:
        data = ndjson.load(file)
        for record in data:
            if "Nameplate (kW DC)" in record:
                list_of_values_in_column_nameplate_of_table_Generators_of_AirTable.append(
                    record["Nameplate (kW DC)"]
                )
    return list_of_values_in_column_nameplate_of_table_Generators_of_AirTable