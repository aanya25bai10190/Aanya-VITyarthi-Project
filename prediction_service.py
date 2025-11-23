# prediction_service.py
from cycle_service import get_user_cycles
from datetime import timedelta

def calculate_cycle_lengths(cycles):
    """Calculates the length of each recorded cycle in days."""
    # sorts the cycles
    sorted_cycles = sorted(cycles, key=lambda x: x[0]) 
    
    lengths = []
    # Calculates difference between each consecutive start date
    for i in range(len(sorted_cycles) - 1):
        start_date_1 = sorted_cycles[i][0]
        start_date_2 = sorted_cycles[i+1][0]
        length = (start_date_2 - start_date_1).days
        lengths.append(length)
        
    return lengths

def get_next_cycle_prediction(user_id):
    '''
    FR1: Calculates the next period and ovulation dates based on MCL.
    '''
    cycles = get_user_cycles(user_id)
    if len(cycles) < 2:
        return None, "Needs at least two cycle entries for prediction."
    
    cycle_lengths = calculate_cycle_lengths(cycles)
    
    if not cycle_lengths:
        return None, "Needs more completed cycle entries for average calculation."

    # Uses up to the last 6 completed cycle lengths
    relevant_lengths = cycle_lengths[-6:]
    
    # Calculates the Mean Cycle Length (MCL)
    mcl = round(sum(relevant_lengths) / len(relevant_lengths))
    
    # Last recorded period start date (newest entry in the full list)
    last_start_date = cycles[0][0]
    
    # Prediction: Next Start Date = Last Start Date + MCL
    predicted_start_date = last_start_date + timedelta(days=mcl)
    
    # Basic Fertility Window Prediction (Ovulation is 14 days before next period)
    ovulation_date = predicted_start_date - timedelta(days=14)
    
    return {
        'mcl': mcl,
        'predicted_start': predicted_start_date.isoformat(),
        'ovulation_date': ovulation_date.isoformat()
    }, "Prediction successful"