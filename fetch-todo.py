import json, datetime

now = datetime.datetime(2025, 8, 11, 15, 47, 32, tzinfo=datetime.timezone(datetime.timedelta(hours=9)))
minute = now.minute  
todo_id = (minute % 60) + 1  

sample = {
    "note": "SAMPLE file for submission. The GitHub Action below will create the real file on each run.",
    "source_url": f"https://jsonplaceholder.typicode.com/todos/{todo_id}",
    "computed_from": {
        "timezone": "Asia/Seoul",
        "current_time": now.isoformat(),
        "current_minute": minute,
        "formula": "todo_id = (current_minute) + 1"
    },
    "placeholder_raw_response": {
        "userId": "…",
        "id": todo_id,
        "title": "… (fetched by the action at runtime)",
        "completed": "…"
    }
}

path = "/mnt/data/test.json"
with open(path, "w", encoding="utf-8") as f:
    json.dump(sample, f, ensure_ascii=False, indent=2)

path
