from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.json
    if payload:
        print("🔔 GitHub push detected.")
        os.system("python vault_log_writer.py")
        print("📜 Vault log updated from GitHub.")
    return '', 200

if __name__ == '__main__':
    app.run(port=5001)
# Test webhook
