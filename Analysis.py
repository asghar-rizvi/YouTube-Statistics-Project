def data_types(data):
    print(data.dtypes)
def describe_data(data):
    print(data.describe())
def correlation_data(data):
    numeric_data = data.select_dtypes(include=[float, int])
    return numeric_data.corr()
def view_duplicates_value(data):
    print(data.duplicated().sum())


