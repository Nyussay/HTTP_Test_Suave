# Start the FastAPI application using uvicorn
#uvicorn testing-local:app --host 0.0.0.0 --port 3000 --log-level debug
from fastapi import FastAPI
import random
from datetime import datetime, timedelta
import time

app = FastAPI()

# Set the timeout for 1 minute (60 seconds)
TIMEOUT_SECONDS = 260
timeout_start = None

runs = [] # The sequence of run, Initialize runs outside of the function

#replicated pipeline found - when the pipeline is found return [], so for next round the timeout will reset to research pipeline
@app.get("/reset_timeout")
def reset_timeout():
    #for timeout - to replicate the pipe is founded
    global timeout_start 
    timeout_start = datetime.now()
    #recont the loop to zero
    global runs 
    runs = [] 
    return timeout_start

@app.get("/monitor")
async def get_monitor_data():
    print(datetime.now()) # Check if the timeout has been reached
    
    water_visibility = []
    
    '''
    #REPLICATE MEHDI SEQUENCE
    global runs  # Use the global variable
    if len(runs) >= 8 and runs[-1] == 8:
    # Reset water visibility after the 8th run
        runs = []
        return {
            "water_visibility": water_visibility,
            "battery state": [],
            "remaining percentage": []
        }
    #REPLICATE MEHDI SEQUENCE
    '''
        
    #replicated pipeline found - when the pipeline is found return []
    if timeout_start and (datetime.now() - timeout_start).total_seconds() >= TIMEOUT_SECONDS:
        return {
            "water_visibility": water_visibility,
            "battery state": [],
            "remaining percentage": []
        }
        
    
    # Step 1: Generate a random range between 1, 2, 3 - For Water Visibility
    random_range = random.randint(1, 3)

    # Step 2: Change the water_visibility values based on the random range
    if random_range == 1:
        water_visibility = [random.uniform(1.0, 1.999) for _ in range(6)]
    elif random_range == 2:
        water_visibility = [random.uniform(2.0, 2.999) for _ in range(6)]
    elif random_range == 3:
        water_visibility = [random.uniform(3.0, 3.999) for _ in range(6)]
    else:
        raise ValueError("Invalid random range")
    '''
    
    #REPLICATE MEHDI SEQUENCE
    # Step 1: Determine the range for water_visibility based on the run number
    # Check if the runs list is empty (first run)
    if not runs:
        runs = [1]
    else:
        run_number = runs[-1] + 1

        if run_number % 3 == 0:
            # Range between 2.5-3 for 1st, 4th, 7th, ... run
            water_visibility = [random.uniform(2.5, 3.5) for _ in range(6)]
        elif run_number % 3 == 1:
            # Range between 1.6-2.4 for 2nd, 5th, 8th, ... run
            water_visibility = [random.uniform(1.6, 2.4) for _ in range(6)]
        elif run_number % 3 == 2:
            # Range between 1-1.4 for 3rd, 6th, 9th, ... run
            water_visibility = [random.uniform(0.5, 1.4) for _ in range(6)]
        else:
            raise ValueError("Invalid run number")

        # Store the run information for the next run
        runs.append(run_number)
    #REPLICATE MEHDI SEQUENCE
    '''
    
    #Step 3 : Define battery Status
    battery_state = ["Normal", "Normal", "Normal", "Normal", "Normal", "Normal"] #Normal
    #battery_state = ["Normal", "Normal", "Normal", "Not Normal", "Normal", "Normal"] #Not Normal
    
    #Step 3 : Define percentage Status
    remaining_percentage = [98.00, 97.96, 97.60, 97.40, 97.10, 96.0] #Full
    #remaining_percentage = [14.50, 13.96, 13.60, 13.40, 12.10, 11.0] #10-15%
    #remaining_percentage = [4.00, 3.96, 3.60, 3.40, 2.10, 2.0] #<5%

    data = {
        "water_visibility": water_visibility,
        "battery state": battery_state,
        "remaining percentage": remaining_percentage
    }
    
    print(data)
    
    return data



@app.put("/execute")
async def execute_mode(payload: dict):
    mode = payload.get("mode")
    if mode >= -1 and mode <=3:
        # Perform actions for mode 1
        print("/execute" + str(mode))
        return True
    else:
        # Return False for other modes or invalid values
        print("Invalid /execute" + str(mode))
        return False



@app.get("/adaptation_options")
async def get_adaptation_options():
    options = {
        "mode": {
            "Afloat": -1,
            "Random": 0,
            "Low": 1,
            "Medium": 2,
            "High": 3
        }
    }
    return options
