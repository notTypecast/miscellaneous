#!/usr/bin/env python2
from random import choice
from sys import argv
from time import sleep

class MontyHallSim(object):

	def __init__(self, repeats, mode):
		
		self.MODE = mode
		self.REPEATS = repeats
		self.OPTIONS = ['a', 'b', 'c']
		#ASSUME a IS THE CORRECT OPTION

		self.WINS = 0


	def run(self):

		for repeat in xrange(1, self.REPEATS + 1):
			tmp = list(self.OPTIONS)
			#random option
			current = choice(self.OPTIONS)

			#a is the correct option, so:
			
			#if switching and choice is b or c, then add win (because of switch to a)
			#otherwise don't add a win, because choice is a and will switch to other
			if self.MODE == 'switch':
				if current in ['b', 'c']:
					self.WINS += 1
				
				#set current to None so if it is a, it isn't added again
				current = None

			#if not switching, just check if option is correct 
			if current == 'a':
				self.WINS += 1

			print '\rWIN: {:.2f}%'.format( (float(self.WINS) / float(repeat)) * 100 ), ' ' * 50,





if __name__ == '__main__':

	try:
		if len(argv) != 3:
			raise

		simulation = MontyHallSim(int(argv[1]), argv[2])
		simulation.run()

	except:
		print 'Usage: monty_hall_sim.py [repeats] [switch/stick]'
		exit(1)