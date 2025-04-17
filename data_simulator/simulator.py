import json
import random
import time
from datetime import datetime
from faker import Faker

fake = Faker()

USERS = ['alice', 'bob', 'carol', 'dave']
EVENT_TYPES = ['login', 'logout', 'file_upload', 'file_download', 'file_delete']
STATUS = ['success', 'fail']
DEVICES = ['Windows10', 'Ubuntu', 'macOS', 'Android']

def generate_log(anomalous=False):
    user = random.choice(USERS)

    # normal ips vs ips de países aleatórios para simular anomalias
    ip_address = (
        fake.ipv4_public() if anomalous else fake.ipv4_private()
    )

    event_type = random.choice(EVENT_TYPES)

    log = {
        "timestamp": datetime.now().isoformat() + "Z",
        "user": user,
        "ip_address": ip_address,
        "event_type": random.choice(EVENT_TYPES),
        "status": random.choices(STATUS, weights=[0.9, 0.1])[0], # 90% success
        "location": fake.city(),
        "device": random.choice(DEVICES),
        "file_accessed": fake.file_name() if "file" in event_type else None,
        "anomalous": anomalous
    }
    return log


def simulate_stream(output_file="data/logs.json", interval=1.0):
    with open(output_file, 'a') as f:
        while True:
            # 10% de chance de gerar anomalia
            anomalous = random.random() < 0.1
            log = generate_log(anomalous)
            f.write(json.dumps(log) + "\n")
            print(f"[+] Generated log: {log}")
            time.sleep(interval)

if __name__ == "__main__":
    simulate_stream()