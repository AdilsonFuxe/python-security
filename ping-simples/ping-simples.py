# Importa o modulo ou biblioteca Os (integra os programas e recursos do sistema operaciomal)
import os

print("#" * 60)  # Impriminto 60 cardenais

# Lendo um valor e adicionando na variavel host
host = input("Digiste seu ip a ser verificado: ")

print("-" * 60)  # Impriminto 60 traços

# Chamando o medoto sistem do modulo os para executar comandos do sistema
os.system("ping -c6 {}".format(host))

print("-" * 60)  # Impriminto 60 traços
