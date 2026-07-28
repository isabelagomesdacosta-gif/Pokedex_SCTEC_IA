#🎮 Desafio Prático: A Missão do Professor Carvalho!
#📜 O Enredo
#"Olá, jovem Treinador(a)! O Professor Carvalho precisa da sua ajuda. Ele desenvolveu um novo modelo de Pokédex em Python, mas a memória do dispositivo foi formatada! Sua missão é reescrever o sistema base da Pokédex para que os novos treinadores consigam registrar seus Pokémons, treinar a equipe e analisar estatísticas da sua jornada."

#🎯 Requisitos do Sistema (O que o código precisa ter)
#Seu programa deve conter obrigatoriamente:

#Estrutura de Dados:

#Usar um Dicionário chamado pokedex para armazenar os Pokémons.

#Menu Contínuo (while e Booleano):

#Usar um laço while com uma variável/flag booleana (rodando = True) para manter o sistema aberto até o usuário escolher a opção de desligar.

#Listagem e Relatório (for):

#Usar um laço for para percorrer o dicionário e listar o Nome, Tipo e Nível de cada Pokémon.

#Usar outro laço for (ou o mesmo) para calcular a média de nível de toda a equipe.

#Evolução/Treino (Lógica de Atualização):

#Uma opção no menu para treinar um Pokémon, o que aumenta o nível dele em +1.

# Dicionário para salvar os Pokémons
pokedex = {
    "Pikachu": {"tipo": "Elétrico", "nível": 5},
    "Charmander": {"tipo": "Fogo", "nível": 5},
    "Robson": {"tipo": "Madeira", "nível": 500}
 }

 # Variável booleana para manter o sistema ON
executando = True

print("\n===== 🔴⚪ POKÉDEX DIGITAL COM DICIONÁRIO 🔴⚪ =====")

 # Laço while
while executando:
     #Menu da POKÉDEX 
     print("\n===== 🔴⚪ MENU POKÉDEX 🔴⚪ =====")
     print("1 - Ver PODÉDEX Completa")
     print("2 - Registrar / Atualizar Pokémon")
     print("3 - Pesquisar Detalhes do Pokémon")
     print("4 - Soltar Pokémon")
     print("5 - Treinar Pokémon")
     print("6 - Média de nível da equipe")
     print("7 - Desligar Pokédex")

     #Lógica de cada opção
     opcao = input("Escolha uma opção (1 à 7): ")
 
     #OPÇÃO 1 - Ver PODÉDEX Completa
     if opcao == "1":
         print("\n --- SEUS POKÉMONS --- ")
         if not pokedex: # Verificar se o dicionário está vazio
            print("Nenhum Pokémon registrado na Pokédex.")
         else:
            for nome, dados in pokedex.items():
                 print(f"Nome: {nome:<12}")
                 print(f"Tipo: {dados['tipo']:<10}")
                 print(f"Nível: {dados['nível']}")
                 print("-" * 20)
         print(f"\nTotal de Pokémons registrados: {len(pokedex)}")
         print("-" * 30)

     #OPÇÃO 2 - Registrar / Atualizar Pokémon
     elif opcao == "2":
         nome = input("Digite o nome do Pokémon: ").strip().capitalize()
         tipo = input("Digite o tipo do Pokémon: ").strip().capitalize()
         nivel = int(input("Nível inicial: ").strip())

         pokedex[nome] = {
            "tipo": tipo,
         "nível": nivel
         }

         print(f"{nome} foi registrado/atualizado com sucesso!")
         print("-" * 30)

     #OPÇÃO 3 - Pesquisar Detalhes do Pokémon
     elif opcao == "3":
         busca = input("Digite o nome do Pokémon que deseja pesquisar: ").strip().capitalize()
    
         #Verificar se o Pokémon existe na Pokédex
         if busca in pokedex:
             dados = pokedex[busca] #Acessar os detalhes do Pokémon
             print(f"\nFICHA TÉCNICA DE {busca.upper()}:")
             print(f"Tipo: {dados['tipo']}")
             print(f"Nível: {dados['nível']}")
             print("-" * 30)
         else:
             print(f"Pokémon {busca} não encontrado na Pokédex.")
             print("-" * 30)

     #OPÇÃO 4 - Soltar Pokémon
     elif opcao == "4":
         soltar = input("Digite o nome do Pokémon que deseja soltar: ").strip().capitalize()
         if soltar in pokedex:
             del pokedex[soltar] #Remover o Pokémon do dicionário
             print(f"Pokémon {soltar} foi liberto da Pokédex.")
             print("-" * 30)
         else:
             print(f"Pokémon {soltar} não encontrado na Pokédex.")
             print("-" * 30)

     #OPÇÃO 5 - Treinar Pokémon
     elif opcao == "5":
         treino = input("Digite o nome do Pokémon que deseja treinar: ").strip().capitalize()

         if treino in pokedex:
             pokedex[treino]["nível"] += 1
             print(f"{treino} treinou e agora está no nível {pokedex[treino]['nível']}!")
             print("-" * 30)
         else:
             print("Pokémon não encontrado.")
             print("-" * 30)

     # OPÇÃO 6 - Média de nível da equipe
     elif opcao == "6":
         if not pokedex:
             print("Nenhum Pokémon registrado.")
             print("-" * 30)
         else:
             soma = 0
             for dados in pokedex.values():
                 soma += dados["nível"]
             media = soma / len(pokedex)
             print(f"Média de nível da equipe: {media:.2f}")
             print("-" * 30)

     #OPÇÃO 7 - Desligar Pokédex
     elif opcao == "7":      
         print("Desligando a Pokédex... Até a próxima, Treinador(a)!")
         print("-" * 30)
         executando = False #Alterar a flag para encerrar o loop
        
     else:
         print("Opção inválida. Por favor, escolha uma opção de 1 à 7.")
         print("-" * 30)
