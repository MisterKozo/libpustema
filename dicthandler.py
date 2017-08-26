import random

def _SeparateAndRequest(dictionary, char):
	words = []
	text  = dictionary.split('\n')

	for l in range(0,len(text)):
		line = text[l].split(' ')
		if line[0] == char:
			words.append(line[1])
	return words

def MakeUp(letter, index, length=0):
	if length == 0:
		length = random.randint(index,index+random.randint(0,5))
	word = ''

	for i in range(0,length):
		char = random.randint(97,122)
		word = word[:i] + chr(char) + word[i+1:]
	word = word[:index] + letter + word[index+1:]

	return word

def WhereIn(string, letter):
	for i in range(0, len(string)-1):
		if string[i] == letter:
			return i
	return -1

class DictionaryFile:
	dtype = ''

	def __init__(self, filename):
		with open(filename, 'r') as dfile:
			self.dictionary = dfile.read()

	def GetWords(self, dtype):
		self.dtype = dtype
		return _SeparateAndRequest(self.dictionary, dtype)
	def GetDtype(self):
		return self.dtype

class Dictionary:
	words = []
	dtype = ''

	def __init__(self, dictFile, dtype):
		self.words  = dictFile.GetWords(dtype)
		self.dtype  = dictFile.GetDtype()

	def GetWords(self):
		return self.words
	def GetLetter(self):
		return self.letter

	def GetLength(self):
		return len(self.words)

	def GetShortest(self):
		shortest = self.words[0]
		for w in range(1, len(self.words)):
			if len(self.words[w]) < len(shortest):
				shortest = self.words[w]
		return shortest
	def GetLongest(self):
		longest = self.words[0]
		for w in range(1, len(self.words)):
			if len(self.words[w]) > len(longest):
				longest = self.words[w]
		return longest

	def PickRandom(self):
		return self.words[random.randint(0,len(self.words)-1)]

	def LookForLength(self, length):
		compat = []
		for w in range(0,len(self.words)):
			if len(self.words[w]) == length:
				compat.append(self.words[w])
		return compat
	def LookForLetter(self, letter):
		compat = []
		for w in range(0,len(self.words)):
			for i in range(0,len(self.words[w])):
				if self.words[w][i] == letter:
					compat.append(self.words[w])
					i = len(self.words[w])
		return compat
	def LookForLetterInIndex(self, letter, index):
		compat     = []
		lookinside = self.LookForLetter(letter)
		for w in range(0, len(lookinside)):
			if len(lookinside[w]) > index:
				if lookinside[w][index] == letter:
					compat.append(lookinside[w])
		return compat
