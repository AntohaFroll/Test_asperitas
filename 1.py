import uuid
import time

def generate_data():
    username = uuid.uuid4().__str__().split("-")[-1]
    password = uuid.uuid1().__str__().split("-")[-1]
    text = uuid.uuid4().__str__().split("-")[-1]
    return {"username": username, "password": password, "text": text}

print(generate_data()["username"])
print(generate_data()["password"])
print(generate_data()["text"])
print(generate_data()["text"])