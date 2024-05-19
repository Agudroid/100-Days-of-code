import requests


parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
    "difficulty": "medium"
}
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = []
for result in response.json()['results']:
    question = {
        'question': result['question'],
        'correct_answer': result['correct_answer']
    }
    question_data.append(question)
