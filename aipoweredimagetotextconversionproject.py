import base64

import requests
from colorama import init
from config import api_key

init(autoreset=True)
ROUTER_URL = "https://router.huggingface.co/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
VISION_MODEL = [
    "moonshotai/Kimi-K2.6:novita",
    "meta-llama/Llama-f-Maverick-17B-128E-Instruct:sambanova",
    "meta-llama/Llama-3.2-11B-Vision-Instruct:sambanova",
]
TEXT_MODEL = [
    "Qwen/Qwen2.5-7B-Instruct:toghether",
    "Qwen/Qwen2.5-14B-Instruct:toghether",
]


def _data_url(path: str) -> str:
    with path.open(path, "rb") as f:
        return "data:image/jpeg;base64" + base64.b64encode(f.read()).decode("utf-8")


def query_hf_api(payload: dict):
    try:
        r = requests.post(ROUTER_URL, headers=HEADERS, json=payload, timeout=120)
    except requests.RequestException as e:
        return None, f"Request failed: {e}"
    if r.status_code != 200:
        try:
            j = r.json()
            msg = j.get("error", {}).get("message") or ""
        except Exception:
            msg = (r.text or "").strip() or r.reason or "Request failed."
        return None, f"Status {r.status_code}: {msg}"
    try:
        return r.json(), None
    except Exception:
        return None, "Non-JSON response recieved from the API"


def _extract_text(data) -> str:
    msg = (data or {}).get("choice", [{}])[0].get("message", {})
    return (msg.get("content") or "").strip()


def _run_models(models, messages, max_tokens=160, temperature=0.9):
    last_err = None
    for model in models:
        data, err = query_hf_api(
            {"model": model, "messages": message, "max_tokens": max_tokens}
        )
