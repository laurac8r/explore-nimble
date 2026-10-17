import ollama

MODEL = 'nimble-v3:9b-mxfp8'

response = ollama.systemone(
    model=MODEL,
    state='Hello world',
    questions={
        'says_hello': {
            'type': 'noul',
            'instructions': 'Does the text contain a greeting?',
            'criteria': {
                'true': 'The state text contains a greeting.',
                'false': 'The state text does not contain a greeting.'
            }
        }
    }
)

print(response.answers['says_hello'].noul)

response = ollama.systemone(
    model=MODEL,
    state='Returns are allowed within 30 days. This item was bought 12 days ago. It arrived undamaged.',
    questions={
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
)

print(response.answers['eligible'].noul, response.answers['department'].choice, response.answers['damage'].score)