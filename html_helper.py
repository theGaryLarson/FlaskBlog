# 3x3 matrix for testing
# my_data = [['header1', 'header2', 'header3'], ['test1', 'test2', 'test3'], ['test4', 'test5', 'test6']]


class Table:
    """Generates an html table and inserts the data from a python matrix.
    If your data has headers set header_row to True.

    :param row: total rows in table
    :param col: total columns in table
    :param data: a row by column matrix containing your data. (optional)
    :param header_row: Does the data contain a header row
    :param border_width:
    :return: None: stores the table in memory
    """
    def __init__(self, row, col, border_width, header_row, data=None):
        self.table_structure = []
        self.data = data
        self.border_width = border_width
        self.header_row = header_row
        if data:
            self.row = len(data)
            self.col = len(data[0])
        else:
            self.row = row
            self.col = col
        self.__make_table()

    def add_row(self, num_rows):
        if num_rows < 1:
            raise ValueError('rows added must be a positive number')
        self.row += num_rows
        self.__make_table()

    def add_col(self, num_cols):
        if num_cols < 1:
            raise ValueError('columns added must be a positive number')
        self.col += num_cols
        self.__make_table()

    def del_row(self, num_rows):
        if num_rows < 1:
            raise ValueError('rows added must be a positive number')
        if self.row - num_rows < 1:
            raise ValueError('The table cannot have 0 or negative rows ')
        self.row += -num_rows
        self.__make_table()

    def del_col(self, num_cols):
        if num_cols < 1:
            raise ValueError('columns added must be a positive number')
        if self.col - num_cols < 1:
            raise ValueError('The table cannot have 0 or negative columns ')
        self.col += -num_cols
        self.__make_table()

    # todo: add data to the existing data
    def add_data(self, data):
        # ensures all data is displayed in the table
        if self.row < len(data):
            self.row = len(data)
        if self.col < len(data[0]):
            self.col = len(data[0])
        self.data = data
        self.__make_table()

    def del_data(self):
        self.data = []
        self.__make_table()

    def print_table(self):
        for line in self.table_structure:
            print(line)

    def write_table(self, file_name, append):
        if append:
            append = 'a'
        else:
            append = 'w'
        with open(file_name, append) as html:
            for line in self.table_structure:
                html.write(line + '\n')

    def set_border_width(self, width):
        self.border_width = width
        self.__make_table()

    def get_table(self):
        return self.table_structure

    def __make_table(self):
        self.table_structure = []
        self.row_count = 0
        self.col_count = 0
        self.table_structure.append('<!--- border has been deprecated. But didn\'t feel its necessary to add css--->')
        self.table_structure.append(f"<table border={self.border_width}>")
        if self.header_row:
            self.table_structure.append("\t<tr>")
            for field in range(self.col):
                if self.data:
                    if self.row_count in range(len(self.data)) and self.col_count in range(len(self.data[0])):
                        self.table_structure.append(f"\t\t<th>{self.data[self.row_count][self.col_count]}</th>")
                    else:
                        self.table_structure.append("\t\t<th></th>")
                else:
                    self.table_structure.append("\t\t<th></th>")
                self.col_count += 1
            self.table_structure.append("\t</tr>")
            self.col_count = 0
            self.row_count = 1
        while self.row_count < self.row:
            self.table_structure.append("\t<tr>")
            while self.col_count < self.col:
                if self.data:
                    if self.row_count in range(len(self.data)) and self.col_count in range(len(self.data[0])):
                        self.table_structure.append(f"\t\t<td>{self.data[self.row_count][self.col_count]}</td>")
                    else:
                        self.table_structure.append("\t\t<td></td>")
                else:
                    self.table_structure.append("\t\t<td></td>")
                self.col_count += 1
            self.table_structure.append("\t</tr>")
            self.row_count += 1
            self.col_count = 0
        self.table_structure.append("</table>")
