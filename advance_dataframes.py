from env import user, password,host
import pandas as pd
import numpy as np
import datetime
from pydataset import data

#1 Create a function named get_db_url. It should accept a username, 
# hostname, password, and database name and return a url connection
#  string formatted like in the example at the start of this lesson.
def get_db_url(user,password,host,db_name):
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'


#2
url =  get_db_url(user,password,host, 'employees')

#3 a. sqlalchemy.exc.OperationalError:
  #b. qlalchemy.exc.ProgrammingError:


#4
# Read the employees 
# and titles tables into two separate DataFrames.
#df_employees = pd.read_sql('select * from employees', url)
#df_titles = pd.read_sql('select * from titles', url)

#5 rows ,columns
# df_employees.shape
# df_titles.shape

#6 summary stats
# df_employees.info()
# df_titles.info()


#7 
#print(len(df_titles['title'].drop_duplicates()))

#8
#print(df_titles['to_date'].min())


#9
#print(df_titles[df_titles['to_date'] < df_titles['to_date'].max()].to_date.max())


#excersise 2

#1
users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})


#2
merge  = users.merge(roles, on='id',how='right') #without nulls
print(merge)

#3
merge  = users.merge(roles, on='id',how='outer') #with nulls
print(merge)


#4
#users = users.drop(['id'])
#merge  = users.merge(roles, on='id',how='right') #not found in axis error
#print(merge)

#5
mpg = data('mpg')
print(mpg)

#6


#7
#print(mpg.shape)

#8
mpg = mpg.rename(columns={'cty': 'city','hwy':'highway', 'displ': 'displacement', 'trans':'transmission','cyl':'cylinder'})

#9
#print(mpg.info())
#print(mpg.describe())

#10
print(len(mpg['manufacturer'].drop_duplicates()))


#11
len(mpg['model'].drop_duplicates())

#12
mpg['mileage_difference'] = abs(mpg.highway - mpg.city)

#13
mpg['average_mileage'] = (mpg.highway + mpg.city)/2

#14
mpg['is_automatic'] = mpg['transmission'].str.contains('auto')

#15
best = mpg.groupby('manufacturer').average_mileage.mean().sort_values().nlargest(1, keep='all')
print(best)


#16
arg = (mpg[mpg['is_automatic'] == True])
auto = int(sum(arg.average_mileage)/len(arg.average_mileage))


arg = (mpg[mpg['is_automatic'] == False])
manual = int(sum(arg.average_mileage)/len(arg.average_mileage))


#exercise 3 
#1
url =  get_db_url(user,password,host, 'chipotle')
orders_df = pd.read_sql('select * from orders', url)

#2 total price for each order

















