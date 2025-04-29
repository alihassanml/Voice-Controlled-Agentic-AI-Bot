import json
import requests


model = "gemma3:1b" 

def generate(prompt, context):
    r = requests.post('http://localhost:11434/api/generate',
        json={
            "model": model,
            "prompt": prompt,
            "context": context,
        },
        stream=True
    )
    r.raise_for_status()

    for line in r.iter_lines():
        body = json.loads(line)
        response_part = body.get('response', '')
        
        print(response_part, end='', flush=True)

        if 'error' in body:
            raise Exception(body['error'])

        if body.get('done', False):
            return body['context']

def main():
    context = []  
    while True:
        user_input = input("Enter a prompt: ")
        if not user_input:
            exit()
        print()
        context = generate(user_input, context)
        print()

if __name__ == "__main__":
    main()
