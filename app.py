# app_runner.py
from auth_service import register_user, login_user, get_username_by_id
from cycle_service import log_period, log_symptom, get_user_cycles, get_user_symptoms
from prediction_service import get_next_cycle_prediction
current_user_id = None

def run_auth_demo():
    """Handles basic registration and login."""
    global current_user_id
    
    print("\n--- CycleSync Authentication Demo ---")
    
    #Registers a user
    username = input("Enter username to register: ")
    password = input("Enter password: ")
    user_id, message = register_user(username, password)
    print(f"[{'SUCCESS' if user_id else 'ERROR'}] {message}")
    
    if user_id:
        #Logs the user in
        print("\n--- Attempting Login ---")
        login_user_id, login_message = login_user(username, password)
        if login_user_id:
            current_user_id = login_user_id
            print(f"[SUCCESS] Logged in as: {get_username_by_id(current_user_id)}")
            return True
    return False

def run_logging_demo():
    """Demonstrates FR1 & FR2: Logging Cycles and Symptoms with RECENT 2025 data."""
    global current_user_id
    
    if current_user_id is None:
        print("ERROR: Please log in first.")
        return

    user_name = get_username_by_id(current_user_id)
    print(f"\n--- Cycle/Symptom Logging Demo for User: {user_name} ---")
    log_period(current_user_id, "2025-08-20", "2025-08-25")
    log_period(current_user_id, "2025-09-20", "2025-09-24")
    log_period(current_user_id, "2025-10-20", "2025-10-24")
    print("3 recent cycles logged (simulating lengths: 31, 30 days).")
    print("\nLogging symptoms:")
    log_symptom(current_user_id, "2025-10-15", "Mood Swing", 3)
    log_symptom(current_user_id, "2025-10-20", "Cramps", 5)
    print("Symptoms logged.")
    print("\n--- Logged Data Summary ---")
    print(f"Cycles: {len(get_user_cycles(current_user_id))} entries.")
    print(f"Symptoms: {len(get_user_symptoms(current_user_id))} entries.")
    
def run_prediction_demo():
    """Demonstrates FR3: Prediction/Analytics (Calculated next date)."""
    print("\n--- Prediction & Analytics Demo ---")
    
    if current_user_id is None:
        print("ERROR: Please log in first.")
        return

    prediction, message = get_next_cycle_prediction(current_user_id)
    
    if prediction:
        print("[SUCCESS] Prediction Calculated (Based on 2025 data):")
        print(f"  Mean Cycle Length (MCL): {prediction['mcl']} days")
        print(f"  Predicted Next Period Start: {prediction['predicted_start']}")
        print(f"  Predicted Ovulation Date: {prediction['ovulation_date']}")
    else:
        print(f"[ERROR] {message}")

if __name__ == '__main__':
    # Start of the workflow
    if run_auth_demo():
        run_logging_demo()
        run_prediction_demo()
        print("\n--- Workflow Complete ---")