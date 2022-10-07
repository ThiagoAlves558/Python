valores = input().split()

tempo_da_viagem = int (valores[0])
velocidade_media = int (valores[1])
litros = (12)

resultado = (tempo_da_viagem * velocidade_media)

resultado2 = (resultado / litros)


print  (f" {resultado2:.3f}")