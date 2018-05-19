

class Retangulo(object):
	"""docstring for retangulo"""
	def __init__(self, altura, largura):
		super(Retangulo, self).__init__()
		self.altura = altura
		self.largura = largura

	def area(self):
		return self.altura * self.largura


class Circulo(object):
	"""docstring for circulo"""
	def __init__(self, raio):
		super(Circulo, self).__init__()
		self.raio = raio

	def area(self):
		return 3.14 * self.raio**2

	def circunferencia(self):
		return 2 * 3.14 * self.raio




