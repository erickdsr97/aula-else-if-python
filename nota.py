nota = int(input())
if nota == 0:
    print('E')
elif nota >= 1 and nota <= 35:
    print('D')
elif nota >= 36 and nota <= 60:
    print('C')
elif nota >= 61 and nota <= 85:
    print('B')
elif nota >= 86 and nota <= 100:
    print('A')
# pode se usar if sempre para abrir a condição.
# e usar elif para adicionar quantas condições forem necessárias.