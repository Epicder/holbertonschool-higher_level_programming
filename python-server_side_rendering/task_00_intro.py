def generate_invitations(template, attendees):
    if not isinstance(template, str) or not isinstance(attendees, list):
        print("Wrong format.")
        return
    
    if not template.strip() or not attendees:
        print("no attendees dict.")
        return

    for i, attendee in enumerate(attendees, start=1):
        output_file = f"output_{i}.txt"
        output_content = template
        for key, value in attendee.items():
            output_content = output_content.replace("{" + key + "}", str(value) if value is not None else "N/A")
        with open(output_file, "w") as file:
            file.write(output_content)
        print(f"Generated output file {output_file}")
