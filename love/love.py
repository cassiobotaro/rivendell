matriz = []
nome = "amor"

for y in range(30, -30, -1):
    linha = []
    for x in range(-30, 30):
        if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (
            y * 0.1
        ) ** 3 <= 0:
            linha.append(nome[(x - y) % len(nome)])
        else:
            linha.append(" ")
    matriz.append("".join(linha))

print("\n".join(matriz))
