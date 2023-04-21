# import csv
# # with open('data/daily_sales_data_0.csv','r') as file:
# #     csv_reader=csv.reader(file)
# #     for row in csv_reader:
# #         print (row)

# #we first define the input and output paths of our data
# input_files = ['data/daily_sales_data_0.csv','data/daily_sales_data_1.csv','data/daily_sales_data_2.csv']
# output_file= 'output/sales.csv'

# product_name='Pink Morsels'

# # we will then define a dictionary to store the total sales for each date and region
# sales_by_date_region={}
# #looping over each of the input files
# for input_file in input_files:
#     with open (input_file, 'r') as file:
#         csv_reader = csv.DictReader(file)

#         for row in csv_reader:
#             if row['product']==product_name:
#                 sales=int (row['quantity'])*float(row['price'])
#                 # extracting the date and region from the row
#                 date=row[date]
  #              #   region=row[region]

#                 # adding the sales to the total for this date and region
                
#                 key = (date,region)
#                 if key in sales_by_date_region:
#                     sales_by_date_region+=sales
#                 else:
#                     sales_by_date_region=sales

                 


# # creating the csv writer in the output file

# with open(output_file,'w',newline='')as file:
#     fieldnames=['Sales','Date','Region']
#     csv_writer=csv.DictWriter(file,fieldnames=fieldnames)
#     csv_writer.writeheader()

#     for key, value in sales_by_date_region.items():
#         date,region=key
#         csv_writer.writerow({'Sales':value,'Date':date,'Region':region})

# import pandas as pd
import pandas as pd

# Read in the CSV files
df0 = pd.read_csv('data/daily_sales_data_0.csv', delimiter=',', encoding='utf-8')
df1 = pd.read_csv('data/daily_sales_data_1.csv', delimiter=',', encoding='utf-8')
dfn = pd.read_csv('data/daily_sales_data_2.csv', delimiter=',', encoding='utf-8')

# Concatenate the DataFrames vertically
frames = [df0, df1, dfn]
df = pd.concat(frames, axis=0, ignore_index=True)

# Filter the DataFrame to only include rows with Pink Morsels
df = df.loc[df['product'] == 'Pink Morsels']

# Combine the quantity and price columns into a new sales column
df['sales'] = df['quantity'] * df['price']

# Drop the quantity and price columns
df.drop(['quantity', 'price'], axis=1, inplace=True)

# Select only the columns we want in the output file
df = df[['sales', 'date', 'region']]

# Check if the DataFrame contains data
if df.shape[0] > 0:
    # Write the DataFrame to a CSV file
    df.to_csv('output.csv', index=False)
else:
    print("No data found in DataFrame.")


