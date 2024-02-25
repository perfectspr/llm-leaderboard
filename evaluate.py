import argparse
import os
import glob
import json
from tqdm import tqdm
from llama_cpp import Llama
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

MODEL_ROOT_PATH = os.environ.get("MODEL_ROOT_PATH", "./models")


def load_questions():
    questions = []
    for q_file in glob.glob("questions/*.md"):
        with open(q_file) as f:
            content = f.read()
            items = content.split("***\n")
            for item in items:
                if item:
                    question, answer = item.split("### Answer\n")
                    qid = question.split("\n")[0].replace("### ", "").strip()
                    q = question.replace(question.split("\n")[0], "").strip()
                    a = answer.strip()
                    questions.append(dict(qid=qid, question=q, answer=answer))
    return questions


def generate(llm, prompt):
    return llm.create_chat_completion(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.1,
    )["choices"][0]["message"]["content"].strip()


def main(model_config_file):
    with open(model_config_file) as f:
        config = json.load(f)
    model_path = os.path.join(MODEL_ROOT_PATH, config["modelPath"])
    llm = Llama(
        model_path=model_path,
        chat_format=config["chatFormat"],
        n_gpu_layers=100,
        n_ctx=config["context"],
        verbose=False,
    )
    questions = load_questions()
    with open("results/" + config["name"] + ".md", "w") as f:
        for q in tqdm(questions):
            answer = generate(llm, q["question"])
            f.writelines(
                [
                    "***",
                    "\n",
                    "### " + q["qid"],
                    "\n",
                    q["question"],
                    "\n",
                    "### Expected Answer",
                    "\n",
                    q["answer"],
                    "\n",
                    "### Received Answer",
                    "\n",
                    answer,
                    "\n",
                ]
            )
    print("Done!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--model", help="model config file")

    args = parser.parse_args()
    main(args.model)
