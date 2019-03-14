import random
greeting_input = ("hello", "hi", "greetings", "sup", "what's up", "hey")
greeting_responses = ["hi", "hey", "*nods*", "hi there", "hello", "i amglad! you are talking to me"]
def check_for_greeting(sentence):
	for word in sentence.split('  '):
		if word.lower() in greeting_input:
			return random.choice(greeting_responses)
		else:
			return "i dont know"
while True:
	sentence = input( 'you: ')
	response = check_for_greeting(sentence)
	print('YourBot : ' + response)
 
	if 'bye' in sentence:
		break	