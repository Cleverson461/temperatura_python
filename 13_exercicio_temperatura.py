# Receba uma temperatura em farenhit e exiba em graus celsius.
# c = 5 * f - 32/9

farenhit = float(input('Digite uma temperatura em grau farenhit: '))
celsius = 5 * ((farenhit - 32) / 9)

print(f'A temperatura em graus celsius é {celsius:.2f}')