import json
from ollama import Client
import argparse

MODEL_SYS_2 = 'qwen2.5-coder:7b'
# MODEL_SYS_2 = 'olmo-3:7b-think'

client = Client(host='http://127.0.0.1:11434')

# Define global execution options
CONFIG = {
    'num_ctx': 16384,
}

def generate_system_2_code(context: str) -> str | None:
    response = client.generate(
        model=MODEL_SYS_2,
        prompt=f'Summarize the below:\n\n{context}',
        options=CONFIG
    )
    return response.response

def example():
    print(generate_system_2_code(""""And when I feel, fair creature of an hour!
    That I shall never look upon thee more,
    Never have relish in the faery power
    Of unreflecting love — then on the shore
    Of the wide world I stand alone, and think
    Till Love and Fame to nothingness do sink."
    - “When I Have Fears That I May Cease to Be,” John Keats
    """))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    # print(args.input)
    print(generate_system_2_code(args.input))

    # Example below
    # $  python qwen.py "$(cat poem.md)"