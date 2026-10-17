import ollama

response = ollama.systemone(
    model='nimble-v3:9b-mxfp8',
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