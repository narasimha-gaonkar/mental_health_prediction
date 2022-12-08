import databaseMethods as dm
import pandas as pd
import constants as c
import numpy as np

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
    create_country_state_table()

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

def create_country_to_countryid_dictionary():
    countryid_dictionary = {}
    conn_norm = getDatabaseConnection()
    country_rows = dm.execute_sql_statement("SELECT * FROM Country", conn_norm)
    for i in country_rows:
        countryid_dictionary[i[1]] = i[0]
    return countryid_dictionary

def create_country_state_table():
    # Read the data from the csv file and create a list of tuples 
    # Insert the data into the table
    df = pd.read_csv(data_filename)
    countryid_dictionary = create_country_to_countryid_dictionary()
    uniqueCountryState = df[['Country','state']].values.tolist()
    for i in uniqueCountryState:
        if str(i[1]) == 'nan':
            i[1] = None
    uniqueCountryStateTuple = list(set([(countryid_dictionary[x[0]], x[1]) for x in uniqueCountryState]))
    uniqueCountryStateTuple = sorted(uniqueCountryStateTuple, key = lambda x:x[0])
    conn_norm = getDatabaseConnection()
    dm.create_table(conn_norm, c.COUNTRY_STATE_CREATE_TABLE_SQL)
    dm.execute_many_sql_statement(c.COUNTRY_STATE__INSERT_TABLE,uniqueCountryStateTuple,conn_norm)

def main():
    conn_norm = createDatabase()
    createTable()
    conn_norm.close()
main()