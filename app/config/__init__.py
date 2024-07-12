import os.path

SECRET_KEY = os.urandom(24)

instance_folder = os.path.join(os.path.dirname(__file__), "..", "instance")
os.makedirs(instance_folder, exist_ok=True)


class Config:
    SECRET_KEY = SECRET_KEY

    DATABASE_FILE = os.path.join(instance_folder, "db.sqlite3")
    DATABASE = f"sqlite:///{DATABASE_FILE}"
