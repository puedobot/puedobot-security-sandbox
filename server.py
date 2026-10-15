import os
import subprocess
import pickle

def run_backup(user_command: str):
    # CRITICAL: Remote Command Injection
    os.system("echo Backing up && " + user_command)

def load_session(serialized_data: bytes):
    # CRITICAL: Insecure Deserialization
    return pickle.loads(serialized_data)
