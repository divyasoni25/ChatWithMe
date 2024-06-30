#Initializing empty lists
words = []
labels = []
docs_x = []
docs_y = []

#Looping through our data
for intent in data['intents']:
	for pattern in intent['patterns']:
		pattern = pattern.lower()
    		#Creating a list of words
		wrds = nltk.word_tokenize(pattern)
		words.extend(wrds)
		docs_x.append(wrds)
		docs_y.append(intent['tag'])

	if intent['tag'] not in labels:
	  labels.append(intent['tag'])