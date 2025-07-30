# dataload.py

import json

def load_task1_data(path="task1_data.jsonl"):
    """task1 jsonl 데이터를 리스트 형태로 반환"""
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            data.append(obj)
    return data