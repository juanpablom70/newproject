"""
This file contains the logic to:

1. Create an user
2. Update user information
3. Get all users
4. Get user information
"""
import user_repository

def get_user(username):
    """
    """
    return user_repository.get_users(username)


def create_user(username, **kwargs):
    """
    """
    if user_repository.get_users(username):
        raise Exception(f"The user {username} already exists")
    
    if len(kwargs) != 3:
        raise Exception(f"The user information doesn't have the expected structure")

    
    cond = all([ kwargs.get(key) for key in ["name", "degree", "password"]])



    print(kwargs)



create_user("pepito",
            name="a",
            degree="asdas",
            password="gasd",
            alias="asd")