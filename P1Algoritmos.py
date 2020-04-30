#	------------- 1 -------------
name = str(input("Informe o seu nome: "))

grades = str(input(name+ ", agora informe suas tres notas separadas por UM espaço: "));

absences = int(input("Informe o numero de suas faltas neste semestre, sem mentir hein, "+ name + ": ")) 

grades = grades.split();

media = (float(grades[0])+float(grades[1])+float(grades[2]))/3

print(name+", aqui está seu resultado: ")
if (absences > 20):
	print("Você foi reprovado por faltas, pois superou as faltas permitidas, tendo %d ausencias em um semestre." % absences);
elif (media < 7.0):
	print("Você foi reprovado por média insufiente. Você deveria ter pelo menos 7.0 de média e infelizmente obteve a media de %d." % media)
else:
	print("Você foi aprovado!")


#	------------- 2 -------------

age = int(input("Informe sua idade: "))

if age <= 10:
	print("O valor do plano para pessoas com %d anos é de R$ 30,00" % age)
elif age > 10 and age <= 29:
	print("O valor do plano para pessoas com %d anos é de R$ 60,00" % age)
elif age > 29 and age <= 45:
	print("O valor do plano para pessoas com %d anos é de R$ 120,00" % age)
elif age > 45 and age <=59:
	print("O valor do plano para pessoas com %d anos é de R$ 150,00" % age)
else:
	print("O valor do plano para pessoas com mais de 59 anos é de R$ 300,00" % age)


#	------------- 3 -------------

salary = float(input("Informe o valor de seu salario: "))

if salary <= 500:
	salary = (salary * 0.05) + salary + 150

elif salary > 500 and salary <= 600:
	salary = (salary * 0.012) + salary + 150

elif salary > 500 and salary <= 1200:
	salary = (salary * 0.012) + salary + 100

elif salary > 1200:
	salary =  salary + 150

print("Salario acrescido de beneficios: %d" % salary)
	

#	------------- 4 -------------

hour = int(input("Informe quantas horas voce ficou estacionado: "))
toPay = -1;
print("Lendo...")

if hour == 1:
	toPay = 4

elif hour == 2:
	toPay = 6

elif hour > 2:
	toPay = 6 + (hour-2)

print("Por ter ficado %d horas no estacionamento, o valor deste ticket é de R$%d,00. Pague em um dos nossos quiosques. " % (hour, toPay))


#	------------- 5 -------------


firstMan = int(input("Informe a idade do primeiro homem: "))

secondMan = int(input("Informe a idade do segundo homem: "))

firstWoman = int(input("Informe a idade da primeira mulher: "))

secondWoman = int(input("Informe a idade da segunda mulher: "))

olderMan = firstMan;
youngerMan = secondMan;

if olderMan < youngerMan:
	youngerMan = olderMan;
	olderMan = secondMan

olderWoman = firstWoman;
youngerWoman = secondWoman;

if olderWoman < youngerWoman:
	youngerWoman = olderWoman;
	olderWoman = secondWoman

print("Idade do homem mais velho somada com a idade da mulher mais nova: %d" % (olderMan + youngerWoman))

print("Produto da idade do homem mais novo com a idade mulher mais velha: %d" % (youngerMan * olderWoman))






