from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# HASH PASSWORD
def hash(password: str):
    return pwd_context.hash(password)

# COMPARE PASSWORD WITH HASHED PASSWORD
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)