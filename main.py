import pandas as pd
import Loading_file as ld
import Cleaning_file as cf
import Analysis as infoFile
import Visuals as vis

pd.set_option('display.max_columns',None)
data= ld.load_file()
print(data.head())

print("INFORMATION OF DATA")
print("\tData types")
print(infoFile.data_types(data))
print("\tDescribing all data")
print((infoFile.describe_data(data)))

#cleaning duplicate values from rank
print("\n\n\tCleaning Process of data")

print("Removing Rank duplicate values")
cleaned_data = cf.clean_duplicates_col(data,"rank")

print("Video Views 0 is useless hence dropping the zero values")
cleaned_data = cf.clean_col_null(data,'video views')

print("Removing Null values from Category")
cleaned_data = data[~data['category'].isna() & (data['category'].str.strip() != '')]

print("Dropping columns which are of no need")
cleaned_data=cf.drop_column(data, ["Longitude","Latitude","Urban_population","Population",
                                  "Gross tertiary education enrollment (%)","created_date","created_month",
                                  "lowest_monthly_earnings","highest_monthly_earnings","video_views_for_the_last_30_days",
                                  "channel_type_rank","Unemployment rate","subscribers_for_last_30_days"])

#Analysis on data using visuals

vis.barPlot(cleaned_data)
vis.scatterPlot(cleaned_data)
vis.countPlot(cleaned_data)
vis.barPlot_Category_views(cleaned_data)
vis.plot_scatter_with_regression(cleaned_data)

#DOWNLOADING THE CLEANED FILE
cleaned_data.to_excel("Data_sets\\cleaned_data.xlsx",index=False,engine="openpyxl")