def clean_null_values(data):
    cleaned_data= data.dropna()
    return cleaned_data

def drop_column(data,col):
    return data.drop(columns=col)

def clean_duplicates(data):
    cleaned_data=data.drop_duplicates()
    return cleaned_data
def clean_duplicates_col(data,col):
    cleaned_data = data.drop_duplicates(subset=[col])
    return cleaned_data
def total_null(data):
    return data.isnull().sum()

def clean_col_null(data,col):
    return data[data[col] != 0]