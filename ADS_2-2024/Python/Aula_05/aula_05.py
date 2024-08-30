# Entrada de dados
idade = int(input("Digite a idade em números inteiros: "))

# Se idade for menor que 0, imprime "Não nasceu".
if idade < 0:
    print("Não nasceu.")
# Se não, verifica outra condicão.
else:
    # Se idade for menor que 16, imprime "Não vota".
    if idade < 16:
        print("Não vota.")
    # Se não, verifica outra condição.
    else:
        # Se idade for menor que 18, imprime "Voto opcional".
        if idade < 18:
            print("Voto opcional.")
        # Se não, verifica outra condição.
        else:
            # Se idade for menor que 61, verifica outras condições dentro do bloco if.
            if idade < 61:
                # Se idade for igual a 37, imprime "Ganha prêmio e não vota".
                if idade == 37:
                    print("Ganha prêmio e não vota.")
                # Se não, imprime "Voto obrigatório".
                else:
                    print("Voto obrigatório.")
            # Se não for menor que 61, verifica outra condição.
            else:
                # Se idade for igual a 74, imprime "Voto obrigatório, e ganha brinde".
                if idade == 74:
                    print("Voto obrigatório, e ganha brinde.")
                # Se não, imprime "Voto opcional".
                else:
                    print("Voto opcional.")