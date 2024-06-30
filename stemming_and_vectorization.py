stemmer = LancasterStemmer()
words = [stemmer.stem(w.lower()) for w in words if w not in "?"]
words = sorted(list(set(words)))
labels = sorted(labels)

training = []
output = []

out_empty = [0 for _ in range(len(labels))]
for x,doc in enumerate(docs_x):
	bag = []
	wrds = [stemmer.stem(w) for w in doc]
	for w in words:
		if w in wrds:
			bag.append(1)
		else:
			bag.append(0)
	output_row = out_empty[:]
	output_row[labels.index(docs_y[x])] = 1
	training.append(bag)
	output.append(output_row)
#Converting training data into NumPy arrays
training = np.array(training)
output = np.array(output)

#Saving data to disk
with open("data.pickle","wb") as f:
	pickle.dump((words, labels, training, output),f)