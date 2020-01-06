#!/usr/bin/env python2
from random import choice, randint
from glob import glob
from string import ascii_lowercase
from sys import argv


#creates one single word in form of string and returns it
def make_word():
	l = ascii_lowercase
	length = randint(1, 12)
	word = ''

	#variable to get more vowels after consonants
	increase_vowel_chance = False

	while len(word) != length:
		#previous letter was consonant
		if increase_vowel_chance:
			ofp = randint(0, 1)
			if ofp:
				l = vowels

		#get random letter and add to word
		letter = choice(l)
		word += letter

		#check if letter was vowel or not
		if letter not in vowels:
			increase_vowel_chance = True
		else:
			increase_vowel_chance = False
			l = ascii_lowercase
	return word


#creates a sentence of random word amount in form of list and returns it
def write_sentence():
	length = randint(1, 25)
	sentence = []

	#stop after sentence length is equal to pre-decided
	while len(sentence) <= length:
		word = make_word()

		#discard word if there are no vowels and it is multi-letter
		if len(word) > 1:
			v = False
			for letter in vowels:
				if letter in word:
					v = True
			if not v:
				continue


		#word is first in sentence, capitalize first letter
		if len(sentence) == 0:
			word = word[0].upper() + word[1:]

		#word is last in sentence, add ;, ?, or .
		if len(sentence) == length:
			mark = randint(0, 9)
			if mark == 8:
				mark = ';'
			elif mark == 9:
				mark = '?'
			else:
				mark = '.'

			word += mark

		#check if previous word was single letter
		if len(sentence) != 0:
			if len(sentence[len(sentence) - 1]) == 1 and len(word) == 1:
				continue

		#add word to sentence
		sentence.append(word)

	#make sentence a string and return
	sentence = ' '.join(sentence)
	sentence += ' '
	return sentence, length


#90k words
word_count = 0

vowels = 'aeiouy'

try:
	if len(argv) != 2:
		raise

	magnitude = int(argv[1])

except:
	print 'Expected a single integer argument'
	exit(1)


#figure out book name
while True:
	name = make_word()
	if name in glob('*'):
		continue
	break


f = open(name + '.txt', 'w')


while word_count <= magnitude:

	#get sentence and amount of words it contains
	sentence, words = write_sentence()

	#add sentence to book
	f.write(sentence)

	#increase word count integer
	word_count += words


#write book in a file
f.close()

