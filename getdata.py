import requests

def load_task1_data(path="task1_data.jsonl"):

    url = "https://flock-fl-param.s3.amazonaws.com/36/training_set.jsonl?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASSFQ745NHQLBLUN4%2F20250729%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20250729T135936Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=8287395a7502d79e59039db5122699ec34632e4711f6733dc046ef2267561f50"
    # 대회 제공된 URL
    response = requests.get(url)

    with open(path, "wb") as f:
        f.write(response.content)

    return 