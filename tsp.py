import itertools
quantidade_cidades= int(input("QUANTIDADE DE CIDADES: "))

nomes_cidades=[0 for x in range(quantidade_cidades)]
cidades=[]
for i in range(quantidade_cidades):
    nomes_cidades[i]=input(f"Nome da cidade[{i+1}]:").strip().upper()

#essa lista é inútil pois só estaria pegando os índices
#for i in range(quantidade_cidades):
    #cidades.append(i)



# Cria uma matriz n x n inicializada com zeros
cidades_distancias = [[0 for j in range(quantidade_cidades)] for i in range(quantidade_cidades)]











tipo_matriz=input("Qual tipo de matriz:Simétria ou assimétrica ?").strip().lower()





#EPRGUNTAR O PQ ESTAR PRINTIANDO O,1 OU 2 E PARTIR DAI


def tsp():
    # Preenche a matriz de distâncias (simétrica)
    for i in range(quantidade_cidades):
        for j in range(i + 1, quantidade_cidades):
            distancia = int(input(f"Distância entre {nomes_cidades[i]} e {nomes_cidades[j]}: "))
            cidades_distancias[i][j] = distancia
            cidades_distancias[j][i] = distancia  # Preenche o simétrico

    cidade_escolhida = input("Digite a cidade escolhida para começar e terminar: ").strip().upper()

    if cidade_escolhida in nomes_cidades:
        indice_escolhido = nomes_cidades.index(cidade_escolhida)
        indices_cidades = list(range(quantidade_cidades))
        indices_cidades.remove(indice_escolhido)

        menor_distancia = float('inf')
        melhor_rota = []

        print("\n=== TODAS AS POSSIBILIDADES DE ROTAS ===")

        for permutacao in itertools.permutations(indices_cidades):
            rota = [indice_escolhido] + list(permutacao) + [indice_escolhido]
            distancia_total = 0

            # Calcula a distância total da rota
            for i in range(len(rota) - 1):
                de = rota[i]
                para = rota[i + 1]
                distancia_total += cidades_distancias[de][para]

            # Imprime a rota atual
            print("\nRota:", end=" ")
            for idx in rota:
                print(nomes_cidades[idx], end=" -> ")
            print(f"Distância total: {distancia_total} km")

            # Verifica se é a melhor rota
            if distancia_total < menor_distancia:
                menor_distancia = distancia_total
                melhor_rota = rota

        # Após todas as permutações, mostra a melhor rota
        print("\n=== MELHOR ROTA ENCONTRADA ===")
        print("Melhor rota:", end=" ")
        for idx in melhor_rota:
            print(nomes_cidades[idx], end=" -> ")
        print(f"\nDistância total: {menor_distancia} km")

    else:
        print("Cidade inválida.")



def tsp_assimetrica():
    for i in range(quantidade_cidades):
        for j in range(quantidade_cidades):
            if i != j:
                distancia = int(input(f"Distância de {nomes_cidades[i]} para {nomes_cidades[j]}: "))
                #ESSES VALORES DE I E J SÃO AUTOMATICAMENTE OS VALORES DO LOOP QUE ESTÁ SENDO RODADO,A VARIÁVEL DISTÂNCIA
                #APENAS SERVE PARA GUARDAR ESSE VALORES
                cidades_distancias[i][j] = distancia


            else:
                # verificador para quando estiver colocando os valores com índices iguais
                cidades_distancias[i][j] = 0
    cidade_escolhida = input("Digite a cidade escolhida para começar e terminar: ").strip().upper()

    if cidade_escolhida in nomes_cidades:
        indice_escolhido = nomes_cidades.index(cidade_escolhida)
        indices_cidades = list(range(quantidade_cidades))
        indices_cidades.remove(indice_escolhido)

        menor_distancia = float('inf')
        melhor_rota = []

        print("\n=== TODAS AS POSSIBILIDADES DE ROTAS ===")

        for permutacao in itertools.permutations(indices_cidades):
            rota = [indice_escolhido] + list(permutacao) + [indice_escolhido]
            distancia_total = 0

            # Calcula a distância total da rota
            for i in range(len(rota) - 1):
                de = rota[i]
                para = rota[i + 1]
                distancia_total += cidades_distancias[de][para]

            # Imprime a rota atual
            print("\nRota:", end=" ")
            for idx in rota:
                print(nomes_cidades[idx], end=" -> ")
            print(f"Distância total: {distancia_total} km")

            # Verifica se é a melhor rota
            if distancia_total < menor_distancia:
                menor_distancia = distancia_total
                melhor_rota = rota

        # Após todas as permutações, mostra a melhor rota
        print("\n=== MELHOR ROTA ENCONTRADA ===")
        print("Melhor rota:", end=" ")
        for idx in melhor_rota:
            print(nomes_cidades[idx], end=" -> ")
        print(f"\nDistância total: {menor_distancia} km")

    else:
        print("Cidade inválida.")




    #for lista in cidades_distancias:
        #print(*lista)

    #CONFERIR NOMES DAS CIDADES
    #for x in nomes_cidades:
        #print(x)
    cidade_escolhida=input("Digite a cidade escolhida para começar e terminar(problema do caixeiro viajante):").strip().upper()
    if cidade_escolhida in nomes_cidades:
        #pega o índice do elemento dentro da lista nomes_cidades
        indice_escolhido = nomes_cidades.index(cidade_escolhida)

        # Len conta a quantidade de cidades,range torna essa quantidade em índices e lis,lista todos os índices
        indices_cidades = list(range(len(nomes_cidades)))
        indices_cidades.remove(indice_escolhido)

        #esse float("inf") serve para usar o infinito como referência para que possa ser feito a comparação
        menor_distancia = float('inf')
        melhor_rota = []

        # Gera todas as permutações possíveis (caminhos)
        #função itertools.permutations gera todas as permutações possíveis em relação a uma lista de números
        for permutacao in itertools.permutations(indices_cidades):
            rota = [indice_escolhido] + list(permutacao) + [indice_escolhido]  # começa e termina na cidade escolhida

            distancia_total = 0
            for i in range(len(rota) - 1):
                de = rota[i]
                para = rota[i + 1]
                #distancia_total = 0
                distancia_total += cidades_distancias[de][para]


       # print("\nRota:", end=" ")
       # for idx in rota:
           # print(nomes_cidades[idx], end=" -> ")
       # print(f"\nDistância total: {distancia_total} km")

        # Verifica se essa é a menor distância até agora

        # Exibe o resultado
        #print("\nMelhor rota encontrada:")
        #for idx in melhor_rota:
            #print(nomes_cidades[idx], end=" -> ")
       # print("\nDistância total:", menor_distancia, "km")

        print("\nRota:", end=" ")
        for idx in rota:
            print(nomes_cidades[idx], end=" -> ")
        print(f"\nDistância total: {distancia_total} km")









    else:
        print("Cidade inválida.")


if tipo_matriz in ["simétrica","simetrica"]:
    tsp()
if tipo_matriz in ["assimétrica","assimetrica","acimetrica","asimetrica"]:
    tsp_assimetrica()
