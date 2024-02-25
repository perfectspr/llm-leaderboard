# Peter's LLM Leaderboard

Evaluating the capabilities of large language models is very difficult. There are already many public leaderboards that do this work. However, public leaderboards are often prone to malicious manipulation and some evaluation benchmarks are not suitable for real application scenarios. So I decided to create my own assessment benchmark and evaluate of my favourite models.

### Questions
I collected 61 test questions from the Internet,  it includes:

* [Knowledge](questions/knowledge.md) (7)
* [Coding](questions/coding.md) (8)
* [Censorship](questions/censorship.md) (6)
* [Instruction](questions/instruction.md) (6)
* [Math](questions/math.md) (7)
* [Extraction](questions/extraction.d) (7)
* [Reasoning](questions/reasoning.md) (10)
* [Summarizing](questions/summarizing.md) (6)
* [Writing](questions/writing.md) (4)

### My favourite models
* [openchat-3.5-0106.Q8_0.gguf](https://huggingface.co/TheBloke/openchat-3.5-1210-GGUF)
* [gemma-2b-it.Q8_0.gguf](https://huggingface.co/brittlewis12/gemma-2b-it-GGUF)
* [gemma-7b-it.Q8_0-v2.gguf](https://huggingface.co/sayhan/gemma-7b-it-GGUF-quantized)
* [qwen1_5-1_8b-chat-q8_0.gguf](https://huggingface.co/Qwen/Qwen1.5-1.8B-Chat-GGUF)
* [phi-2.Q8_0.gguf](https://huggingface.co/TheBloke/phi-2-GGUF)

34B, MoE and 70B models is comming soon!

### Evaluation tools

* llama-cpp-python
* python 3.10

### Evaluation result

| Model    | Total | Knowledge | Coding | Censorship | Instruction | Math | Extraction | Reasoning | Summarizing | Writing |
| -------- | ------- | -------- | ------- | -------- | ------- | -------- | ------- | -------- | ------- | ------- |
| openchat-3.5-0106.Q8_0.gguf | 50  | 7 | 7 | 6 | 6 | 4 | 7 | 4 | 6 | 3 |
| gemma-2b-it.Q8_0.gguf  | 36  | 3 | 6 | 6 | 3 | 2 | 3 | 4 | 6 | 3 |
| gemma-7b-it.Q8_0-v2.gguf  | 25  | 6 | 2 | 6 | 2 | 0 | 4 | 3 | 2 | 0 |
| qwen1_5-1_8b-chat-q8_0.gguf  | 24  | 3 | 5 | 3 | 2 | 0 | 5 | 2 | 2 | 2 |
| phi-2.Q8_0.gguf  | 24  | 6 | 4 | 5 | 3 | 2 | 1 | 2 | 1 | 0 |

gemma-2b-it is the best 2b models that I have tested, but there is still a big gap with the 7b models.
