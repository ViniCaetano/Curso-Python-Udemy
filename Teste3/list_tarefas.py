tarefas = []
tarefas_excluidas = []
def organizador():    
    while True:
        ação = int(input('Você quer:\n [1] Adicionar tarefa \n [2] Listar tarefas \n [3] Remover última tarefa inserida \n [4] Reincerir última tarefa removida \n'))
        if ação == 1:
            tarefas.append(input('Insira a tarefa: '))
            print(tarefas)
        elif ação == 2:
            print('\n A lista de tarefas é:')
            for i in tarefas:
                print (f'{tarefas.index(i)+1}. {i}')
            break
        elif ação == 3:    
            try:    
                for i in tarefas[-1]:
                    tarefas_excluidas.append(i)
                    del tarefas [-1]
                    print(tarefas)
                    continue
            except:
                print('Não há mais tarefas.')
        elif ação == 4:
            try:    
                for i in tarefas_excluidas[-1]:
                    tarefas.append(i)
                    del tarefas_excluidas [-1]
                    print(tarefas)
            except:
                    print('Não há mais tarefas excluídas.')            
        else:
            print('Digite uma das opçãoes disponíveis abaixo.')

organizador()