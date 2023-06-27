from itertools import combinations
   

if __name__=='__main__':
    valores = [405.86,
    2540.74,
    2735.25,
    4005.26,
    15848.21,
    10158.86,
    2882.98,
    8938.47,
    4007.08,
    9348.67,
    9923.21,
    16907.47]
    soma_desejada = 51414.75 

    comb_encontrada = None

    for r in range(1, len(valores) + 1):
        comb = list(combinations(valores, r))
        for c in comb:
            if sum(c) == soma_desejada:
                comb_encontrada = c
                break

    if comb_encontrada:
        print(f"A combinação {comb_encontrada} tem a soma igual a {soma_desejada}.")
    else:
        print("Não foi encontrada uma combinação cuja soma é igual ao valor desejado.")
        



        