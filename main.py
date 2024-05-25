import random as rd
import json

def valida_opcao(frase, opcoes):
   opcao = input(frase)
   while not opcao in opcoes:
       print(f'\n\tOpcão inválida! Escolha entre:')
       print("\n".join(opcoes))
       opcao = input(frase)
   return opcao


def invalida_opcao(frase, opcoes):
   opcao = input(frase)
   while opcao in opcoes:
       print(f'\n\tOpcão já cadastrada!')
       opcao = input(frase)
   return opcao


def pergunta_cpf(lista_pacientes, frase_selecionar_cpf):
   cpf_pacientes = []
   for elem in lista_pacientes.keys():
       cpf_pacientes.append(elem)
   cpf_escolhido = valida_opcao(frase_selecionar_cpf, cpf_pacientes)
   return cpf_escolhido


def selecionar(dados_paciente, pergunta_selecionar_ciclo_1, opcoes_selecionar_ciclo, pergunta_selecionar_ciclo_2):
   ciclo_escolhido = valida_opcao(pergunta_selecionar_ciclo_1, opcoes_selecionar_ciclo)
   selecionar_print(ciclo_escolhido, dados_paciente, pergunta_selecionar_ciclo_2)
   return


def selecionar_print(tipo_print, dados_paciente, pergunta_selecionar_ciclo_2):
   if tipo_print == '1':
       for elem in dados_paciente.keys():
           if elem == "Nome":
               print(f"\n{elem}: {dados_paciente[elem]}")
           elif elem != "Exames/Consultas realizados" and elem != "Exames/Consultas atuais":
               print(f"{elem}: {dados_paciente[elem][-1]}")
           else:
            eventos = "\n-".join(dados_paciente[elem])
            print(f"{elem}:\n-{eventos}")
   else:
       ciclos = []
       for elem in dados_paciente["Ciclo"]:
           ciclos.append(elem)
       ciclo_escolhido = valida_opcao(pergunta_selecionar_ciclo_2, ciclos)
       for elem in dados_paciente.keys():
           if elem == "Nome":
               print(f"\n{elem}: {dados_paciente[elem]}")
           elif elem != "Exames/Consultas realizados" and elem != "Exames/Consultas atuais":
               print(f"{elem}: {dados_paciente[elem][int(ciclo_escolhido) - 1]}")
           else:
               eventos = "\n-".join(dados_paciente[elem])
               print(f"{elem}:\n-{eventos}")
   return


def atualizar(dados_paciente, novo=False):
   for elem in dados_paciente.keys():
       anotar = ""
       if elem == "Nome":
           continue
       if elem == "Ciclo":
           if novo == False:
            ciclo = int(dados_paciente[elem][-1]) + 1
            dados_paciente[elem].append(f"{ciclo}")
           else:
               dados_paciente[elem].append('1')
           continue
       elif elem == "Pressao":
           numero_random_1 = rd.randint(10, 12)
           numero_random_2 = rd.randint(6, 8)
           anotar = f"{numero_random_1}/{numero_random_2}"
       elif elem == "Temperatura":
           anotar = f"{rd.randint(1,5)*0.2 +36}"
       elif elem == "Batimentos":
           anotar = f"{rd.randint(50,100)}"
       elif elem == "Exames/Consultas atuais":
           anotar_string = input(f"\nQual os/as {elem}?(separe-os apenas por: / )\n>")
           anotar_string = anotar_string.lower()
           anotar = anotar_string.split("/")
           if novo == False:
            for count in range(len( dados_paciente[elem] )):
                if dados_paciente[elem][0] and dados_paciente[elem][0] not in dados_paciente["Exames/Consultas realizados"] and dados_paciente[elem][0] not in anotar:
                    dados_paciente["Exames/Consultas realizados"].append( dados_paciente[elem][0] )
                del dados_paciente[elem][0]
            dados_paciente[elem] = anotar[:]
            print(f"\nRegistro do paciente atualizado com sucesso!", end='')
            continue
           else:
                dados_paciente[elem] = anotar[:]
                dado_anotar = input("\nQuais os últimos exames/consultas realizados?(separe os exames por: / )\n>")
                dado_anotar = dado_anotar.lower()
                dados_paciente["Exames/Consultas realizados"].extend(dado_anotar.split("/"))
                continue
       if elem != "Exames/Consultas realizados":
           dados_paciente[elem].append(anotar)
   return


def criar(lista_pacientes, pergunta_criar_cpf):
   cpfs_existentes = (elem for elem in lista_pacientes.keys())
   novo_cpf = invalida_opcao(pergunta_criar_cpf, cpfs_existentes)
   try:
       int(novo_cpf)
   except:
       print("\nValor não numérico inserido! Insira outro valor", end="")
       novo_cpf = invalida_opcao(pergunta_criar_cpf, cpfs_existentes)
   novo_nome = input(f"\nQual o nome do paciente de cpf:{novo_cpf}?\n>")
   lista_pacientes.update({novo_cpf: {
       "Nome": novo_nome,
       "Ciclo": [],
       "Pressao": [],
       "Temperatura": [],
       "Batimentos": [],
       "Exames/Consultas atuais": [],
       "Exames/Consultas realizados": []
   }})
   atualizar(lista_pacientes[novo_cpf], True)
   print(f"\nRegistro do paciente de cpf {novo_cpf} criado com sucesso!", end='')
   return


def deletar(lista_pacientes, cpf_escolhido):
   lista_chaves = []
   for elem in lista_pacientes.keys():
       lista_chaves.append(elem)
   if len(lista_chaves) < 2:
       print("\nDeve ter mais de um paciente cadastrado para que algum possa ser deletado!")
   else:
       del lista_pacientes[cpf_escolhido]
       print(f"\nRegistro do paciente de cpf {cpf_escolhido} deletado com sucesso!", end='')
   return


def main():
   pergunta_crud = f"\nVocê deseja:\n\tVer a ficha de um paciente[1]\n\tAtualizar a ficha de um paciente[2]\n\tCriar uma ficha de paciente[3]\n\tDeletar uma ficha de paciente[4]\n\tFinalizar sessão[5]\n>"
   opcoes_crud = ['1', '2', '3', '4', '5']
   frase_selecionar_cpf = "\nDigite o cpf do paciente que deseja acessar:\n>"
   pergunta_selecionar_ciclo_1 = "\nUtilizar último ciclo[1] ou ciclo em específico[2]?\n>"
   opcoes_selecionar_ciclo = ['1', '2']
   pergunta_selecionar_ciclo_2 = "\nQual ciclo deseja utilizar?\n>"
   pergunta_criar_cpf = "\nQual o cpf do novo usuário a ser cadastrado?\n>"


   while True:
       try:
        arquivo = open('dadosPacientes.json', 'r')
        pacientes = json.load(arquivo)
        arquivo.close()
       except:
        arquivo = open('pacienteTeste.json', 'r')
        pacientes = json.load(arquivo)
        arquivo.close()

       opcao_crud = valida_opcao(pergunta_crud, opcoes_crud)
       if opcao_crud == '1':
           selecionar(pacientes[pergunta_cpf(pacientes, frase_selecionar_cpf)], pergunta_selecionar_ciclo_1, opcoes_selecionar_ciclo, pergunta_selecionar_ciclo_2)
       elif opcao_crud == '2':
           atualizar(pacientes[pergunta_cpf(pacientes, frase_selecionar_cpf)])
       elif opcao_crud == '3':
           criar(pacientes, pergunta_criar_cpf)
       elif opcao_crud == '4':
           deletar(pacientes, pergunta_cpf(pacientes, frase_selecionar_cpf))
       else:
           break
       
       arquivo = open('dadosPacientes.json', 'w')
       dicio_json = json.dumps(pacientes, ensure_ascii=False, indent=4)
       arquivo.write(dicio_json)
       arquivo.close()
   return


main()