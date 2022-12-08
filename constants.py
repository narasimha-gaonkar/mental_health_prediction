NORMALIZED_DATABASE_FILENAME = 'normalized.db'
DATA_FILENAME = 'survey.csv'
DELEMETER = ','

GENDER_CREATE_TABLE_SQL = """CREATE TABLE IF NOT EXISTS [Gender] (
            [Gender] TEXT NOT NULL,
            [GenderCode] INTEGER NOT NULL
        );
        """
GENDER_INSERT_TABLE = '''INSERT INTO Gender (Gender, GenderCode) VALUES(?,?)'''


COUNTRY_CREATE_TABLE_SQL = """CREATE TABLE IF NOT EXISTS [Country] (
            [CountryID] INTEGER NOT NULL PRIMARY KEY,
            [Country] TEXT NOT NULL
        );
        """
COUNTRY_INSERT_TABLE = '''INSERT INTO Country (Country) VALUES(?)'''

COUNTRY_STATE_CREATE_TABLE_SQL = """CREATE TABLE IF NOT EXISTS [CountryState] (
            [CountryStateID] INTEGER NOT NULL PRIMARY KEY,
            [CountryID] TEXT NOT NULL,
            [State] TEXT,
            FOREIGN KEY (CountryID) REFERENCES Country(CountryID)
        );
        """
COUNTRY_STATE__INSERT_TABLE = '''INSERT INTO CountryState (CountryID, State) VALUES(?,?)'''

Gender = {
    "A little about you":	2,
    "Agender":	2,
    "All":	2,
    "Androgyne":	2,
    "Cis Female":	1,
    "Cis Male":	0,
    "Cis Man":	0,
    "Enby":	2,
    "F":	1,
    "Femake":	1,
    "Female ":	1,
    "Female (cis)":	1,
    "Female (trans)":	1,
    "Female":	1,
    "Genderqueer":	2,
    "Guy (-ish) ^_^":	0,
    "M":	0,
    "Mail":	0,
    "Make":	0,
    "Mal":	0,
    "Male ":	0,
    "Male (CIS)":	0,
    "Male":	0,
    "Male-ish":	0,
    "Malr":	0,
    "Man":	0,
    "Nah":	2,
    "Neuter":	2,
    "Trans woman":	2,
    "Trans-female":	2,
    "Woman":	1,
    "cis male":	1,
    "cis-female/femme":	1,
    "f":	1,
    "femail":	1,
    "female":	1,
    "fluid":	1,
    "m":	0,
    "maile":	0,
    "male leaning androgynous":	2,
    "male":	0,
    "msle":	0,
    "non-binary":	2,
    "ostensibly male":	2,
    "p":	2,
    "queer":	2,
    "queer/she/they":	1,
    "something kinda male?":	2,
    "woman":	1,
    'ostensibly male, unsure what that really means':	2,
}
