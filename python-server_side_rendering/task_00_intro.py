import os

def generate_invitations(template, attendees):
    # 1. Check Input Types
    if not isinstance(template, str):
        print(f"Error: Invalid input type for template. Expected str, got {type(template).__name__}.")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print(f"Error: Invalid input type for attendees. Expected list of dictionaries, got {type(attendees).__name__}.")
        return

    # 2. Handle Empty Inputs
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Process Each Attendee
    for i, attendee in enumerate(attendees, start=1):
        processed_template = template
        
        # List of placeholders expected in the template
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for key in placeholders:
            # Get value from attendee dict, default to "N/A" if missing or None
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            
            # Use replace to swap {key} with the actual value
            processed_template = processed_template.replace(f"{{{key}}}", str(value))

        # 4. Generate Output Files
        filename = f"output_{i}.txt"
        
        # Check if file exists (as per hint) though 'w' overwrites anyway
        try:
            with open(filename, 'w') as f:
                f.write(processed_template)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
