#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import dicthandler

def RandomWord(array):
	if len(array) == 0:
		return ''
	if len(array) == 1:
		return array[0]
	if (len(array) > 1):
		return array[random.randint(0,len(array)-1)]

filename = "dict.txt"
string   = "pustema"
song     = ""

dictFile = dicthandler.DictionaryFile(filename)
length   = len(string)

for i in range(0, length):
	word1 = ''
	word2 = ''

	method = 0 #method     = random.randint(0,3)
	if   method == 0:
		dict1 = dicthandler.Dictionary(dictFile, 'N')
		dict2 = dicthandler.Dictionary(dictFile, 'N')
	elif method == 1:
		dict1 = dicthandler.Dictionary(dictFile, 'N')
		dict2 = dicthandler.Dictionary(dictFile, 'V')
	elif method == 2:
		dict1 = dicthandler.Dictionary(dictFile, 'V')
		dict2 = dicthandler.Dictionary(dictFile, 'V')
	elif method == 3:
		dict1 = dicthandler.Dictionary(dictFile, 'C')
		dict2 = dicthandler.Dictionary(dictFile, 'C')
	lend1  = len(dict1.GetWords())
	lend2  = len(dict2.GetWords())
	
	shortest1 = dict1.GetShortest()
	shortest2 = dict2.GetShortest()
	longest1  = dict1.GetLongest()
	longest2  = dict2.GetLongest()
	
	#dts
	#look for first word that fits
	word1 = RandomWord(dict1.LookForLetterInIndex(string[i], i))
	if word1 != '':
		word2 = dict2.PickRandom()
	#dte

	if word1 == '':
		if i+1 < len(shortest1):
			word1 = dictHandler.MakeUp(string[i], i)
			word2 = dict2.PickRandom()
		else:
			compat2 = dict2.LookForLetter(string[i])
			for w2 in range(0, len(compat2)-1):
				for w1 in range(0, dict1.GetLength()):
					if len(dict1.GetWords()[w1])+dicthandler.WhereIn(compat2[w2],string[i]) == i:
						word1 = dict1.GetWords()[w1]
						word2 = compat2[w2]		
						w1 = lend1
						w2 = len(compat2)
	if word2 == '':
		if i+1 >= len(shortest1) and i+1 <= len(longest1):
			word1 = dicthandler.MakeUp(string[i], i)
			word2 = dict2.PickRandom()
		else:
			word1 = dict1.PickRandom()
			word2 = dicthandler.MakeUp(string[i], i-len(word1))
		#word1 isn't set, means that no word matches
		#DONE if index+1 is shorter than shortest word, make up first word and random second word
		#DONE if not, find all the second words that have the letter in them, loop through them, with each word look for a compatible first word (len1+newI=i). once found end loop
		#DONE if looped and word2 is empty and if index >= shortest || index <= longest, make up first word and put random second word
		#DONE else first random, second made up
		"""
		for w in range(0, lend2):
			if string[i] in dict2[w]:
				for x in range(0, len(dict2[w])):
					if dict2[w][x] == string[i]:
						position = x
						x = len(dict2[w])
				#word1 = dicthandler.LookForLength(i-position, dict1)[random.randint(0,len(dicthandler.LookForLength(i-position,dict1))-1)]
				word1 = dicthandler.LookForLength(i-position+1, dict1)[0]
				word2 = dict2[w]
				w = lend2
	if word1 == '':
		word1 = dict1[random.randint(0,lend1-1)]
		if i >= longl:
			word2 = dicthandler.MakeUp(string[i], i-len(word1))
		else:
			word1 = dicthandler.MakeUp(string[i], i, longl)
			word2 = dict2[random.randint(0,lend2-1)]
		"""
	print(word1 + ' ' + word2)
