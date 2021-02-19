#Desenvolva um programa que pergunte a distancia de uma viagem em km.
#Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km, e R$ 0,45 para viagens mais longas
print('=============================================================')
print('Vamos calcular o preço de sua passagem')
print('Será cobrando R$ 0,50 por km para viagens de até 200 km')
print('Será cobrando R$ 0,45 por km para viagens maiores que 200 km')
print('=============================================================\n')
distancia = float(input('\nQual é a distância da viagem em Km? '))
if distancia <= 200:
	preço = distancia * 0.50
	print('\nO seu custo é R$ {:.2f}'.format(preço))
else:
	preço = distancia * 0.45
	print('\nO seu custo é R$ {:.2f}'.format(preço))

#outra forma feita pelo professor	
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('\nO custo de sua passagem será {:.2f}'.format(preço))