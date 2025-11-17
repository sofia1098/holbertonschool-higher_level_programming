import os 

def  generate_invitations(template, attendees):
    # template empty
    if template == "":
        print("Template is empty, no output files generated.")
        return

    # attendees empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # template must be str 
    if not isinstance(template, str):
        print("Invalid template type, expected a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(x, dict) for x in attendees):
        print("Invalid attendees data, expected a list of dictionaries.")
        return
    
    for idx, attendee in enumerate(attendees, start=1):
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        # replace placeholders
        fill = template.replace("{name}", name)
        fill = fill.replace("{event_title}", event_title)
        fill = fill.replace("{event_date}", event_date)
        fill = fill.replace("{event_location}", event_location)

        output_file = f"output_{idx}.txt"
    
        # Write to file
        try:
            with open(output_filename, "w") as f:
                f.write(fill)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
            continue
