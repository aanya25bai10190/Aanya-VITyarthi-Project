# cycle_service.py
from models import get_cycle_data, get_symptom_data, parse_date
from datetime import date

CYCLE_DATA = get_cycle_data()
SYMPTOM_DATA = get_symptom_data()

def log_period(user_id, start_date_str, end_date_str):
    """Logs a new period entry (CREATE operation)."""
    try:
        start_date = parse_date(start_date_str)
        end_date = parse_date(end_date_str)
    except ValueError:
        return None, "Invalid date format. Use YYYY-MM-DD."
    
    # Stores [user_id, start_date, end_date]
    CYCLE_DATA.append([user_id, start_date, end_date])
    
    # Sorts data by start date (newest first)
    CYCLE_DATA.sort(key=lambda x: x[1], reverse=True)
    
    return start_date.isoformat(), "Period logged successfully"

def get_user_cycles(user_id):
    """Retrieves all cycle entries for a user."""
    # Returns [(start_date, end_date), ...]
    user_cycles = []
    for entry in CYCLE_DATA:
        if entry[0] == user_id:
            user_cycles.append((entry[1], entry[2]))
    return user_cycles

def log_symptom(user_id, date_str, symptom_type, intensity):
    """Logs a symptom for a specific date."""
    try:
        log_date = parse_date(date_str)
        intensity = int(intensity)
        if not 1 <= intensity <= 5: 
            return None, "Intensity must be between 1 and 5."
    except ValueError:
        return None, "Invalid date or intensity format."
        
    # Stores [user_id, date, symptom_type, intensity]
    SYMPTOM_DATA.append([user_id, log_date, symptom_type, intensity])
    
    return log_date.isoformat(), "Symptom logged successfully"

def get_user_symptoms(user_id):
    """Retrieves all symptom logs for a user."""
    user_symptoms = []
    for entry in SYMPTOM_DATA:
        if entry[0] == user_id:
            # Returns [(date, type, intensity), ...]
            user_symptoms.append((entry[1], entry[2], entry[3]))
    return user_symptoms