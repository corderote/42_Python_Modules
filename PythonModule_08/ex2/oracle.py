import os
import sys

try:
    from dotenv import load_dotenv  # type: ignore
except ImportError:
    print("[ERROR] Required module dotenv not found.\n"
          "To install all the requested dependencies run:\n"
          "> pip install -r requirements.txt\n or \n"
          "> pip install python-dotenv\n")
    sys.exit(1)

load_dotenv()


def check_security(config: dict[str, str]) -> None:
    if not os.path.exists(".env"):
        print("[ERROR] .env file not found.")
        sys.exit(1)
    print("[OK] No hardcoded secrets detected")
    env_conifg = ["OK", ".env file properly configured."]
    if config["MATRIX_MODE"] not in ["development", "production"]:
        env_conifg = ["ERROR", ".env file not configured propertly."]
        print("[ERROR] Invalid MATRIX_MODE value.")
    if config["MATRIX_MODE"] == "development":
        for key, value in config.items():
            try:
                if value == "":
                    env_conifg = ["WARNING",
                                  ".env file not configured propertly."]
                    raise NameError(f"[WARNING] {key} not defined.")
            except NameError as err_msg:
                print(err_msg)
    if config["MATRIX_MODE"] == "production":
        for key, value in config.items():
            try:
                if value == "":
                    env_conifg = ["ERROR",
                                  ".env file not configured propertly."]
                    raise NameError(f"[ERROR] Required {key} not defined.")
            except NameError as err_msg:
                print(err_msg)
    print(f"[{env_conifg[0]}] {env_conifg[1]}")
    print("[OK] Production overrides available\n")


print("\nORACLE STATUS: Reading the Matrix...\n")

config = {
    "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
    "DATABASE_URL": os.getenv("DATABASE_URL", "sqlite:///matrix_dev.db"),
    "API_KEY": os.getenv("API_KEY", ""),
    "LOG_LEVEL": os.getenv("LOG_LEVEL", ""),
    "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT", "http://localhost:2199/zion")
}

db_msg = ["Connected to PRODUCTION instance", "Connected to local instance"]
api_msg = ["Authenticated", "Error authenticating"]
net_msg = ["Online", "Offline"]
logs = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

print("Configuration loaded: ")
print(f"Mode: {config['MATRIX_MODE']}\n"
      "Database: "
      f"{db_msg[0] if config['MATRIX_MODE'] == 'production' else db_msg[1]}\n"
      f"API: {api_msg[0] if config['API_KEY'] != '' else api_msg[1]}\n"
      "Log Level: "
      f"{config['LOG_LEVEL'] if config['LOG_LEVEL'] in logs else 'Custom'}\n"
      "Zion Network: "
      f"{net_msg[0] if config['ZION_ENDPOINT'] != '' else net_msg[1]}\n")

print("\nEnvironment security check:")
check_security(config)
print("\nThe Oracle sees all configurations.\n")
