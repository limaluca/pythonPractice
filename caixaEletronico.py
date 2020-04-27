accountOne = [101,'Arnold',123,0];
accountTwo = [102,'Dolores',321,100];
accounts = [accountOne,accountTwo];
authenticatedAccount = [];
option = -1;

def bankLogo():
	print("\n\t\t| Banco UNDB |\n");

def mainMenu():
	print("Bem vindo ao autoatendimento! Insira o numero de uma das opcoes abaixo: \n");

	print("1. Inserir Cartao\n2. Deposito\n3. Desligar\n")


def subMenu():
	print("Insira o numero de uma das opcoes abaixo: \n");
	print("4. Saldo\n5. Saque\n6. Transferencia\n7. Voltar\n");


def errorMessage(errorType):
	print("\nErro:",errorType);

def sucessMessage(sucessType):
	bankLogo();
	print("Operacao realizada com sucesso! ",sucessType);

def authenticateAccount(ATMaccount,ATMpassword):
	counter = 0;
	ATMaccount = int(ATMaccount);
	ATMpassword = int(ATMpassword);

	for i in range(0,2):
		if ATMaccount == accounts[i][0] and ATMpassword == accounts[i][2]:
			authenticatedAccount = accounts[i];
			sucessMessage("Correntista autenticado. \n");
			return authenticatedAccount;
			break;

		elif counter == 0:
			 counter +=1;

		else:
			return False;
			break;

def validateAccount(accountToValidate):
	counter =0;
	accountToValidate = int(accountToValidate);
	validatedAccount = 1;
	for i in range(0,2):
		if accountToValidate == accounts[i][0]:
			validatedAccount = accounts[i];
			return validatedAccount;
			break;

		elif counter == 0:
			 counter +=1;

		else:
			errorMessage("Numero de conta inexistente.");
			return False;
			break;


def validateValue(value):
	if float(value) > 0:
		return True;
	else:
		errorMessage("Valor Invalido.");
		return False;


def deposit(depositAccount,depositValue):
	depositValue = float(depositValue);
	depositAccount = int(depositAccount);
	if validateAccount(depositAccount) and validateValue(depositValue):
		sucessMessage("Foram depositados R$%s na conta de numero %s." % (depositValue,depositAccount));
		validateAccount(depositAccount)[3]+=depositValue;
		print(validateAccount(depositAccount)[3]);
		
		return True
	else:
		return False;

def desligar():
	bankLogo();
	print("Relatorio de contas: \n")
	for i in range(0,2):
		print("Numero da conta: %d \nNome do titular: %s \nSaldo: $%d\n" % (accounts[i][0], accounts[i][1], accounts[i][3]));

def balance(balanceAccount):
	bankLogo();
	print('Nome: %s\nSaldo: $%s' % (balanceAccount[1],balanceAccount[3]));


def withdraw (withdrawAccount):
	while True:
		withdrawValue = float(input("\nInforme um valor para sacar: "));
		if validateValue(withdrawValue) and withdrawValue <= withdrawAccount[3]:
			print('Saldo atual: %s$\nValor Solicitado:%s$\nSaldo após saque: %s$\n' % (withdrawAccount[3],withdrawValue,withdrawAccount[3]-withdrawValue));
			
			while True:
				opcao = int(input('Digite 1 para confirmar a operacao ou 2 para voltar: '));
				if opcao == 1:
					withdrawAccount[3] -= withdrawValue;
					return sucessMessage("Voce acaba de sacar %s$." % (withdrawValue));
			
				elif opcao == 2:
					break;
				else:
					errorMessage("Opcao invalida.");
                    
		elif withdrawValue > withdrawAccount[3]:
			errorMessage("Valor para saque eh maior que seu saldo.");
            
#Na opção TRANSFEReNCIA, solicita o numero da conta de destino e o valor a ser transferido. Exibe o numero e nome da conta de origem e destino e o valor a ser transferido. Pede a confirmação e atualiza os dois saldos. Ponha mensagens se a conta de destino não existir ou se for a mesma de origem.

def transfer(transferReceiver,transferValue):
	transferReceiver = int(transferReceiver);
	transferValue = float(transferValue);

	if validateAccount(transferReceiver) and validateValue(transferValue):
		sucessMessage("Valor e contas validados");

		if authenticatedAccount[3] >= transferValue:
			print("Numero da conta: %s \nNome do titular: %s \nNumero da conta do receptor: %s \nNome do titular receptor: %s \nValor a ser transferido: $%s \n" % (authenticatedAccount[0],authenticatedAccount[1],transferReceiver[0],transferReceiver[1],transferValue));
			option = int(input("Digite 1 para confirmar operacao ou 2 para voltar. "))
			if option == 1:
				transferReceiver = validateAccount(transferReceiver);
				authenticatedAccount[3] -= transferValue;
				transferReceiver[3] += transferValue;
				return True;
			#Exibe o numero e nome da conta de origem e destino e o valor a ser transferido. 
			#Pede a confirmação e atualiza os dois saldos. 
		else:
			errorMessage("Seu saldo é insuficiente para esta transacao");
			return False;		
	else:
		return False;	



#Dando inicio ao programa
while True: 
	bankLogo();
	mainMenu();
	option = int(input());
	aux = -1;
	if option == 1:

		while True:
			authenticatedAccount = authenticateAccount(ATMaccount=input("Informe o numero da sua conta: \n"), ATMpassword=input("Informe a senha de sua conta: \n"));		
			if authenticatedAccount:
				while True:
					subMenu();
					option = int(input());
					if option == 4:
						while True:
							balance(authenticatedAccount)
							break;
					
					elif option == 5:
						if withdraw(authenticatedAccount):
							print("");

					elif option == 6:
						while True:
							if transfer(transferReceiver=int(input("Informe o numero da conta destino de sua transferencia: \n")), transferValue=float(input("Informe o valor a ser transferido: \n"))):
								break;
					elif option == 7:
						aux +=2;
						break;
				#Opcao para voltar ao menu principal			
			if aux != -1:
				break;
			else:
				errorMessage("Numero de conta inexistente ou senha invalida")
	
	elif option == 2:
		while True:
			bankLogo();
			if deposit(depositAccount=input("Informe o numero da conta destino de seu deposito: \n"), depositValue=float(input("Informe o valor a ser depositado: \n"))):
				break;

	elif option == 3:
		desligar();
		break;

#deposit(depositAccount,depositValue):













