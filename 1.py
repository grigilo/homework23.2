import random
import string


def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(10))
    return password


generated_password = generate_password()
print("Ваш сгенерированный пароль:", generated_password)
