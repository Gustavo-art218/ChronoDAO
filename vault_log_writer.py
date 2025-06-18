import json
import subprocess
from datetime import datetime

log_file = "vault_log.json"

# Fetch latest commit details
commit = subprocess.check_output(
    ['git', 'log', '-1', '--pretty=format:%H|%an|%s|%ad'],
    universal_newlines=True
).strip()

commit_hash, author, message, timestamp = commit.split("|")

entry = {
    "hash": commit_hash,
    "author": author,
    "message": message,
    "timestamp": timestamp,
    "logged_at": datetime.utcnow().isoformat() + "Z"
}

try:
    with open(log_file, "w") as f:
    json.dump(entry, f, indent=4)
except:
    logs = []

logs.append(entry)

with open(log_file, "w") as f:
    json.dump(logs, f, indent=4)

print("📜 Vault updated with new Git commit.")
