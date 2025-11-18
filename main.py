
from grafos_lib import Lista_Grafo
def main():

    print("1 - Usar Lista de Adjacência \n"
          "2 - Usar Matriz de Adjacência")

    escolha = input("Escolha a opção (1 ou 2): ").strip()

    entrada = input("Digite o caminho do arquivo de entrada .txt do grafo: ").strip()

    saida = input("Digite o caminho de saída .txt: ").strip()

    if escolha == "1":
        print("\nLista de adjacência escolhida")
        Lista_Grafo.ler_de_arquivo(entrada)
        print("Grafo carregado com sucesso!")
        print("Qual função deseja chamar?")
        funcao = input("1 - Resumo do grafo \n"
                       "2 - Busca em Largura \n"
                       "3 - Busca em Profundidade \n"
                       "4 - Componentes conexos").strip()

        if funcao == 1:
            Lista_Grafo.salvar_resumo(saida)
        elif funcao == 2:
            origem = input("Defina a origem da busca em largura").strip()
            Lista_Grafo.busca_largura(origem)
            Lista_Grafo.salvar_busca_largura(origem, saida)
        elif funcao == 3:
            origem = input("Defina a origem da busca em profundidade").strip()
            Lista_Grafo.busca_profundidade(origem)
            Lista_Grafo.salvar_busca_profundidade(origem, saida)
        elif funcao == 4:
            Lista_Grafo.componentes_conexos()
            Lista_Grafo.salvar_componentes(saida)
        else:
            print("Opção inválida!")
            return 

    elif escolha == "2":
        print("\nMatriz de Adjacência escolhida")
        Matriz_Grafo.ler_de_arquivo(entrada)
        print("Grafo carregado com sucesso!")

        print("Qual função deseja chamar?")
        funcao = input("1 - Resumo do grafo \n"
                       "2 - Busca em Largura \n"
                       "3 - Busca em Profundidade \n"
                       "4 - Componentes conexos").strip()

        if funcao == 1:
            Matriz_Grafo.salvar_resumo(saida)
        elif funcao == 2:
            origem = input("Defina a origem da busca em largura").strip()
            Matriz_Grafo.busca_largura(origem)
            Matriz_Grafo.salvar_busca_largura(origem, saida)
        elif funcao == 3:
            origem = input("Defina a origem da busca em profundidade").strip()
            Matriz_Grafo.busca_profundidade(origem)
            Matriz_Grafo.salvar_busca_profundidade(origem, saida)
        elif funcao == 4:
            Matriz_Grafo.componentes_conexos()
            Matriz_Grafo.salvar_componentes(saida)
        else:
            print("Opção inválida!")
            return
        
    else:
        print("Opção inválida!")
        return
    

if __name__ == "__main__":
    main()
