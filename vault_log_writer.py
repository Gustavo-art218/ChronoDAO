import json
import subprocess
from datetime import datetime

log_file = "vault_log.json"

# Get the latest Git commit data
commit_hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("utf-8").strip()
author = subprocess.check_output(["git", "log", "-1", "--pretty=format:%an"]).decode("utf-8").strip()
message = subprocess.check_output(["git", "log", "-1", "--pretty=format:%s"]).decode("utf-8").strip()
timestamp = subprocess.check_output(["git", "log", "-1", "--pretty=format:%ct"]).decode("utf-8").strip()

entry = {
    "hash": commit_hash,
    "author": author,
    "message": message,
    "timestamp": timestamp,
    "logged_at": datetime.utcnow().isoformat() + "Z"
}

# Load existing logs
try:
    with open(log_file, "r") as f:
        logs = json.load(f)
        if isinstance(logs, dict):  # <-- YOUR OLD FILE WAS A DICT
            logs = [logs]           # Convert to list before appending
except:
    logs = []

# Add new entry
logs.append(entry)

# Write all logs back to file
with open(log_file, "w") as f:
    json.dump(logs, f, indent=4)

print("✅ Vault updated with new Git commit.")
