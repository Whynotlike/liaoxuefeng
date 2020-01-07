class Student(object):
    __slots__ = ('name', 'age')


class Teacher(Student):
    pass


class Police(Student):
    __slots__ = ('score')


"""
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
====== RESTART: C:\Users\Administrator.USER-20190718XU\Desktop\slots.py ======
>>> s = Student()
>>> s.name = 'sala'
>>> s.age = '23'
>>> s.score = '11'
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s.score = '11'
AttributeError: 'Student' object has no attribute 'score'
>>> t = Teacher()
>>> t.score = '11'
>>> p = Police()
>>> p.name = 'poloce'
>>> p.age = '32'
>>> p.score = '90'
>>> from types import MethodType
>>> def fn_1(self,school):
	self.school = school

	
>>> def fn_2(self,home):
	self.home = home

	
>>> a.fn_1 = MethodType(fn_1, a)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.fn_1 = MethodType(fn_1, a)
NameError: name 'a' is not defined
>>> t.fn_1 = MethodType(fn_1, t)
>>> t.fn_1('longyu')
>>> t.fn_1
<bound method fn_1 of <__main__.Teacher object at 0x0000000002E71870>>
>>> print(t.fn_1)
<bound method fn_1 of <__main__.Teacher object at 0x0000000002E71870>>
>>> t.school
'longyu'
>>> Student.fn_2 = fn_2
>>> t.home = 'fujian'
>>> t.home
'fujian'
>>> p.home = 'jiangxi'
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    p.home = 'jiangxi'
AttributeError: 'Police' object has no attribute 'home'
>>> s.school = 'minjiang'
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s.school = 'minjiang'
AttributeError: 'Student' object has no attribute 'school'
>>> q = Student()
>>> w = Teacher()
>>> e = Police()
>>> q.fn_2('fujian')
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    q.fn_2('fujian')
  File "<pyshell#16>", line 2, in fn_2
    self.home = home
AttributeError: 'Student' object has no attribute 'home'
>>> q.name = 'qianxun'
>>> q.school = 'zheda'
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    q.school = 'zheda'
AttributeError: 'Student' object has no attribute 'school'
>>> w.name = 'womemn'
>>> w.school = 'beida'
>>> w.home = 'shanghai'
>>> e.name = 'erzi'
>>> e.score = '0'
>>> e.school = 'shehuidaxue'
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    e.school = 'shehuidaxue'
AttributeError: 'Police' object has no attribute 'school'
>>> e.home = ''qiaodong''
SyntaxError: invalid syntax
>>> e.home = 'qiaodong'
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    e.home = 'qiaodong'
AttributeError: 'Police' object has no attribute.
"""
