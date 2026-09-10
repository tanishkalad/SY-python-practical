

status = input(
    "Enter atmospheric status (hot/cold/comfortable): "
).strip().lower()

if status == "hot":
    recommendation = "Turn on AC"
elif status == "cold":
    recommendation = "Activate heater"
elif status == "comfortable":
    recommendation = "Idle"
else:
    recommendation = "Unknown climate status - no action taken"


print("\n===== SMART HOME CLIMATE STATUS =====")
print(f"Atmospheric Status : {status.capitalize()}")
print(f"Hardware Action    : {recommendation}")
print("=====================================")
