import json
import ndjson
import pandas as pd


class Loader():


    def __init__(self):
        self.path_to_data = "C:/Users/Tom/Documents/RecMint/data/"


    def list_indices_of_rows_in_table_Generators_of_database_AirTable_with_missing_sysID(self):
        list_representing_table_Generators_of_database_AirTable = None
        with open(self.path_to_data + "AirTable/Generators.ndjson", 'r') as file:
            list_representing_table_Generators_of_database_AirTable = ndjson.load(file)
        list_of_indices_of_rows_with_missing_sysID = []
        for i, row in enumerate(list_representing_table_Generators_of_database_AirTable):
            if "sysID" not in row or row["sysID"] is None or row["sysID"] == "":
                list_of_indices_of_rows_with_missing_sysID.append(i)
        return list_of_indices_of_rows_with_missing_sysID
    

    def list_indices_of_rows_in_table_Generators_of_database_RECBus_with_missing_sysid(self):
        data_frame_Generators_of_database_RECBus = pd.read_csv(
            filepath_or_buffer = self.path_to_data + "RECBus/Generators.csv"
        )
        list_of_indices_of_rows_with_missing_sysid = data_frame_Generators_of_database_RECBus[
            data_frame_Generators_of_database_RECBus["sysid"].isna()
        ].index.to_list()
        return list_of_indices_of_rows_with_missing_sysid


    def create_dictionary_of_sets_of_system_IDs_in_table_Generators(self):
        JSON_object_representing_table_Generators_of_database_AirTable = None
        with open(self.path_to_data + "AirTable/Generators.ndjson") as file:
            JSON_object_representing_table_Generators_of_database_AirTable = ndjson.load(file)
        data_frame_Generators_of_database_AirTable = pd.DataFrame(
            JSON_object_representing_table_Generators_of_database_AirTable
        )
        data_frame_Generators_of_database_RECBus = pd.read_csv(
            filepath_or_buffer = self.path_to_data + "RECBus/Generators.csv",
            header = 0
        )
        set_of_system_IDs_in_table_Generators_of_database_AirTable = \
            set(data_frame_Generators_of_database_AirTable["sysID"])
        set_of_system_IDs_in_table_Generators_of_database_RECBus = \
            set(data_frame_Generators_of_database_RECBus["sysid"])
        dictionary_of_sets_of_systems_IDs_in_table_Generators = {
            "set_of_system_IDs_in_table_Generators_of_database_AirTable": set_of_system_IDs_in_table_Generators_of_database_AirTable,
            "set_of_system_IDs_in_table_Generators_of_database_RECBus": set_of_system_IDs_in_table_Generators_of_database_RECBus
        }
        return dictionary_of_sets_of_systems_IDs_in_table_Generators


    def calculate_number_of_generators_in_AirTable_that_do_not_correspond_to_generators_in_RECBus(self):
        dictionary_of_sets_of_systems_IDs_in_table_Generators = \
            self.create_dictionary_of_sets_of_system_IDs_in_table_Generators()
        set_of_system_IDs_in_table_Generators_of_database_AirTable = \
            dictionary_of_sets_of_systems_IDs_in_table_Generators[
                "set_of_system_IDs_in_table_Generators_of_database_AirTable"
            ]
        set_of_system_IDs_in_table_Generators_of_database_RECBus = \
            dictionary_of_sets_of_systems_IDs_in_table_Generators[
                "set_of_system_IDs_in_table_Generators_of_database_RECBus"
            ]
        
        set_of_system_IDs_that_are_in_AirTable_Generators_but_not_RECBus_Generators = \
            set_of_system_IDs_in_table_Generators_of_database_AirTable - \
            set_of_system_IDs_in_table_Generators_of_database_RECBus
        number_of_system_IDs_that_are_in_AirTable_Generators_but_not_RECBus_Generators = \
            len(set_of_system_IDs_that_are_in_AirTable_Generators_but_not_RECBus_Generators)
        return number_of_system_IDs_that_are_in_AirTable_Generators_but_not_RECBus_Generators
    

    def calculate_number_of_generators_in_RECBus_that_do_not_correspond_to_generators_in_AirTable(self):
        dictionary_of_sets_of_systems_IDs_in_table_Generators = \
            self.create_dictionary_of_sets_of_system_IDs_in_table_Generators()
        set_of_system_IDs_in_table_Generators_of_database_AirTable = \
            dictionary_of_sets_of_systems_IDs_in_table_Generators[
                "set_of_system_IDs_in_table_Generators_of_database_AirTable"
            ]
        set_of_system_IDs_in_table_Generators_of_database_RECBus = \
            dictionary_of_sets_of_systems_IDs_in_table_Generators[
                "set_of_system_IDs_in_table_Generators_of_database_RECBus"
            ]
        
        set_of_system_IDs_that_are_in_RecBus_Generators_but_not_AirTable_Generators = \
            set_of_system_IDs_in_table_Generators_of_database_RECBus - \
            set_of_system_IDs_in_table_Generators_of_database_AirTable
        number_of_system_IDs_that_are_in_RecBus_Generators_but_not_AirTable_Generators = \
            len(set_of_system_IDs_that_are_in_RecBus_Generators_but_not_AirTable_Generators)
        return number_of_system_IDs_that_are_in_RecBus_Generators_but_not_AirTable_Generators


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