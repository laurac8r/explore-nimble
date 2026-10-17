import ollama
from ollama import SystemOneResponse

MODEL = 'nimble-v3:9b-mxfp8'

SIMPLE_QUESTIONS = {
    'says_hello': {
        'type': 'noul',
        'instructions': 'Does the text contain a greeting?',
        'criteria': {
            'true': 'The state text contains a greeting.',
            'false': 'The state text does not contain a greeting.'
        }
    }
}
COMPLEX_QUESTIONS = {
    'eligible': {
        'type': 'noul',
        'instructions': 'Is this item within the store return window?',
        'criteria': {}
    },
    'department': {
        'type': 'choice',
        'instructions': 'Which department handles a return?',
        'criteria': {
            'returns': 'Product returns and refunds',
            'technical': 'Software installation',
        }
    },
    'damage': {
        'type': 'score',
        'instructions': 'How damaged was the item?',
        'criteria': [
            "Undamaged", "Minor damage", "Destroyed"
        ]
    },

}

MAPPING = {'0': "Undamaged", '1': "Minor damage", '2': "Destroyed"}

GREETING = 'Hello world'
RETURN_ELIGIBLE = 'Returns are allowed within 30 days. This item was bought 90 days ago. It arrived undamaged.'
RETURN_INELIGIBLE = 'Returns are allowed within 30 days. This item was bought 12 days ago. It arrived undamaged.'


def decide(state, questions=None):
    if questions is None:
        questions = COMPLEX_QUESTIONS
    response = ollama.systemone(
        model=MODEL,
        state=state,
        questions=questions
    )

    return response


def extract_multi_responses(response: SystemOneResponse) -> tuple[float | int, str, float | int]:
    return response.answers['eligible'].noul, response.answers['department'].choice, response.answers['damage'].score


response = decide(state=GREETING, questions=SIMPLE_QUESTIONS)

# Simple decision: Does the state contain a greeting?
print(response.answers['says_hello'].noul > 0.5)

# Complex decision: Return eligible? Department to handle it? Damage level of item?

## For an item that is eligible for a return
noul, choice, score = extract_multi_responses(decide(RETURN_ELIGIBLE))
print(f'Eligible for return?    Department to handle?   Damage level?')
print(f'{'Yes' if noul > 0.5 else 'No'}   {choice}     {MAPPING[f'{round(score)}']}')
print()

## For an item that is not eligible for a return
noul, choice, score = extract_multi_responses(decide(RETURN_INELIGIBLE))
print(f'Eligible for return?    Department to handle?   Damage level?')
print(f'{'Yes' if noul > 0.5 else 'No'}   {choice}     {MAPPING[f'{round(score)}']}')
print()
