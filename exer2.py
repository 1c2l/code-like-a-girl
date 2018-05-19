def  function1(lista):
	x = 1
	for item in lista:
		x = x * item 
	print(x)


#function1([8, 2, 3, -1, 7])



def fatorial(numero):
	if numero < 0:
		raise Exception("numero negativo")
	function1(range(1, numero + 1))

#fatorial(8)

def exercicio3(divisor, multiplicador, limiteminimo, limitemaximo):
	x = []
	for item in range(limiteminimo, limitemaximo):
		if item % divisor== 0 and item % multiplicador== 0:
			x.append(item)
	print(x)

exercicio3(7,5,1500,1700)


	
