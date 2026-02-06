import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files based on a template and a list of attendees.
    
    Args:
        template (str): The invitation template containing placeholders.
        attendees (list): A list of dictionaries containing attendee details.
    
    Returns:
        None
    """
    
    # **Check Input Types**
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # **Handle Empty Inputs**
    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # **Process Each Attendee and Generate Output**
    for index, attendee in enumerate(attendees, start=1):
        # Replace missing values with "N/A"
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")  # Handles None case
        event_location = attendee.get("event_location", "N/A")

        # Format the template with attendee data
        invitation_text = template.replace("{name}", name) \
                                  .replace("{event_title}", event_title) \
                                  .replace("{event_date}", str(event_date)) \
                                  .replace("{event_location}", event_location)

        # Define output file name
        output_filename = f"output_{index}.txt"

        # Write to file
        try:
            with open(output_filename, "w") as file:
                file.write(invitation_text)
            print(f"Generated: {output_filename}")
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
