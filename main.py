import os
from datetime import date, datetime
from tabulate import tabulate
datastamp = datetime.now().date()
import pandas as pd  



codigo_cli = 1003
codigo_os = 6003

def cls():
    os.system(
        "cls" if os.name == "nt" else "clear"
    ) 
# cliente 1000 é o cliente Matriz ​🇧🇷​
dados_clientes = [
    {"cod_cli": "1000", "nome_cli": "Auto Adiv", "whatsapp": 31326598, "placa": "AAS5656"},
    {"cod_cli": "1001", "nome_cli": "Auto Bia", "whatsapp": 3265478, "placa": "DDD656"},
    {"cod_cli": "1002", "nome_cli": "Luck", "whatsapp": 31999998888, "placa": "BBB1234"},
    {"cod_cli": "1003","nome_cli": "Juliano","whatsapp": 31888887777,"placa": "CCC5678" }
]

dados_os = [
    {
        "codigo_os": "6001",
        "codigo_cli": "1000",
        "nome_cli": "Auto Adiv",
        "descricao": "Troca de óleo e filtros",
        "valor": "250.00",
        "data da entrega": "28/06/2026",
        "status": True,  # 🟢 Aberta
    },
    {
        "codigo_os": "6002",
        "codigo_cli": "1001",
        "nome_cli": "Auto Bia",
        "descricao": "Alinhamento e balanceamento",
        "valor": "180.00",
        "data da entrega": "29/06/2026",
        "status": True,  # 🟢 Aberta
    },
    {
        "codigo_os": "6003",
        "codigo_cli": "1002",
        "nome_cli": "Luck",
        "descricao": "Troca das pastilhas de freio",
        "valor": "320.00",
        "data da entrega": "25/06/2026",
        "status": False,  # 🔴 Fechada (Já entregue)
    },
]


"""def listar_cliente():
    # supondo que cada cliente seja um dicionário
    cabecalho = dados_clientes[0].keys()  # pega as chaves como cabeçalho
    linhas = [n.values() for n in dados_clientes]  # pega os valores
    
    print(tabulate(linhas, headers=cabecalho, tablefmt="grid"))"""

"""def listar_cliente():
    cabecalho = list(dados_clientes[0].keys())
    print("{:<15} {:<10} {:<25}".format(*cabecalho))  # cabeçalho
    
    for n in dados_clientes:
        print("{:<15} {:<10} {:<25}".format(*n.values()))"""
        
def listar_cliente():
    cabecalho = dados_clientes[0].keys()
    linhas = [n.values() for n in dados_clientes]
    print(tabulate(linhas, headers=cabecalho, tablefmt="grid", colalign=("center",)*len(cabecalho)))

"""def listar_Os():    
    cabecalho = dados_os[0].keys()
    linhas = [n.values() for n in dados_os]
    print(tabulate(linhas,headers=cabecalho, tablefmt="grid", colalign=("center",)*len(cabecalho)))"""

def listar_Os():    
    if not dados_os:
        print("Nenhuma ordem de serviço cadastrada.")
        return

    cabecalho = dados_os[0].keys()
    
    linhas = []
    for n in dados_os:
        # Transforma os valores em uma lista para podermos modificar o último elemento
        valores = list(n.values())
        
       valores[-1] = 'Aberto' if valores[-1] else 'Fechado'
        
        linhas.append(valores)
        
    print(tabulate(linhas, headers=cabecalho, tablefmt="grid", colalign=("center",)*len(cabecalho)))

def cadatrar_cliente():
 
    global codigo_cli   

    print("Cadastro de clientes")
    global codigo_cli
    codigo_cli +=1
    nome_cli = input("Digite o nome do cliente 👤 : ").strip() .upper()
    whatsapp = input("Digite o número do WhatsApp ​📞​: ").strip()
    placa = input("Digite a placa do veículo 🚗 : ").strip().upper()  .upper()

    novo_cliente = {
        "cod_cli": codigo_cli,
        "nome_cli": nome_cli,
        "whatsapp": whatsapp,
        "placa": placa
    }

    dados_clientes.append(novo_cliente)
    print("Cliente cadastrado com sucesso!")

def abrir_os():
    cls()
    global codigo_os
    codigo_os += 1
    
    # Pea a data atual do sistema (sem as horas) para usar na validação -
    datastamp = datetime.now().date()
    
    print("\n✨ NEW ORDER | CADASTRO DE ORDEM DE SERVIÇO ✨\n")
    print(f"Nova Ordem de Serviço n° {codigo_os}\n")
    
    # 1. Validação do Código do Cliente
    while True:
        try:
            codigo_cli = int(input("🔢 Digite o código do cliente: ").strip())
            break
        except ValueError:
            print("❌ Erro: Digite apenas números válidos!")
    
    # 2. Busca do Cliente
    cliente_encontrado = None
    for cliente in dados_clientes:
        if int(cliente["cod_cli"]) == codigo_cli:
            cliente_encontrado = cliente
            break
            
    # 3. Se encontrou o cliente, prossegue com os dados da OS
    if cliente_encontrado:
        nome_cli = cliente_encontrado["nome_cli"]
        print(f"✅ Cliente localizado: {nome_cli}\n")
        
        descricao = input("📝 Digite a descrição do serviço: ").strip()
        valor = input("💰 Digite o valor do serviço: ").strip()
        
        # 4. Validação da Data de Entrega (Seu segundo While no lugar certo)
        while True:
            try:
                data_input = input("📅 Digite a data de entrega (dd/mm/aaaa): ").strip()
                
                # Converte a string para data real
                data_entrega_convertida = datetime.strptime(data_input, "%d/%m/%Y").date()
                
                # Valida se é retroativa
                if data_entrega_convertida < datastamp:
                    print("❌ Erro: A data de entrega não pode ser menor que a data atual!")
                    continue 
                    
                break # Se a data for válida, sai do loop da data
                
            except ValueError:
                print("❌ Erro: Formato de data inválido! Digite no padrão dd/mm/aaaa.")
        
        nova_os = {
            "codigo_os": codigo_os,
            "codigo_cli": codigo_cli,
            "nome_cli": nome_cli,
            "descricao": descricao,
            "valor": valor,
            "data_entrega": data_input, # estou salvando a string formatada dd/mm/aaaa para exibição posterior
            "status": True
        }
        
        # Adiciona na lista global de OS
        dados_os.append(nova_os)
        print(f"\n🚀 Ordem de Serviço n° {codigo_os} cadastrada com sucesso!")
        
    else:
        print("❌ Código de cliente não encontrado! Cadastre o cliente primeiro.")
        codigo_os -= 1 
        return

def fechar_os():
    print("\n✨ FECHAR ORDEM DE SERVIÇO ✨\n")
    
    if not dados_os:
        print("❌ Não há nenhuma Ordem de Serviço cadastrada no sistema.")
        return
    
    # 1. Validação da digitação do Código da OS
    while True:
        try:
            codigo_busca = int(input("🔢 Digite o código da OS que deseja fechar: ").strip())
            break  # Sai do loop se for um número válido
        except ValueError:
            print("❌ Erro: Digite apenas números válidos!")
    
    # 2. Busca da OS dentro da lista dados_os
    os_encontrada = None
    for ordem in dados_os:
        
        id_os = ordem.get("codigo_os")
        
        if id_os is not None and int(id_os) == codigo_busca:
            os_encontrada = ordem
            break  
     
    if os_encontrada:
        # Verifica se ela já não está fechada
        if os_encontrada.get("status") == False:
            print(f"⚠️ A OS n° {codigo_busca} já se encontra FECHADA!")
        else:
            # Altera o status de True (Ativo) para False (Fechado)
            os_encontrada["status"] = False
            print(f"✅ Sucesso! A OS n° {codigo_busca} do cliente {os_encontrada.get('nome_cli')} foi FECHADA com sucesso.")
    else:
        print(f"❌ Erro: Ordem de Serviço n° {codigo_busca} não foi encontrada.")         

def caixa(): # este trecho foi criado com a ajuda do copilot
    # 1. VERIFICAÇÃO: Se a lista estiver vazia, não há como criar o df
    if not dados_os:
        print("❌ Não há nenhuma Ordem de Serviço cadastrada no sistema.")
        return

    # 2. DEFINIÇÃO: Criamos o df a partir da lista global dados_os
    df = pd.DataFrame(dados_os)
    
    # 3. TRATAMENTO: Convertemos a coluna para float para o .sum() funcionar
    df["valor"] = df["valor"].astype(float)
    
    # Apenas UM loop while controla o menu agora
    while True:
        print("\n=== MENU CAIXA ===")
        print("1 - Total geral")
        print("2 - Total aberto")
        print("3 - Total fechado")
        print("4 - Valor por cliente")
        print("5 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print(f"💰 Total geral: R$ {df['valor'].sum():.2f}")
            
        elif opcao == "2":
            # Filtra onde o status é True (Aberto)
            total_aberto = df[df["status"] == True]["valor"].sum()
            print(f"💰 Total aberto: R$ {total_aberto:.2f}")
            
        elif opcao == "3":
            # Filtra onde o status é False (Fechado)
            total_fechado = df[df["status"] == False]["valor"].sum()
            print(f"💰 Total fechado: R$ {total_fechado:.2f}")
            
        elif opcao == "4":
            print("\n💰 Valor por cliente:")
            # Agrupamento com Pandas salvando na variável
            resultado = df.groupby("nome_cli")["valor"].sum()
            
            # Loop limpo que remove o 'Name: valor, dtype: float64' do terminal
            for cliente, total in resultado.items():
                print(f" 👤 {cliente:<15} -> R$ {total:>8.2f}")
            
        elif opcao == "5":
            print("Encerrando caixa...")
            break
        else:
            print("❌ Opção inválida, tente novamente.")


##  =====================   Menu  ====================================
def exibir_menu():
    cls()
    print("┌────────────────────────────────────────────────┐")
    print("│         ⚙️  SISTEMA OS - SERVIÇOS MECÂNICOS     │")
    print("├────────────────────────────────────────────────┤")
    print("│                                                │")
    print("│  [ 1 ]  🔎 Listar Clientes                     │")
    print("│  [ 2 ]  ➕ Cadastrar Cliente                   │")
    print("│  [ 3 ]  📝 Registrar Nova OS                   │")
    print("│  [ 4 ]  📊 Consultar OS                        │")
    print("│  [ 5 ]  ✅ Baixar OS                           │")
    print("│  [ 6 ]  💰 Caixa                               │")
    print("│  [ 7 ]  ❌ Sair do Sistema                     │")
    print("│                                                │")
    print("└────────────────────────────────────────────────┘")

# --- FLUXO PRINCIPAL DO SISTEMA ---
while True:
    exibir_menu()
    opcao = input("👉 Escolha uma opção: ").strip()

    if opcao == "1":
        cls()
        listar_cliente()  
        input("\nPressione Enter para voltar ao menu...")

    elif opcao == "2":
        cls()
        cadatrar_cliente()
        input("\nPressione Enter para voltar ao menu...")

    elif opcao == "3":
        cls()
        abrir_os()  
        input("\nPressione Enter para voltar ao menu...")

    elif opcao == "4":
        cls()
        listar_Os()
        input("\nPressione Enter para voltar ao menu...")

    elif opcao == "5":
        cls()
        fechar_os()
        input("\nPressione Enter para voltar ao menu...")

    elif opcao == "6":
        cls()
        caixa()
        input("\nPressione Enter para voltar ao menu...")

    elif opcao == "7":
        cls()
        print("\n⚙️ Obrigado por utilizar o sistema. Até logo!")
        break  

    else:
        input("\n❌ Opção inválida! Digite um número de 1 a 7. (Enter)")

exibir_menu()        

