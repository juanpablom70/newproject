"""
This file contains the logic to:

1. Create an user
2. Update user information
3. Get all users
4. Get user information
"""
import os
import json
from models.users import users

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_PATH, "user.json")

def load_users():
    """
    """
    global users
    f = open(JSON_PATH, "r")
    users = json.load(f)
    f.close()

    return users


def save_users(new_info):
    """
    """
    f = open(JSON_PATH, "w")
    json.dump(new_info,
              f,
              indent=4)
    f.close()


def get_users(username):
    """
    """
    return users.get(username)


def create_user(username, user_info):
    """
    """
    users[username] = user_info