#!/usr/bin/env python2
from string import printable
from msvcrt import getch

class encoder(object):

	def __init__(self):

		self.printable_edit()
		self.get_values()
		self.encode()
		self.output()

	#Whenever we want to skip given indexes for a character, we first run (skip_indexes % length), which gives us the actual number of indexes we need to skip
	#After that we use that as our skip number
	###############
	def encode(self):
		#New string that we'll be adding the resulting characters to
		self.resulting_string = ''

		numbers_skip = self.skip_indexes % 10
		letters_skip = self.skip_indexes % 26
		symbols_skip = self.skip_indexes % 32


		#Run for every character in string
		for char in self.str_to_encode:
			#If character is a lowercase letter
			if char in self.letters_lowercase:
				try:
					#Do the same as above but use letters_skip instead
					new_char = self.letters_lowercase[self.letters_lowercase.index(char) + letters_skip]
				except:
					#Out of range, do the same but remove index from the length of the letters
					new_char = self.letters_lowercase[letters_skip - (26 - self.letters_lowercase.index(char))]
			#If character is an uppercase letter (exactly the same as lowercase, but use the uppercase list to get uppercase result)
			elif char in self.letters_uppercase:
				try:
					new_char = self.letters_uppercase[self.letters_uppercase.index(char) + letters_skip]
				except:
					new_char = self.letters_uppercase[letters_skip - (26 - self.letters_uppercase.index(char))]
			#If user wants to encode special characters as well, proceed
			elif self.spchars == 'y':
				#If character is a number
				if char in self.numbers:				
					try:
						#Try adding "numbers_skip" (which is how many indexes we skip on the numbers list) to the character's current index
						new_char = self.numbers[self.numbers.index(char) + numbers_skip]
					except: 
						#If it fails, it means it's out of range, so we'll instead count how many we've already skipped, remove that from our skip number and skip the resulting ones from the beginning
						new_char = self.numbers[numbers_skip - (10 - self.numbers.index(char))]
				#If character is a symbol
				elif char in self.symbols:
					try:
						new_char = self.symbols[self.symbols.index(char) + symbols_skip]
					except:
						new_char = self.symbols[symbols_skip - (32 - self.symbols.index(char))]
			#If user does not want to encode special characters, use character as it is
			elif self.spchars == 'n':
				new_char = char

			#We've saved the resulting character in new_char, so we add that to our result string
			self.resulting_string += new_char


	#Get the values required from the user
	def get_values(self):

		#get string
		self.str_to_encode = raw_input('String to encode: ')

		#get indexes
		while True:

			self.skip_indexes = raw_input('Indexes to skip: ')

			try:
				self.skip_indexes = int(self.skip_indexes)
				break

			except:
				print 'An integer is required.'

		#Encode special characters or not
		#Note: msvcrt.getch() is used to get a single character in place of raw input. It also does not require pressing enter
		print 'Encode special characters and numbers (y/n)?'
		while True:
			self.spchars = getch()

			if self.spchars in ['y', 'n']:
				break
			else:
				continue



	#Split printable into 3 lists (letters, numbers, symbols)
	def printable_edit(self):
		p_list = list(printable)

		self.numbers = p_list[:10]
		self.letters_lowercase = p_list[10:36]
		self.letters_uppercase = p_list[36:62]
		self.symbols = p_list[62:95]

	#Give user the resulting string
	def output(self):
		print 'Resulting string:', self.resulting_string


if __name__ == '__main__':
	encoder()