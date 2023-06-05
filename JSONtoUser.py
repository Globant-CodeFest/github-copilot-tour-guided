class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


user = {
    "name": "John Doe",
    "email": "johndoe@gmail.com",
    "password": "password123"
}

# TODO: escriba una función que tome un json y devuelva una clase de usuario


def create_user(json):

    return User(json["name"], json["email"], json["password"])
