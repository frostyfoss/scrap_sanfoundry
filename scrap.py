# Webscrapping program to grab all the mcq question and answers from sanfoundry.com
# Then create a Markdown friendly md file to make pdf directly
# I like things offline, so made this...
# and it was fun too!

import requests
from bs4 import BeautifulSoup

URL = "https://www.sanfoundry.com/operating-system-questions-answers/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "lxml") # html.parser

article = soup.find('div', class_='entry-content')
questions = article.find_all('p')
answers = article.find_all('div', class_='collapseomatic_content')

#print(len(questions))
#print(len(answers))

title = questions[0].text.splitlines()
#print(title) # don't include last element 'View Answer'

def ansFirst():
	for (question,answer) in zip(questions[1:], answers): #questions[0] is title
		ans = answer.text.splitlines()
		for a in ans: # newline for list ele
			print(a)
		ques = question.text.splitlines()[0:-1] #last one is View Answer
		for q in ques:
			print(q) # newline for list ele
		print()

def questionFirst():
	for (question,answer) in zip(questions[1:], answers): #questions[0] is title
		ques = question.text.splitlines()[0:-1] #last one is View Answer
		for q in ques:
			print(q) # this loop is just for newline
		print(answer.text)

mcqObj = []

def makeMcqObject():
	for (question,answer) in zip(questions[1:], answers): #questions[0] is title
		dict = {}
		# q[0] = '1. What is an operating system?'
		# q[1], q[2], q[3] and q[4] are options
		q = question.text.splitlines()[0:-1] #last one is View Answer
		dict['sn'] = int(q[0].split()[0][0]) # result = 1
		dict['question'] = ' '.join(q[0].split()[1:]) # result = 'What is an operating system?'
		listOption = [q[1], q[2], q[3], q[4]]
		dict['options'] = listOption # options

		# ans = ['Answer: d', 'Explanation:']
		ans = answer.text.splitlines()
		# option a=1, b=2, c=3, d=4
		correctOption = ord(ans[0].split()[1])-97+1
		dict['answer'] = correctOption
		dict['explanation'] = ans[1]
		
		mcqObj.append(dict)
"""
sample output of makeMcqObject():
[{'sn': 1, 'question': 'What is an operating system?', 'options': ['a) collection of programs that manages hardware resources', 'b) system service provider to the application programs', 'c) interface between the hardware and application programs', 'd) all of the mentioned'], 'answer': 4, 'explanation': 'Explanation: An Operating System acts as an intermediary between user/user applications/application programs and hardware. It is a program that manages hardware resources. It provides services to application programs.'}]
"""
		

def mdObject():
	for (question,answer) in zip(questions[1:], answers): #questions[0] is title
		ans = answer.text.splitlines()
		# option a=1, b=2, c=3, d=4
		correctOption = ord(ans[0].split()[1])-97+1  # ans = ['Answer: a', 'Explanation: None.']
		print(correctOption)
	#print(ord('z') - 97)


makeMcqObject()
print(mcqObj[3])



"""
structure of the object
list = [ [ {'sn':int, 'question':'string', 'options':[a,b,c,d], 'answer':int, 'explanation':'string'} ],
		 [],
		 [] 
	   ]
"""

"""
# Code experiment, since I'm noob in python XD
#{'sn':int, 'question':'string', 'options':[a,b,c,d], 'answer':int, 'explanation':'string'}
list1 = []
dict1 = {}
dict1['sn'] = 1 
dict1['question'] = 'the question'
listOption = ['optionA', 'optionB', 'optionC', 'optionD']
dict1['options'] = listOption
dict1['answer'] = 3
dict1['explanation'] = 'the explanation'
list1.append(dict1)
dict1['sn'] = 2
list1.append(dict1)

print(list1)
print(list1[1])
print(list1[1]['sn'])
print(list1[1]['options'][2])

op:
[{'sn': 2, 'question': 'the question', 'options': ['optionA', 'optionB', 'optionC', 'optionD'], 'answer': 3, 'explanation': 'the explanation'}, {'sn': 2, 'question': 'the question', 'option': ['optionA', 'optionB', 'optionC', 'optionD'], 'answer': 3, 'explanation': 'the explanation'}]
{'sn': 2, 'question': 'the question', 'options': ['optionA', 'optionB', 'optionC', 'optionD'], 'answer': 3, 'explanation': 'the explanation'}
2
optionC
"""


"""
# this just prints the questions only
article = soup.find('div', class_='entry-content').findAll('p')

for question in article:
	qText = question.text
	qAns = question.
	print(qText)
"""