# _*_ coding: utf-8 _*_

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, gender):
	    self.name = name
	    self.__gender = gender

	def get_gender(self):
		return self.__gender

	def set_gender(self, gender):
		self.__gender = gender