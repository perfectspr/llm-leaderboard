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
[miqu-1-70b-Requant-b2007-iMat-c32_ch400-IQ2_XS.gguf](https://huggingface.co/Nexesenex/MIstral-QUantized-70b_Miqu-1-70b-iMat.GGUF)
[Smaug-34B-v0.1_Q4_K_M.gguf](https://huggingface.co/nold/Smaug-34B-v0.1-GGUF)
[nous-capybara-34b.Q4_K_M.gguf](https://huggingface.co/TheBloke/Nous-Capybara-34B-GGUF)
* [ggml-senku-70b-iq2_xxs.gguf](https://huggingface.co/dranger003/Senku-70B-iMat.GGUF)
* [Nous-Hermes-2-Mixtral-8x7B-DPO.Q4_K_M.gguf](https://huggingface.co/TheBloke/Nous-Hermes-2-Mixtral-8x7B-DPO-GGUF)
* [openchat-3.5-0106.Q8_0.gguf](https://huggingface.co/TheBloke/openchat-3.5-1210-GGUF)
* [gemma-7b-it.Q8_0.gguf](https://huggingface.co/MaziyarPanahi/gemma-7b-it-GGUF)
* [gemma-2b-it.Q8_0.gguf](https://huggingface.co/brittlewis12/gemma-2b-it-GGUF)
* [qwen1_5-1_8b-chat-q8_0.gguf](https://huggingface.co/Qwen/Qwen1.5-1.8B-Chat-GGUF)
* [phi-2.Q8_0.gguf](https://huggingface.co/TheBloke/phi-2-GGUF)

34B, MoE and 70B models are comming soon!

### Evaluation tools

* llama-cpp-python
* python 3.10

### Evaluation result

| Model    | Total | Knowledge | Coding | Censorship | Instruction | Math | Extraction | Reasoning | Summarizing | Writing |
| -------- | ------- | -------- | ------- | -------- | ------- | -------- | ------- | -------- | ------- | ------- |
| miqu-1-70b-Requant-b2007-iMat-c32_ch400-IQ2_XS.gguf | 55  | 6 | 8 | 5 | 6 | 5 | 7 | 8 | 6 | 4 |
| ggml-senku-70b-iq2_xxs.gguf | 55  | 6 | 8 | 5 | 6 | 5 | 7 | 8 | 6 | 4 |
| nous-capybara-34b.Q4_K_M.gguf | 55  | 6 | 8 | 5 | 6 | 5 | 7 | 8 | 6 | 4 |
| Nous-Hermes-2-Mixtral-8x7B-DPO.Q4_K_M.gguf | 55  | 6 | 8 | 5 | 6 | 5 | 7 | 8 | 6 | 4 |
| openchat-3.5-0106.Q8_0.gguf | 53  | 7 | 8 | 6 | 6 | 5 | 7 | 4 | 6 | 3 |
| gemma-7b-it.Q8_0.gguf  | 44  | 6 | 7 | 6 | 5 | 4 | 5 | 2 | 6 | 3 |
| gemma-2b-it.Q8_0.gguf  | 36  | 3 | 7 | 6 | 3 | 2 | 2 | 4 | 6 | 3 |
| phi-2.Q8_0.gguf  | 26  | 6 | 5 | 5 | 3 | 3 | 1 | 2 | 1 | 0 |
| qwen1_5-1_8b-chat-q8_0.gguf  | 25  | 3 | 5 | 3 | 2 | 1 | 5 | 2 | 2 | 2 |

#### Noetes
* gemma-2b-it is the best 2b models that I have tested, but there is still a big gap with the 7b models.
* gemma-7b-it is worse than gemma-2b-it, it may caused by GGUF issue. I will replace it with another version later. 

### Detailed result

* [miqu-1-70b-Requant-b2007-iMat-c32_ch400-IQ2_XS.gguf](./results/miqu-1-70b.md)
* [Nous-Hermes-2-Mixtral-8x7B-DPO.Q4_K_M.gguf](results/Nous-Hermes-2-Mixtral-8x7B-DPO.md)
* [openchat-3.5-0106.Q8_0.gguf](./results/openchat.md)
* [gemma-2b-it.Q8_0.gguf](./results/gemma-2b.md)
* [gemma-7b-it.Q8_0.gguf](./results/gemma-7b.md)
* [qwen1_5-1_8b-chat-q8_0.gguf](./results/qwen-1.5-1.8B.md)
* [phi-2.Q8_0.gguf](./results/phi-2.csv)

### Model Info
| Model    | Size | VRAM | GPUs |
| -------- | ------- | ------- | -------- |
| miqu-1-70b-Requant-b2007-iMat-c32_ch400-IQ2_XS.gguf | 19G | 23.8G  | >= GTX-3090 |

| Nous-Hermes-2-Mixtral-8x7B-DPO.Q4_K_M.gguf | 28.4G | 24G  | >= GTX-3090 |
| nous-capybara-34b.Q4_K_M.gguf | 23.8 | 24G  | >= GTX-3090 |
| | 28.4G | 24G  | >= GTX-3090 |
| openchat-3.5-0106.Q8_0.gguf | 7.7G | 9.4G | >= GTX-3080 |
| gemma-7b-it.Q8_0.gguf | 9.1G | 15G | >= GTX-3080 |
| gemma-2b-it.Q8_0.gguf |  |  | >= GTX-3070 |
| phi-2.Q8_0.gguf  |  |  | >= GTX-3070  |
| qwen1_5-1_8b-chat-q8_0.gguf  |  |  | >= GTX-3070 |

### Run in local

#### 1. Install Dependencies

```bash
CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install -r requirements.txt
```

#### 2. Download Models

Download models from huggingface and put gguf files to `models` folder.

#### 3. Create model config file

Create model config file in `models` folder, here is an example:
``` json
{
  "name": "gemma-2b",
  "chatFormat": "gemma",
  "modelPath": "gemma-2b-it.Q8_0.gguf",
  "context": 8192
}
```

#### 4. Evaluation
```bash
python evaluate.py -m models/gemma-7b-it.json
```
