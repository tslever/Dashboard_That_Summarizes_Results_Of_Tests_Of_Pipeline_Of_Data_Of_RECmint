import json
import ndjson
import pandas as pd


class Loader():


    def __init__(self):
        self.path_to_data = "C:/Users/Tom/Documents/RecMint/data/"


    def count_columns_of_table_Generators_of_database_AirTable(self):
        maximum_number_of_keys = 0
        with open(self.path_to_data + "AirTable/Generators.ndjson", 'r') as file:
            for line in file:
                JSON_object = json.loads(line)
                number_of_keys = len(JSON_object.keys())
                if number_of_keys > maximum_number_of_keys:
                    maximum_number_of_keys = number_of_keys
        return maximum_number_of_keys
    

    def count_columns_of_table_Generators_of_database_RECBus(self):
        data_frame = pd.read_csv(
            filepath_or_buffer = self.path_to_data + "RECBus/Generators.csv",
            header = 0,
            nrows = 1
        )
        count = len(data_frame.columns)
        return count


    def count_rows_of_table_Generators_of_database_AirTable(self):
        count = 0
        with open(self.path_to_data + "AirTable/Generators.ndjson", 'r') as file:
            for line in file:
                count += 1
        return count
    

    def count_rows_of_table_Generators_of_database_AirTable_without_key_sysID(self):
        count = 0
        with open(self.path_to_data + "AirTable/Generators.ndjson", 'r') as file:
            for line in file:
                JSON_object = json.loads(line)
                if "sysID" not in JSON_object:
                    count += 1
        return count


    def count_rows_of_table_Generators_of_database_RECBus(self):
        data_frame = pd.read_csv(
            filepath_or_buffer = self.path_to_data + "RECBus/Generators.csv",
            header = 0
        )
        count = len(data_frame.index)
        return count
    

    def count_rows_of_table_Generators_of_database_RECBus_without_key_sysid(self):
        data_frame = pd.read_csv(
            filepath_or_buffer = self.path_to_data + "RECBus/Generators.csv",
            header = 0,
            nrows = 1
        )
        count = data_frame["sysid"].isna().sum()
        return count


    def create_excerpt_of_table_Generators_of_database_AirTable(self):
        data = []
        with open(self.path_to_data + "AirTable/Generators.ndjson", 'r') as file:
            for i, line in enumerate(file):
                if i == 1:
                    break
                data.append(json.loads(line))
        df = pd.DataFrame(data)
        df = df[sorted(df.columns)]
        return df


    def create_excerpt_of_table_Generators_of_database_RECBus(self):
        data_frame = pd.read_csv(
            filepath_or_buffer = self.path_to_data + "RECBus/Generators.csv",
            header = 0,
            nrows = 1
        )
        data_frame = data_frame[sorted(data_frame.columns)]
        return data_frame


    def create_list_of_values_in_column_Nameplate_of_table_Generators_of_AirTable(self) -> list:
        list_of_values_in_column_nameplate_of_table_Generators_of_AirTable = []
        with open(self.path_to_data + "AirTable/Generators.ndjson", 'r') as file:
            data = ndjson.load(file)
            for record in data:
                if "Nameplate (kW DC)" in record:
                    list_of_values_in_column_nameplate_of_table_Generators_of_AirTable.append(
                        record["Nameplate (kW DC)"]
                    )
        return list_of_values_in_column_nameplate_of_table_Generators_of_AirTable
    

    def create_list_of_values_in_column_nominal_power_of_table_Generators_of_RECBus(self) -> list:
        data_frame = pd.read_csv(
            filepath_or_buffer = self.path_to_data + "RECBus/Generators.csv",
            header = 0
        )
        return data_frame["nominal-power"].to_list()
    

loader = Loader()