# Integrantes:
- RM553842 Gustavo Gouvêa Soares
- RM553945 Henrique Rafael Gomes de Souza
- RM554223 Pedro Henrique Mello Silva Alves

# Dependências e instruções:
- Caso já tenha instalado um ambiente python:
  - Instalar a biblioteca flask manualmente ou inserindo no terminal: pip install flask
- ou
- Caso não tenha instalado um ambiente python:
  - Para garantir que scripts locais, como o ambiente python, possam ser executados, acesse o terminal do PowerShell de seu Dispositivo, execute e confirme a mudança deste comando:
    - Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
  - Quando não houver mais a necessidade de um ambiente python, esta configuração pode ser revertida através da execução e confirmação do comando:
    - Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Restricted
  - No terminal PowerShell do VSCode, crie o ambiente python na mesma pasta que seus arquivos através do comando:
    - python -m venv myenv
  - Ative o ambiente através do comando:
    - .\myenv\Scripts\Activate.ps1
  - Instale a biblioteca flask inserindo no terminal:
    - pip install flask
## 
- Agora, para ter acesso ao menu, execute:
  - python main.py 
- Em outro terminal, para gerar sua API em http://127.0.0.1:5000/api/items, execute:
  - python app.py

# Funcionalidades:
- Leitura do arquivo dadosPacientes.json ou pacienteTeste.json, caso o primeiro ainda não exista
- Escrita no arquivo dadosPacientes.json
- Criação de uma API para o endereço http://127.0.0.1:5000/api/items
    
- Criação de uma ficha de paciente
- Atualização da ficha de um paciente, adicionando um novo ciclo
- Visualização de qualquer ciclo da ficha de um paciente
- Remoção de uma ficha de paciente
- Finalização de sessão
