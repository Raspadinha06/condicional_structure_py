# Entrada de dados
idade = int(input("Digite a idade em números inteiros: "))

# Se a idade for menor que 0, imprimir "Não nasceu".
if idade < 0:
    print("Não nasceu.")
# Se não, verifica outra condição.
else:
    # Se a idade for menor que 16, imprimir "Não vota".
    if idade < 16:
        print("Não vota.")
    # Se não, verifica outra condição.
    else:
        # Se a idade for igual a 16, imprimir "Voto opcional". 
        if idade == 16:
            print("Voto opcional.")
        # Se não, verifica outra condição.
        else:
            # Se a idade for igual a 17, imprimir "Voto opcional". 
            if idade == 17:
                print("Voto opcional.")
            # Se não, verifica outra condição.
            else:
                # Se a idade for igual a 37, imprimir "Ganha um prêmio e não vota!". 
                if idade == 37:
                    print("Ganha um prêmio e não vota!")
                # Se não, verifica outra condição.
                else:
                    # Se a idade for igual a 74, imprimir "Voto obrigatório, porém ganha um brinde". 
                    if idade == 74:
                        print("Voto obrigatório, porém ganha um brinde.")
                    # Se não, verifica outra condição.
                    else:
                        # Se a idade for maior que 17, verifica as condições restantes. 
                        if idade > 17:
                            # Se a idade for maior que 16, imprime "Voto opcional". 
                            if idade > 60:
                                print("Voto opcional.")
                            # Se nenhuma condição declarada for verdadeira, imprime "voto obrigatório".
                            else:
                                print("Voto obrigatório.")
