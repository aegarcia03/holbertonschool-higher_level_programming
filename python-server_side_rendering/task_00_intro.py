#!/usr/bin/python3
import sys, os, logging


def generate_invitations(template_content, attendees):
    if not isinstance(template_content, str):
        logging.error("Invalid template type: Expected a string")
        sys.exit()
    if not isinstance(attendees, list) or not all(not isinstance(attendee, dict) for attendee in attendees):
        logging.error("Invalid attendees type: Expected a list of dictionaries")
        sys.exit()
    
    if not template_content:
        logging.error("Template is empty, not output files generated")
        sys.exit()
    if not attendees:
        logging.error("No data provided, not output files generated")
        sys.exit()
    
    for index, attendee in enumerate(attendess, start=1):
        try:
            new_template = template_content.replace("name", attendee.get("name", "N/A"))
            new_template = new_template.replace("event_title", attendee.get("event_title", "N/A"))
            new_template = new_template.replace("event_date", attendee.get("event_date", "N/A"))
            new_template = new_template.replace("event_location", attendee.get("event_location", "N/A"))

            file_name = f"output_{index}.txt"

            if os.path.exists(file_name):
                raise Exception("File already exists")
            
            with open(file_name, 'w') as file:
                file.write(new_template)
        except Exception as error:
            print(f"{index}: {error}")
        

