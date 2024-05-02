N = int(input())
nums_recibidos = [False] * 13

for i in range(N):
    valor = int(input())
    nums_recibidos[valor - 1] = True

inicio, final, a, b = -1, -1, -1, -1
for i in range(13):
    if nums_recibidos[i]:  # se tiene la ficha de número i+1
        if a < 0:
            a = i + 1
        b = i + 2
    else:  # se acabó la consecución
        if b - a >= final - inicio:
            inicio, final = a, b
            a = -1
            b = -1
if b - a >= final - inicio:
    inicio, final = a, b

print([i for i in range(inicio, final)])
