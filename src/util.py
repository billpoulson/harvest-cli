def parse_hours(hours_str):
    """Parse hours in H:MM format."""
    try:
        hours, minutes = map(int, hours_str.split(":"))
        return hours + minutes / 60.0
    except ValueError:
        raise ValueError("Invalid time format. Use H:MM format.")
