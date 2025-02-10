from datetime import datetime
import random

def get_current_time():
    return datetime.now().strftime("%H:%M:%S")

def generate_random_number(start, end):
    return random.randint(start, end)

def generate_otp_number():
    return random.randint(1000, 9999)