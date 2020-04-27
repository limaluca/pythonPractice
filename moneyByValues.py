# Separando valor em cedulas E MOEDAS
dinheiro = float(input());
cedulas = (100.00, 50.00, 20.00, 10.00, 5.00, 2.00);
moedas = (1.00,0.50,0.25,0.10,0.05,0.01);

print('NOTAS: ');
for valor in cedulas:
    count, dinheiro = divmod(dinheiro, valor);
    print(int(count),'nota (s) de R$ {:0,.2f}'.format(valor));

print('MOEDAS: ');
for valor in moedas:
	count,dinheiro = divmod(dinheiro,valor);
	print(int(count),'moeda (s) de R$ {:0,.2f}'.format(valor));