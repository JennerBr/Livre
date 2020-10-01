ColA  = 0
ColB  = 1
ColC  = 2
ColD  = 3
ColE  = 4
ColF  = 5
ColG  = 6
ColH  = 7
ColI  = 8
ColJ  = 9
ColK  = 10 
ColL  = 11
ColM  = 12
ColN  = 13
ColO  = 14
ColP  = 15
ColQ  = 16
ColR  = 17
ColS  = 18
ColT  = 19
ColU  = 20
ColV  = 21
ColW  = 22
ColX  = 23
ColY  = 24
ColZ  = 25
ColAA = 26
ColAB = 27
ColAC = 28
ColAD = 29
ColAE = 30
ColAF = 31
ColAG = 32
ColAH = 33    
ColAI = 34
ColAJ = 35
ColAK = 36
ColAL = 37
ColAM = 38
ColAN = 39
ColAO = 40
ColAP = 41
ColAQ = 42
ColAR = 43
ColAS = 44
ColAT = 45
ColAU = 46
ColAV = 47
ColAW = 48
ColAX = 49
ColAY = 50
ColAZ = 51

CT_Contato		  = ColA
CT_TP			  = ColB
CT_Fone	          = ColC
CT_IdSite	      = ColD
CT_CRM	          = ColE
CT_DtContato      = ColF
CT_Resposta	      = ColG
CT_Zona           = ColH
CT_Bairro	      = ColI
CT_Endereco	      = ColJ
CT_Complemento    = ColK
CT_Referencia     = ColL
CT_Cidade	      = ColM
CT_Estado         = ColN
CT_Cep            = ColO
CT_Grupo  	      = ColP
CT_CPF            = ColQ
CT_RazaoSocial    = ColR
CT_CNPJ           = ColS
CT_IE             = ColT
CT_Telefones      = ColU
CT_eMail          = ColV
CT_NF	          = ColW
CT_ET	          = ColX
CT_ObsInterna     = ColY
CT_ObsNota        = ColZ
CT_Indicadopor    = ColAA
CT_Div	          = ColAB
CT_Frete          = ColAC
CT_Km	          = ColAD
CT_PrazoAcordo    = ColAE
CT_Banco          = ColAF
CT_Saldo          = ColAG
CT_Preju          = ColAH
CT_ReprFone       = ColAI
CT_ReprNome       = ColAJ
CT_Comissao       = ColAK
CT_TotalFat       = ColAL
CT_MgLiq          = ColAM
CT_PercMgLiq      = ColAN
CT_Ticket         = ColAO
CT_MLMedia        = ColAP
CT_PrazoPg        = ColAQ
CT_Saldo          = ColAR
CT_PrimeiraCompra = ColAS
CT_WeekPrimCompra = ColAT
CT_UltCompra      = ColAU
CT_90DUltCompra   = ColAV
CT_DUC	          = ColAW

TP_Assunto = ColA
TP_Msg     = ColB

import pyautogui  #simula mouse e teclado
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#print(datetime.now())
startColtime = datetime.time()

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json')

gc = gspread.authorize(credentials)

ssCom = gc.open_by_key('1sgwr8TO8m87cXEg_LD8kxi9NruQ1OnBEuL6_GFWpJl4') # Comunica
abaComTemplate = ssCom.worksheet('Template')
selComTemplate = abaComTemplate.get_all_values()

while True:
	num = 0
	print( '\n---- GS-IO.PY -----')
	for row in selComTemplate:
		num=num+1
		if num > 1:
			print( str(num-1) + " " + row[TP_Assunto])

	t = input('Escolha um Template - (0 para cancelar): ')

	if t == "0":
		exit()
	elif int(t) > num-1:
		print('Opção inválida')
	else:
		break

t = int(t)

template = selComTemplate[t][TP_Msg]

abaComMsgWA    = ssCom.worksheet('MsgWA')
selComMsgWA    = abaComMsgWA.get_all_values()

try:
	waconectado = pyautogui.locateOnScreen('.png')
	print(waconectado[0]) # 'encontrei wa desconecado')	
except:
	raise ImageNotFoundException
	print('nao encontrou')
	pass

exit()

pyautogui.moveTo(1399,660,0.25,pyautogui.easeInElastic)
pyautogui.click(1399,660,button='left',duration=0.25)
pyautogui.click(1399,660,button='left',duration=0.25)
pyautogui.hotkey('command','a')
pyautogui.hotkey('del')
fone = '11 97521-1314'
pyautogui.write(fone)
pyautogui.hotkey('enter')
pyautogui.pause = 1

try:
	wanrok = pyautogui.locateOnScreen('wa nao encontrado.png')
except:
	print('wa ok')

print(fone + ' ok')

pyautogui.click(1724,1049,button='left',duration=0.25)
pyautogui.hotkey('command','a')
pyautogui.hotkey('del')
import pyperclip
pyperclip.copy('será que consigo acentuar ou não?')
pyautogui.hotkey('command','v')

exit()
ssDist = gc.open_by_key('1SXKrcRIFyp27UxgifJ4uoYhon2aNAFi6DkUCc5WzT5w') # Dist-py
abaDistContatos = ssDist.worksheet('Contatos')
selDistContatos = abaDistContatos.get_all_values()
dReenvio = datetime.date.today() - datetime.timedelta(days=30)

row = 1

while row < len(selDistContatos):
	print(selDistContatos[row][CT_DtContato])

	if selDistContatos[row][CT_DUC].isdigit() and int(selDistContatos[row][CT_DUC])>=30 and selDistContatos[row][CT_DtContato]=="":

		data     = str(datetime.date.today())
		datahora = str(datetime.datetime.today())
		nome     = selDistContatos[row][CT_Contato]
		nomePart = nome.partition(" ")
		fone     = '1197521-1314' # selDistContatos[row][CT_Fone]
		msg      = selComTemplate[t][TP_Msg].format(nomePart[0], str(selDistContatos[row][CT_UltCompra]))
		
		pyautogui.moveTo(1399,660,duration=0.25)
		pyautogui.click(1399,660,button='left',duration=0.25)
		pyautogui.click(1399,660,button='left',duration=0.25)
		pyautogui.hotkey('command','a')
		pyautogui.hotkey('del')
		pyautogui.typewrite(fone)
		pyautogui.hotkey('enter')
		pyautogui.typewrite(['tab','tab','Z','´'])
		pyautogui.pause = 1
		pyautogui.typewrite('e')
		
		#pyautogui.typewrite(msg)
		#pyautogui.hotkey('enter')

		print(msg)
		abaDistContatos.update_cell(row,CT_DtContato+1,data)
		abaComMsgWA.append_row([datahora,nome,fone,selComTemplate[t][TP_Assunto],msg])


	row = row + 1



#     if int(row[CT_DUC]) > 30:
#   	print(row[CT_Contato])

print(datetime.time() - startColtime)


#print(wks.colColvalues(1))


#for i in contatos:
#	print('linha ' + str(i) )
# = linha <Cell R99C10 'Rua Ferreira de Araújo, 410'>


	#for i range wks

#print(wks.getColallColrecords())