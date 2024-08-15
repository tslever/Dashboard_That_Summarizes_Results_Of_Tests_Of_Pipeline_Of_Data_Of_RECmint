import json
import ndjson
import pandas as pd


class Loader():

    def create_excerpt_of_table_Generators_of_database_AirTable(self):
        data = []
        with open("C:/Users/Tom/Documents/RecMint/data/AirTable/Generators.ndjson", 'r') as file:
            for i, line in enumerate(file):
                if i == 1:
                    break
                data.append(json.loads(line))
        df = pd.DataFrame(data)
        return df


    def create_excerpt_of_table_Generators_of_database_RECBus(self):
        return pd.read_csv(
            filepath_or_buffer = "C:/Users/Tom/Documents/RecMint/data/RECBus/Generators.csv",
            header = 0,
            nrows = 1
        )


    def create_list_of_values_in_column_Nameplate_of_table_Generators_of(self, name_of_database: str) -> list:

        list_of_values_in_column_nameplate_of_table_Generators_of_AirTable = []
        with open(f"C:/Users/Tom/Documents/RecMint/data/{name_of_database}/Generators.ndjson", 'r') as file:
            data = ndjson.load(file)
            for record in data:
                if "Nameplate (kW DC)" in record:
                    list_of_values_in_column_nameplate_of_table_Generators_of_AirTable.append(
                        record["Nameplate (kW DC)"]
                    )
        return list_of_values_in_column_nameplate_of_table_Generators_of_AirTable
    

loader = Loader()