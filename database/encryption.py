import bcrypt


class Encryptor:
    @classmethod
    def hash_password(cls, encoded_password):
        return bcrypt.hashpw(encoded_password, bcrypt.gensalt())

    @classmethod
    def is_password_correct(cls, password, hashed):
        return bcrypt.checkpw(password.encode(), hashed.encode())
