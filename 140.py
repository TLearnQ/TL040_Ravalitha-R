
log_data = [
    "INFO: Connection successful",
    "ERROR: Timeout",
    "INFO: Retry"
]

audit = []       
errors = 0
processed = 0

for line in log_data:
    try:
        processed += 1
        
        if "ERROR" in line or "WARNING" in line:
            audit.append(line)
            errors += 1
    except Exception as e:
        audit.append(f"Failed to process line: {e}")

print("Audit Log:", audit)
print(f"Processed: {processed}, Alerts: {errors}")

