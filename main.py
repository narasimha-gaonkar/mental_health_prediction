import databaseMethods as dm
import pandas as pd
import constants as c


#Global variable 
normalized_database_filename = c.NORMALIZED_DATABASE_FILENAME
data_filename = c.DATA_FILENAME


# Create new database and  establish the connection
def createDatabase():
    return dm.create_connection(normalized_database_filename, True)

# Get Database connection
def getDatabaseConnection():
    return dm.create_connection(normalized_database_filename)

# Create Gender table
def createTable():
    create_gender_table()   
    create_country_table()

def create_gender_table():
    # Read the data from the csv file and create a list of tuples 
    # Insert the data into the table
    df = pd.read_csv(data_filename)
    uniqueGender = df['Gender'].unique().tolist()

    genderList = [(x, c.Gender[x]) for x in uniqueGender]
    genderList = sorted(genderList, key = lambda x:x[0])
    conn_norm = getDatabaseConnection()
    dm.create_table(conn_norm, c.GENDER_CREATE_TABLE_SQL)
    dm.execute_many_sql_statement(c.GENDER_INSERT_TABLE,genderList,conn_norm)

def create_country_table():
    # Read the data from the csv file and create a list of tuples 
    # Insert the data into the table
    df = pd.read_csv(data_filename)
    uniqueCountry = df['Country'].unique().tolist()

    uniqueCountryTuple = [(x, ) for x in uniqueCountry]
    uniqueCountryTuple = sorted(uniqueCountryTuple, key = lambda x:x[0])
    conn_norm = getDatabaseConnection()
    dm.create_table(conn_norm, c.COUNTRY_CREATE_TABLE_SQL)
    dm.execute_many_sql_statement(c.COUNTRY_INSERT_TABLE,uniqueCountryTuple,conn_norm)


def main():
    conn_norm = createDatabase()
    createTable()
    conn_norm.close()
main()