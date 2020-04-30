import requests


token = '1158495dddc2bfea5532a710ce71e9b9d5932306'

url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=' + token
answer = {'answer': ('answer', open('answer.json', 'rb'))}

post_result = requests.post(url, files=answer)
print(post_result.text)
