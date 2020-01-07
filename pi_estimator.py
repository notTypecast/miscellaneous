#!/usr/bin/env python2
import pygame
from pygame.locals import *
from random import randint
from math import sqrt
from sys import argv


class Estimator(object):

	def __init__(self, keep = False):

		#keep or disgard dots after a certain amount (keeping causes eventual lag)
		self.keep = keep

		##Basic execution variables
		self._display_surf = None
		self.length = 1220
		self.height = 820
		self.FPS = 12000
		self.clock = pygame.time.Clock()
		pygame.font.init()
		self.myfont = pygame.font.SysFont('Comic Sans MS', 30)

		self.RED = (255, 0, 0)
		self.WHITE = (255, 255, 255, 0)
		self.BLACK = (0, 0, 0)

		#Program variables

		#points to throw
		self.points = 'inf'
		#points landed in circle
		self.Nc = 0
		#points landed in square (total points thrown)
		self.N = 0

		self.radius = 360
		self.center_x = self.length/2
		self.center_y = self.height/2

		self.all_points = []


	def on_run(self):
		pygame.init()
		self._display_surf = pygame.display.set_mode((self.length, self.height,))
		pygame.display.set_caption('PI estimator')

		self.runner()

	def calculator(self):

		if self.N <= self.points or f == 'inf':

			point_x = randint(self.center_x - self.radius, self.center_x + self.radius)
			point_y = randint(self.center_y - self.radius, self.center_y + self.radius)

			distance_from_center = sqrt( (self.center_x - point_x) ** 2 + (self.center_y - point_y) ** 2 )

			if distance_from_center <= self.radius:
				self.Nc += 1

			self.N += 1

			return (point_x, point_y,)


		else:

			return None


	
	def runner(self):


		while True:

			if len(self.all_points) == 1000 and not self.keep:
				self.all_points = []

			point = self.calculator()

			if point:

				self.all_points.append(point)

				self._display_surf.fill(self.BLACK)

				pygame.draw.circle(self._display_surf, self.WHITE, (610, 410,), 360, 5)
				pygame.draw.rect(self._display_surf, self.WHITE, (250, 50, 720, 720,), 5)

				for point in self.all_points:
					pygame.draw.rect(self._display_surf, self.RED, point + (5, 5,) ,0)

				Nc_text = self.myfont.render('In circle: {}'.format(self.Nc), False, self.WHITE)
				N_text = self.myfont.render('Thrown: {}'.format(self.N), False, self.WHITE)

				self._display_surf.blit(Nc_text, (0, 0,))
				self._display_surf.blit(N_text, (0, 40,))

				result = self.myfont.render('pi = {}'.format(4 * float(self.Nc)/self.N), False, self.WHITE)

				self._display_surf.blit(result, (500, 0))


				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						exit()

				
				pygame.display.update()
				self.clock.tick(self.FPS)

			else:

				break



		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					pygame.quit()
					exit()

			pygame.display.update()










if __name__ == '__main__':

	try:
		if len(argv) not in [1, 2]:
			raise

		if len(argv) == 2:
			if argv[1] == 'keep':
				estimator = Estimator(keep = True)
			else:
				raise
		else:
			estimator = Estimator()
		
		estimator.on_run()

	except Exception as e:
		print e
		print 'Usage: python estimator (keep)'