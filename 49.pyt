from datetime import datetime

# Get current date and time
now = datetime.now()

# Extract individual components
date = now.date()
hours = now.hour
minutes = now.minute
seconds = now.second
milliseconds = now.microsecond // 1000  # Convert microseconds to milliseconds
nanoseconds = now.microsecond * 1000  # Convert microseconds to nanoseconds

# Print values
print(date, hours, minutes, seconds, milliseconds, nanoseconds)