# inference.py

from dataload import load_task1_data
from task1_model import load_qwen_model, infer_one

def main():
    # 1. 데이터 로딩
    data = load_task1_data("task1_data.jsonl")
    print(f" 총 샘플 수: {len(data)}")

    # 2. 모델 로딩
    print(" Qwen 모델 로딩 중...")
    tokenizer, model = load_qwen_model()

    # 3. 첫 샘플에 대해 추론 수행
    question = data[0]["conversations"][0]["content"]
    print(f"\n 질문:\n{question}\n")

    response = infer_one(model, tokenizer, question)
    print(f"\n 응답:\n{response}")

if __name__ == "__main__":
    main()
