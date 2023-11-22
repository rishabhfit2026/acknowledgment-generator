import random
import time

def generate_acknowledgment_number():
    timestamp = int(time.time())  # Get current timestamp
    random_component = random.randint(1000, 9999)  # Generate a random 4-digit number
    acknowledgment_number = f"{timestamp}-{random_component}"
    return acknowledgment_number

# Example usage:
acknowledgment_number = generate_acknowledgment_number()
print(f"Your acknowledgment number is: {acknowledgment_number}")
