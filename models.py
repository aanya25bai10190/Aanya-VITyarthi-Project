# models.py
from datetime import datetime
# In-memory 'Database' simulation using lists
# [user_id, username, password]
USER_DATA = []

# [user_id, start_date (datetime.date), end_date (datetime.date)]
CYCLE_DATA = [] 

# [user_id, date (datetime.date), symptom_type, intensity]
SYMPTOM_DATA = []

def get_user_data():
    '''Returns the list that stores the User's Credentials'''
    return USER_DATA

def get_cycle_data():
    '''Returns the list that stores Cycle Entries.'''
    return CYCLE_DATA

def get_symptom_data():
    '''Return the list that stores symptom logs.'''
    return SYMPTOM_DATA

def parse_date(date_str):
    '''This will convert YYYY-MM-DD string to datetime.date object.'''
    return datetime.strptime(date_str, "%Y-%m-%d").date()