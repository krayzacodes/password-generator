import random
import string

def generate_password(length):
    if length < 4:
        return "Password must be at least 4 characters long!"
    if length > 100:
        return "Password too long! Please choose less than 100 characters."
    
    #character pool: letters (upper.lower), digits, punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
# 🎨 Title block
print("=" * 35)
print("🔐 Strong Password Generator")
print("=" * 35)

try:
    user_length = int(input("Enter desired password length: "))
    result = generate_password(user_length)
    print(f"✅ Generated password: {result}")
except ValueError:
    print("⚠️ Please enter a valid number.")