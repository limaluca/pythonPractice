#1

distancia = int(input("Informe o comprimento total da pista de corrida: "))

tempoCarroA = int(input("Você completou o percurso de %d metros em quantos segundos? " % (distancia)))

tempoCarroB = int(input("Você completou o percurso de %d metros em quantos segundos? " % (distancia)))

velocidadeCarroA = distancia/tempoCarroA;

velocidadeCarroB = distancia/tempoCarroB;

if velocidadeCarroA > velocidadeCarroB:
	print("O carro mais rápido estava a %d Km/h " % (velocidadeCarroA*3.6))
	# Multiplica-se a velocidade 3.6 para conversão de m/s para Km/h

else:
	print("O carro mais rápido estava a %d Km/h " % (velocidadeCarroB*3.6))

#__________________________________
#2 
#__________________________________


day = int(input("Informe o dia da sua data: "))
month = int(input("Informe o mês da sua data: "))
year = int(input("Informe o ano da sua data: "))

bissexto = False;
dataValida = True;

#Regra dos anos bissextos
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
	bissexto = True;

if day > 31 or month > 12:
	dataValida = False

if day == 29 and month == 2 and not bissexto:
	dataValida = False

if day > 28 and month == 2 and not bissexto:
	dataValida = False;

#meses com 30 dias e fevereiro com 29
if month == 4 or month == 6 or month == 9 or month == 11 and day > 30 or month == 2 and day > 29:
	dataValida = False 

if dataValida:
	print("A data %d/%d/%d é válida." % (day,month,year))
else:
	print("A data %d/%d/%d é inválida." % (day,month,year))

 
#__________________________________
#3
#__________________________________


pi = 4
n = 3
i = 0
aux = 0

while (aux <= 0.0001):
	aux = 4/n
	if (i==1):
		pi = pi + aux
		i = 0
	else:
		pi = pi-aux;
		i = 1;
n = n + 2

	
	


print("O valor do PI é: ",pi)

#__________________________________
#4 
#__________________________________

#Decidi por utilizar laços aninhados para simular as horas passando por 24 horas
for horas in range(24): 
    for minutos in range(60):
        for segundos in range(60):
            print("Relógio: ",horas,"h",minutos,"min",segundos,"s")



#__________________________________
#5
#__________________________________


sectors = []
maior = 0;
firstVisited = ""
secondVisited =""


while True:

	sector = str(input("Informe o nome do setor favorito de cada visitante: "))
	if sector == "fim":
		break;
	sectors.append(sector)

#Primeiro mais visitado
for item in sectors:
	if sectors.count(item) > maior:
		maior = sectors.count(item);
		firstVisited = item;
		

#preparação para deletar o mais visitado e procurar o segundo mais visitado
i = 0
length = len(sectors)	
while (i < length):
	if (sectors[i] == firstVisited):
		sectors.remove (sectors[i])
		length = length -1
		continue
	i +=1;


#Segundo mais visitado
maior = 0;
for item in sectors:
	if sectors.count(item) > maior:
		maior = sectors.count(item);
		secondVisited = item;

print("O setor mais visitado: %s"%(firstVisited))
print("O segundo setor mais visitado: %s" %(secondVisited))


