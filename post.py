import requests


token = input('Informe seu token: ')
try:
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=' + token
    answer = {'answer': ('answer', open('answer.json', 'rb'))}

    post_result = requests.post(url, files=answer)
  
except:
    print('Token incorreto ou inexistente!')

print(post_result.text)
