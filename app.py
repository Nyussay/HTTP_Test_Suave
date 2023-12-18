from fastapi import FastAPI

app = FastAPI()

data = {
    "water_visibility": [1.3, 3.213, 3.222, 2.333, 2.13, 2.144],
    "battery state": ["Normal", "Normal", "Normal", "Normal", "Normal", "Normal"],
    "remaining percentage": [98.00, 97.96, 97.60, 97.40, 97.10, 96.0]
}

@app.get("/monitor")
async def get_monitor_data():
    return data
