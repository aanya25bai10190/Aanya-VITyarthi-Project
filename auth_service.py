# auth_service.py
from models import get_user_data

USER_DATA = get_user_data()

def register_user(username, password):
    '''Registers a new User'''
    # Checking if user already exists
    for user_entry in USER_DATA:
        if user_entry[1] == username:
            return None, "User already exists"
    
    # Assigns a simple ID
    user_id = len(USER_DATA) + 1
    USER_DATA.append([user_id, username, password])
    
    return user_id, "Registration successful"

def login_user(username, password):
    """Logs in a user."""
    for user_entry in USER_DATA:
        # user_entry: [id, username, password]
        if user_entry[1] == username and user_entry[2] == password:
            return user_entry[0], "Login successful" # Returns the user_id
    
    return None, "Invalid username or password"

def get_username_by_id(user_id):
    """Retrieves username for display."""
    for user_entry in USER_DATA:
        if user_entry[0] == user_id:
            return user_entry[1]
    return "Unknown User"