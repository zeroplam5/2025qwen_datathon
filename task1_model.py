# task1_model.py

from transformers import AutoTokenizer, AutoModelForCausalLM

def load_qwen_model(model_id="Qwen/Qwen2.5-7B-Instruct"):
    """Qwen 모델과 토크나이저 로딩 (GPU 자동 할당)"""
    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        device_map="auto",
        trust_remote_code=True
    )
    return tokenizer, model

def infer_one(model, tokenizer, prompt, max_new_tokens=200):
    """Qwen 모델에 단일 질문(prompt)을 넣어 답변 생성"""
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=max_new_tokens)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
