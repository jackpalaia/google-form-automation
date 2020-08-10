import requests

def send_request(id, questions, content):
  baseUrl = f'https://docs.google.com/forms/d/e/{id}/formResponse'
  params = {}
  for i in range(len(questions)):
    params[f'entry.{questions[i]}'] = f'{content[i]}'
  r = requests.get(baseUrl, params=params)
  print(r.status_code, r.url)

def main():
  # replace question id's here
  question_numbers = ['480450170', '281008616', '357985642']

  # input content to fill questions with here
  # position in question_numbers array corresponds with position in content array
  content = ['content0', 'content1', 'option 2']

  # input form_id here
  form_id = '1FAIpQLSdO1ZC75xyi-2CCY5odhQTOBOkjR0ayXkKmhf8bTVHvP9MbeA'

  send_request(form_id, question_numbers, content)

if __name__ == "__main__":
  main()  