# DDD e cidades 
# USANDO dicionarios e chaves
# DICIONARIO = {Chave:Valor}
# Digite um codigo e a cidade vai aparecer
ddd = {61 : 'Brasilia', 71:'Salvador', 21:'Rio de Janeiro',11:'Sao Paulo',32:'Juiz de Fora', 19:'Campinas',27:'Vitoria', 31:'Belo Horizonte'}

codigo = int(input());

if codigo in ddd.keys():
	print (ddd[codigo])
else:
	print("DDD nao cadastrado");



