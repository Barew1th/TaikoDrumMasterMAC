import random
import json

notes = []
current_time = 1.0
for _ in range(20):
    note_type = random.choice(["don", "ka"])
    interval = random.uniform(0.3, 1.2)  # 每個音符間隔 0.3~1.2 秒
    current_time += interval
    notes.append({"time": round(current_time, 2), "type": note_type})

with open("chart.json", "w", encoding="utf-8") as f:
    json.dump(notes, f, ensure_ascii=False, indent=4)

