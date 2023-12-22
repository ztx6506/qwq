import bardapi
token = 'eghNmXrbUgaww3da878dHTTs1B42O3QA4VOx7kJoM9xBtG37-k8-EWOX8ti42BHKSMq-PQ.'
input_text = "王启航是什么东西"
response = bardapi.core.Bard(token).get_answer(input_text)['content']
print(response)