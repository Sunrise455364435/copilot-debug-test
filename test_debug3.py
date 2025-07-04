def greet_user(user):
    return f"Hello, {user['name']}!"

print(greet_user({"email": "test@example.com"}))
