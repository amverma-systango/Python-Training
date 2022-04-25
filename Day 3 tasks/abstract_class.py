# abstract class


from abc import ABC, abstractmethod

class Polygon(ABC):

	@abstractmethod
	def sides(self):
		pass

class Triangle(Polygon):

	def sides(self):
		print("3 sides")

class Square(Polygon):

	def sides(self):
		print("4 sides")

class Pentagon(Polygon):
	
	def sides(self):
		print("5 sides")

class Hexagon(Polygon):

	def sides(self):
		print("6 sides")


r1 = Triangle()
r1.sides()

s1 = Square()
s1.sides()

p1 = Pentagon()
p1.sides()

h1 = Hexagon()
h1.sides()
