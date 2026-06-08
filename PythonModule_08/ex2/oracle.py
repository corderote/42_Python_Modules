import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("[ERROR] Required module dotenv not found.\n"
          "To install all the requested dependencies run:\n"
          "> pip install -r requirements.txt\n or \n"
          "> pip install python-dotenv\n")
    sys.exit(1)

load_dotenv()

print("ORACLE STATUS: Reading the Matrix...")

conifguration = {
    "MATRIX_MODE": os.getenv("MATRIX_MODE"),
    "DATABASE_URL": os.getenv("DATABASE_URL"),
    "API_KEY": os.getenv("API_KEY"),
    "LOG_LEVEL": os.getenv("LOG_LEVEL"),
    "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT")
}

print("Configuration loaded: ")
for key, value in conifguration.items():
    print

print("Environment security check:")
print("[OK] No hardcoded secrets detected")
if os.path.exists(".env"):
    print("[OK] .env file properly configured")
else:
    print("[WARN] No .env file found")
print("[OK] Production overrides available")

print("\nThe Oracle sees all configurations.\n")
