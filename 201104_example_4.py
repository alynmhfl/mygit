#Program: Arrange and manipulate data using pandas module
import pandas as pd

year_index = { 'Year' :[y for y in range( 2010, 2031 )],'Index' :[i for i in range( 0, 21 )],}
df = pd.DataFrame(year_index)

#pandas.head() will print the first five data
print(df.head())
