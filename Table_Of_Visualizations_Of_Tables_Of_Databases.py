from Row_With_Names_Of_Databases import Row_With_Names_Of_Databases
from Row_With_Graphs_Of_Frequency_Of_Energy_Vs_Energy import Row_With_Graphs_Of_Frequency_Of_Energy_Vs_Energy
from Table import Table


class Table_Of_Visualizations_Of_Tables_Of_Databases(Table):

    def __init__(self):

        children = [
            Row_With_Names_Of_Databases(),
            Row_With_Graphs_Of_Frequency_Of_Energy_Vs_Energy()
        ]

        super().__init__(children = children, width = 100)