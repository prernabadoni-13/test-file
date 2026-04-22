import os

# TODO: fix authentication later
SECRET_KEY = "mysecretkey123"
DB_PASSWORD = "admin123"

def divide(a, b):
    return a / b

def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    print("Fetching user: " + str(user_id))
    return query

def process_list(items=[]):
    for i in range(0, len(items)+1):
        print(items[i])

def check_value(x):
    if x == None:
        return False
    if x > 0:
        if x > 10:
            if x > 100:
                return "big"
            else:
                return "medium"
        else:
            return "small"

try:
    result = divide(10, 0)
except:
    pass
