from llama import model

from llama.config import REPEAT_PENALTY, SYSTEM_PROMPT, TEMPERATURE, TOP_K, TOP_P, DEFAULT_JSON



def predict(message, history, response_format=None):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    for human, assistant in history:
        messages.append({"role": "user", "content": human })
        messages.append({"role": "assistant", "content":assistant})
    
    messages.append({"role": "user", "content": message})
    
    output =  model.create_chat_completion(
        messages,
        temperature=TEMPERATURE,
        top_k=TOP_K,
        top_p=TOP_P,
        repeat_penalty=REPEAT_PENALTY,
        stream=False,
        response_format=response_format
    )
    response = output["choices"][0]["message"]["content"]
    return response