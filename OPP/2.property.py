# -*- coding: utf-8 -*-

''' Learn @property '''

# 在绑定属性时，属性直接暴露出去，虽然写起来简单，但没办法检查参数，参数的值也可以随意改动
# 显然不符合逻辑，通过限制方法来设置，也可以在里面加入检查参数的办法。

# class Student(object):

# 	#创建调用方法
# 	def get_score(self):
# 		return self._score

# 	#创建设置参数和检查参数的方法
# 	def set_score(self,value):
		
# 		# 参数检查，检查传入的值是否为 'int'，如果不是抛出ValueError错误
# 		if not isinstance(value, int):
# 			raise ValueError('score must be an integer!')
		
# 		# 参数检查，限制传入的参数取值在0~100之间，如果不是抛出ValueError错误
# 		if value < 0 or value > 100:
# 			raise ValueError('score must between 0~100!')
		
# 		# 赋值
# 		self._score = value

'''
========================================================================
'''

# 不过上面的调用方法略显复杂，有没有既能检查参数又可以用类似属性这样简单的方法来访问类的变量呢？
# 装饰器(decorator)可以给函数动态加上功能，对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的:

# class Student(object):

# 	# 调用内置 @property 装饰器
# 	# @property 会把一个getter方法变成属性，其本身又创建了另一个装饰器 @score.setter，负责把另一个setter变成属性赋值。
# 	@property
# 	def score(self):
#                 # 调用方法： s.score 实际转化为 s.get_score()
# 		return self._score
	
# 	# 调用 @score.setter (@property创建的另一个装饰器)
# 	@score.setter
# 	def score(self,value):
#                 # 调用方法： s.score = value  实际转化为 s.set_score()

# 		# 参数检查，检查传入的值是否为 'int'，如果不是抛出ValueError错误
# 		if not isinstance(value, int):
# 			raise ValueError('score must be an integer!')
		
# 		# 参数检查，限制传入的参数取值在0~100之间，如果不是抛出ValueError错误
# 		if value < 0 or value > 100:
# 			raise ValueError('score must between 0~100!')
		
# 		# 赋值
# 		self._score = value

'''
========================================================================
'''

# 注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

# class Student(object):

# 	@property
# 	def birth(self):
# 		return self._birth
	
# 	@birth.setter
# 	def birth(self,value):
# 		self._birth = value

# 	# 创建‘age’只读属性
# 	@property
# 	def age(self):
# 		return 2020 - self._birth
	
'''
====================================================================
Practice
'''

# class Screen(object):

# 	@property
# 	def Width(self):
# 		return self._Width
	
# 	@Width.setter
# 	def Width(self,value):
# 		self._Width = value

# 	@property
# 	def Height(self):
# 		return self._Height
	
# 	@Height.setter
# 	def Height(self,value):
# 		self._Height = value

# 	@property
# 	def Resolution(self):
# 		return self.Width * self.Height
	
'''
Completed January 7,2020
'''
'''
优化版
'''
class Screen(object):

	@property
	def kid(self):
		return self._width,self._height

	@kid.setter
	def kid(self, arrs):
		self._width = arrs[0]
		self._height = arrs[1]
	
	@property
	def Sum(self):
		self.sum = self._width * self._height
		return self.sum
	
# January 8