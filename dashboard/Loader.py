import json
import numpy as np
import pandas as pd
from pyairtable import Api


class Loader():


    def __init__(self):
        with open("config.json", 'r') as file:
            config = json.load(file)
            self.data_frame_Generators_of_database_AirTable = self.load_table_Generators_of_AirTable()
            self.path_to_data = config.get("path_to_data")


    def count_columns_of_table_Generators_of_database_AirTable(self):
        maximum_number_of_keys = self.data_frame_Generators_of_database_AirTable.shape[1]
        return maximum_number_of_keys
    

    def count_columns_of_table_Generators_of_database_RECBus(self):
        data_frame = pd.read_csv(filepath_or_buffer = self.path_to_data + "RECBus/Generators.csv", header = 0, nrows = 1)
        count = len(data_frame.columns)
        return count


    def count_generators_in_AirTable_that_do_not_correspond_to_generators_in_RECBus(self):
        dictionary_of_sets_of_GATS_IDs_in_table_Generators = self._create_dictionary_of_sets_of_GATS_IDs_in_table_Generators()
        set_of_GATS_IDs_in_table_Generators_of_database_AirTable = dictionary_of_sets_of_GATS_IDs_in_table_Generators["set_of_GATS_IDs_in_table_Generators_of_database_AirTable"]
        set_of_GATS_IDs_in_table_Generators_of_database_RECBus = dictionary_of_sets_of_GATS_IDs_in_table_Generators["set_of_GATS_IDs_in_table_Generators_of_database_RECBus"]

        set_of_GATS_IDs_that_are_in_AirTable_Generators_but_not_RECBus_Generators = set_of_GATS_IDs_in_table_Generators_of_database_AirTable - set_of_GATS_IDs_in_table_Generators_of_database_RECBus
        count_of_GATS_IDs_that_are_in_AirTable_Generators_but_not_RECBus_Generators = len(set_of_GATS_IDs_that_are_in_AirTable_Generators_but_not_RECBus_Generators)
        return count_of_GATS_IDs_that_are_in_AirTable_Generators_but_not_RECBus_Generators
    

    def count_generators_in_RECBus_that_do_not_correspond_to_generators_in_AirTable(self):
        dictionary_of_sets_of_GATS_IDs_in_table_Generators = self._create_dictionary_of_sets_of_GATS_IDs_in_table_Generators()
        set_of_GATS_IDs_in_table_Generators_of_database_AirTable = dictionary_of_sets_of_GATS_IDs_in_table_Generators["set_of_GATS_IDs_in_table_Generators_of_database_AirTable"]
        set_of_GATS_IDs_in_table_Generators_of_database_RECBus = dictionary_of_sets_of_GATS_IDs_in_table_Generators["set_of_GATS_IDs_in_table_Generators_of_database_RECBus"]
        
        set_of_GATS_IDs_that_are_in_RecBus_Generators_but_not_AirTable_Generators = set_of_GATS_IDs_in_table_Generators_of_database_RECBus - set_of_GATS_IDs_in_table_Generators_of_database_AirTable
        count_of_GATS_IDs_that_are_in_RecBus_Generators_but_not_AirTable_Generators = len(set_of_GATS_IDs_that_are_in_RecBus_Generators_but_not_AirTable_Generators)
        return count_of_GATS_IDs_that_are_in_RecBus_Generators_but_not_AirTable_Generators


    def count_rows_in_table_Generators_of_database_AirTable_with_existing_GATS_ID_in_column_unit_id_of_table_Generators_of_database_RECBus(self):       
        data_frame_Generators_of_database_RECBus = pd.read_csv(filepath_or_buffer = self.path_to_data + "RECBus/Generators.csv", header = 0)
        filtered_data_frame = self.data_frame_Generators_of_database_AirTable[self.data_frame_Generators_of_database_AirTable["GATS ID"].notnull() & self.data_frame_Generators_of_database_AirTable["GATS ID"].isin(data_frame_Generators_of_database_RECBus["unit-id"])]
        count_of_rows_in_table_Generators_of_database_AirTable_with_existing_GATS_ID_in_column_unit_id_of_table_Generators_of_database_RECBus = len(filtered_data_frame)
        return count_of_rows_in_table_Generators_of_database_AirTable_with_existing_GATS_ID_in_column_unit_id_of_table_Generators_of_database_RECBus
    

    def count_rows_in_table_Generators_of_database_RECBus_with_existing_unit_id_in_column_GATS_ID_of_table_Generators_of_database_AirTable(self):
        data_frame_Generators_of_database_RECBus = pd.read_csv(filepath_or_buffer = self.path_to_data + "RECBus/Generators.csv", header = 0)
        data_frame_of_matching_rows = data_frame_Generators_of_database_RECBus[data_frame_Generators_of_database_RECBus["unit-id"].isin(self.data_frame_Generators_of_database_AirTable["GATS ID"])]
        count_of_matching_rows = len(data_frame_of_matching_rows)
        return count_of_matching_rows


    def count_rows_of_table_Generators_of_database_AirTable(self):
        return len(self.data_frame_Generators_of_database_AirTable)
    

    def count_rows_of_table_Generators_of_database_AirTable_without_key_GATS_ID(self):
        count_of_rows_of_table_Generators_of_database_AirTable_without_key_GATS_ID = len(self.list_indices_of_rows_in_table_Generators_of_database_AirTable_with_missing_GATS_ID())
        return count_of_rows_of_table_Generators_of_database_AirTable_without_key_GATS_ID


    def count_rows_of_table_Generators_of_database_RECBus(self):
        data_frame = pd.read_csv(filepath_or_buffer = self.path_to_data + "RECBus/Generators.csv", header = 0)
        count = len(data_frame.index)
        return count
    

    def count_rows_of_table_Generators_of_database_RECBus_without_key_unit_id(self):
        count_of_rows_of_table_Generators_of_database_RECBus_without_key_unit_id = len(self.list_indices_of_rows_in_table_Generators_of_database_RECBus_with_missing_unit_id())
        return count_of_rows_of_table_Generators_of_database_RECBus_without_key_unit_id


    def _create_dictionary_of_sets_of_GATS_IDs_in_table_Generators(self):
        data_frame_Generators_of_database_RECBus = pd.read_csv(filepath_or_buffer = self.path_to_data + "RECBus/Generators.csv", header = 0)
        set_of_GATS_IDs_in_table_Generators_of_database_AirTable = set(self.data_frame_Generators_of_database_AirTable["GATS ID"])
        set_of_GATS_IDs_in_table_Generators_of_database_RECBus = set(data_frame_Generators_of_database_RECBus["unit-id"])
        dictionary_of_sets_of_GATS_IDs_in_table_Generators = {
            "set_of_GATS_IDs_in_table_Generators_of_database_AirTable": set_of_GATS_IDs_in_table_Generators_of_database_AirTable,
            "set_of_GATS_IDs_in_table_Generators_of_database_RECBus": set_of_GATS_IDs_in_table_Generators_of_database_RECBus
        }
        return dictionary_of_sets_of_GATS_IDs_in_table_Generators
    

    def create_excerpt_of_table_Generators_of_database_AirTable(self):
        data_frame = self.data_frame_Generators_of_database_AirTable.head(n = 1)
        data_frame = data_frame[sorted(data_frame.columns)]
        return data_frame


    def create_excerpt_of_table_Generators_of_database_RECBus(self):
        data_frame = pd.read_csv(filepath_or_buffer = self.path_to_data + "RECBus/Generators.csv", header = 0, nrows = 1)
        data_frame = data_frame[sorted(data_frame.columns)]
        return data_frame


    def list_values_in_column_of_table_Generators(self, name_of_database: str, start_of_name_of_column: str) -> list:
        data_frame = None
        if name_of_database == "AirTable":
            data_frame = self.data_frame_Generators_of_database_AirTable
        elif name_of_database == "RECBus":
            data_frame = pd.read_csv(filepath_or_buffer = self.path_to_data + "RECBus/Generators.csv", header = 0)
        list_of_names_of_columns = [col for col in data_frame.columns if col.startswith(start_of_name_of_column)]
        name_of_column = list_of_names_of_columns[0]
        if name_of_column in ["Contract Term Length", "Locked Annuity Rate for Current Contract", "M&S - Fee%", "Year Contract Signed"]:
            data_frame[name_of_column] = data_frame[name_of_column].apply(lambda x: x[0] if isinstance(x, list) else x)
        if name_of_column in ["Average Cost/REC", "Year Contract Signed"] or name_of_column.startswith("TEMP - GenSync row mismatch (expected RECs"):
            data_frame[name_of_column] = data_frame[name_of_column].apply(lambda x: np.nan if x == {'specialValue': 'NaN'} else x)
        return data_frame[name_of_column].to_list()


    def list_indices_of_rows_in_table_Generators_of_database_AirTable_with_missing_GATS_ID(self):
        data_frame_of_rows_missing_GATS_ID = self.data_frame_Generators_of_database_AirTable[self.data_frame_Generators_of_database_AirTable["GATS ID"].isna() | (self.data_frame_Generators_of_database_AirTable["GATS ID"] == "")]
        list_of_indices_of_rows_with_missing_GATS_ID = data_frame_of_rows_missing_GATS_ID.index.to_list()
        return list_of_indices_of_rows_with_missing_GATS_ID
    

    def list_indices_of_rows_in_table_Generators_of_database_RECBus_with_missing_unit_id(self):
        data_frame_Generators_of_database_RECBus = pd.read_csv(filepath_or_buffer = self.path_to_data + "RECBus/Generators.csv")
        list_of_indices_of_rows_with_missing_unit_id = data_frame_Generators_of_database_RECBus[data_frame_Generators_of_database_RECBus["unit-id"].isna()].index.to_list()
        return list_of_indices_of_rows_with_missing_unit_id


    def list_DC_powers_in_AirTable_and_RECBus(self):
        data_frame_Generators_of_database_RECBus = pd.read_csv(self.path_to_data + "RECBus/Generators.csv")
        excerpt_of_data_frame_Generators_of_database_AirTable = self.data_frame_Generators_of_database_AirTable[["GATS ID", "Nameplate (kW DC)"]].rename(columns = {"Nameplate (kW DC)": "power"})
        excerpt_of_data_frame_Generators_of_database_RECBus = data_frame_Generators_of_database_RECBus[["unit-id", "nominal-power"]].rename(columns = {"nominal-power": "power"})
        unioned_excerpts = pd.concat([excerpt_of_data_frame_Generators_of_database_AirTable, excerpt_of_data_frame_Generators_of_database_RECBus]).drop_duplicates()
        list_of_powers_in_AirTable_and_RECBus = unioned_excerpts["power"].to_list()
        return list_of_powers_in_AirTable_and_RECBus
    

    def load_table_Generators_of_AirTable(self):
        personal_access_token_for_AirTable = None
        with open("credentials.json", 'r') as file:
            json_object_of_credentials = json.load(file)
            id_of_base_REC_Accounting = json_object_of_credentials.get("id_of_base_REC_Accounting")
            personal_access_token_for_AirTable = json_object_of_credentials.get("personal_access_token_for_AirTable")
        api = Api(personal_access_token_for_AirTable)
        table = api.table(base_id = id_of_base_REC_Accounting, table_name = "Generators")
        list_of_records = table.all()
        data = [record["fields"] for record in list_of_records]
        data_frame = pd.DataFrame(data)
        return data_frame


loader = Loader()