
import torch
import os
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

class KernelConnector:
    def __init__(self, base_model_id="Qwen/Qwen2.5-1.5B"):
        self.base_path = "/content/drive/MyDrive/ai-kernel/adapters"
        self.tokenizer = AutoTokenizer.from_pretrained(base_model_id)
        self.base_model = AutoModelForCausalLM.from_pretrained(
            base_model_id, torch_dtype=torch.float16, device_map="auto"
        )
        intent_path = os.path.join(self.base_path, "intent")
        self.model = PeftModel.from_pretrained(self.base_model, intent_path, adapter_name="intent")
        for adapter in ["decomposition", "planning", "constraints", "self_check", "stop"]:
            path = os.path.join(self.base_path, adapter)
            if os.path.exists(path):
                self.model.load_adapter(path, adapter_name=adapter)
        self.model.eval()

    def call_primitive(self, adapter_name, prompt):
        self.model.set_adapter(adapter_name)
        full_prompt = f"### INPUT:\n{prompt}\n\n### OUTPUT:\n"
        inputs = self.tokenizer(full_prompt, return_tensors="pt").to("cuda")
        with torch.no_grad():
            outputs = self.model.generate(**inputs, max_new_tokens=128, pad_token_id=self.tokenizer.eos_token_id)
        raw = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return raw.split("### OUTPUT:")[-1].strip()

KERNEL = None
def get_kernel():
    global KERNEL
    if KERNEL is None: KERNEL = KernelConnector()
    return KERNEL
