from util.table import export_csv, import_csv, int_table, print_table, create_data


# Create a table and read and write it
def test_create_data():
    table  = create_data(20,12)
    assert(len(table)==20)


# Create a table and read and write it
def test_write_csv():
    table  = create_data(20,12)
    tmp = '/tmp/data.csv'
    export_csv(tmp, table)


# Read a table from a file
def test_read_csv():
    table1  = create_data(20,12)
    table2 = import_csv('/tmp/data.csv')
    assert(len(table1)==len(table2))
    assert(table1==int_table(table2))
