from dash import dash_table
import pandas as pd


class Sample(dash_table.DataTable):

    def __init__(
        self,
        data_frame: pd.DataFrame,
        id: str
    ):

        for name_of_column in data_frame.columns:
            data_frame[name_of_column] = data_frame[name_of_column].map(
                lambda element: str(element) if isinstance(element, (dict, list)) else element
            )

        data_frame_of_elements_in_first_row = data_frame.iloc[0].to_frame()
        data_frame_of_values_and_elements_in_first_row = data_frame_of_elements_in_first_row.reset_index()
        data_frame_of_indices_values_and_elements_in_first_row = data_frame_of_values_and_elements_in_first_row.reset_index()
        data_frame_of_indices_values_and_elements_in_first_row.columns = ["Index", "Value", "Row 0"]

        super().__init__(
            id = id,
            columns = [{"name": name_of_column, "id": name_of_column} for name_of_column in data_frame_of_indices_values_and_elements_in_first_row],
            data = data_frame_of_indices_values_and_elements_in_first_row.to_dict("records"),
            style_cell = {
                "max-width": "0px",
                "white-space": "break-spaces"
            }
        )