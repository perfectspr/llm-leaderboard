# Peter's LLM Leaderboard

Evaluating the capabilities of large language models is very difficult. There are already many public leaderboards that do this work. However, public leaderboards are often prone to malicious manipulation and some evaluation benchmarks are not suitable for real application scenarios. So I decided to create my own assessment benchmark and evaluate of my favourite models.

### Questions

I collected 61 test questions from the Internet,  it includes:

* [Knowledge](questions/knowledge.md) (7)
* [Coding](questions/coding.md) (8)
* [Censorship](questions/censorship.md) (6)
* [Instruction](questions/instruction.md) (6)
* [Math](questions/math.md) (7)
* [Extraction](questions/extraction.md) (7)
* [Reasoning](questions/reasoning.md) (10)
* [Summarizing](questions/summarizing.md) (6)
* [Writing](questions/writing.md) (4)

### My favourite models
* [Nous-Hermes-2-Mixtral-8x7B-DPO.Q4_K_M.gguf](https://huggingface.co/chat/settings/NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO)
* [openchat-3.5-0106.Q8_0.gguf](https://huggingface.co/TheBloke/openchat-3.5-1210-GGUF)
* [gemma-2b-it.Q8_0.gguf](https://huggingface.co/brittlewis12/gemma-2b-it-GGUF)
* [gemma-7b-it.Q8_0-v2.gguf](https://huggingface.co/sayhan/gemma-7b-it-GGUF-quantized)
* [qwen1_5-1_8b-chat-q8_0.gguf](https://huggingface.co/Qwen/Qwen1.5-1.8B-Chat-GGUF)
* [phi-2.Q8_0.gguf](https://huggingface.co/TheBloke/phi-2-GGUF)

34B, MoE and 70B models are comming soon!

### Evaluation tools

* llama-cpp-python
* python 3.10

### Evaluation result

| Model    | Total | Knowledge | Coding | Censorship | Instruction | Math | Extraction | Reasoning | Summarizing | Writing |
| -------- | ------- | -------- | ------- | -------- | ------- | -------- | ------- | -------- | ------- | ------- |
| Nous-Hermes-2-Mixtral-8x7B-DPO.Q4_K_M.gguf | 55  | 6 | 8 | 5 | 6 | 5 | 7 | 8 | 6 | 4 |
| openchat-3.5-0106.Q8_0.gguf | 53  | 7 | 8 | 6 | 6 | 5 | 7 | 4 | 6 | 3 |
| gemma-2b-it.Q8_0.gguf  | 36  | 3 | 7 | 6 | 3 | 2 | 2 | 4 | 6 | 3 |
| phi-2.Q8_0.gguf  | 26  | 6 | 5 | 5 | 3 | 3 | 1 | 2 | 1 | 0 |
| gemma-7b-it.Q8_0-v2.gguf  | 25  | 6 | 2 | 6 | 2 | 0 | 4 | 3 | 2 | 0 |
| qwen1_5-1_8b-chat-q8_0.gguf  | 25  | 3 | 5 | 3 | 2 | 1 | 5 | 2 | 2 | 2 |

#### Noetes
* gemma-2b-it is the best 2b models that I have tested, but there is still a big gap with the 7b models.
* gemma-7b-it is worse than gemma-2b-it, it may caused by GGUF issue. I will replace it with another version later. 

### Detailed result

* [Nous-Hermes-2-Mixtral-8x7B-DPO.Q4_K_M.gguf](results/Nous-Hermes-2-Mixtral-8x7B-DPO.md)
* [openchat-3.5-0106.Q8_0.gguf](./results/openchat.md)
* [gemma-2b-it.Q8_0.gguf](./results/gemma-2b.md)
* [gemma-7b-it.Q8_0-v2.gguf](./results/gemma-7b.md)
* [qwen1_5-1_8b-chat-q8_0.gguf](./results/qwen-1.5-1.8B.md)
* [phi-2.Q8_0.gguf](./results/phi-2.csv)

### VRAM requirements
| Model    | VRAM | GPUs |
| -------- | ------- | -------- |
| Nous-Hermes-2-Mixtral-8x7B-DPO.Q4_K_M.gguf | 24G  | >= GTX-3090 |
| openchat-3.5-0106.Q8_0.gguf | 9.4G | >= GTX-3080 |
| gemma-7b-it.Q8_0-v2.gguf | 15G | >= GTX-3080 |
| gemma-2b-it.Q8_0.gguf |  | >= GTX-3070 |
| phi-2.Q8_0.gguf  |  | >= GTX-3070  |
| qwen1_5-1_8b-chat-q8_0.gguf  |  | >= GTX-3070 |

### Run in local

#### Install Dependencies

```bash
CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install -r requirements.tx
```

#### Download Models

Download models from huggingface and put gguf files to `models` folder.

#### Create model config file

Create model config file in `models` folder, here is an example:
``` json
{
  "name": "gemma-2b",
  "chatFormat": "gemma",
  "modelPath": "gemma-2b-it.Q8_0.gguf",
  "context": 8192
}
```

#### Evaluation
```bash
python evaluate.py -m models/gemma-7b-it.json
```
