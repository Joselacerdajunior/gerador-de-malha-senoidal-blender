import math

#largura e altura em centimetros
largura_cortina = 200
altura_cortina = 180

dist_pontos = 1
num_pontos_horizontal = largura_cortina / dist_pontos
num_pontos_vertical = altura_cortina / dist_pontos
num_pontos_total = num_pontos_vertical * num_pontos_horizontal

# geração da primeira linha
coordenada_l1 = ''

for eixo_x in range(int(num_pontos_horizontal)):
    profundidade_gomo = 2
    y = profundidade_gomo * math.sin( dist_pontos * eixo_x)

    if eixo_x == num_pontos_horizontal-1:
        coordenada_l1 += f'({eixo_x:.2f},{y:.2f},0.00)'
        continue

    coordenada_l1 += f'({eixo_x:.2f},{y:.2f},0.00), '

# duplicando a primeira linha, porém com z diferente
coordenada_l1_bkp = coordenada_l1
for eixo_z in range(int(num_pontos_vertical)-1):
    coordenada_aux = coordenada_l1_bkp
    coord_z = dist_pontos * (eixo_z + 1)
    coord_z_str = str('{:.2f}'.format(coord_z))
    coordenada_aux = coordenada_aux.replace('0.00)', str(coord_z_str)+')')
    coordenada_l1 = coordenada_l1 + ', ' + coordenada_aux


# preencher faces
coordenada_faces = ''
contador = 0
for ponto in range(int(num_pontos_total-1-num_pontos_horizontal)):
    coordenada_faces_aux = ''
    if contador == num_pontos_horizontal-1:
        contador = 0
        continue

    if ponto == (num_pontos_total-1-num_pontos_horizontal-1):
        coordenada_faces_aux = '({:.2f},{:.2f},{:.2f}), ({:.2f},{:.2f},{:.2f})'.format(ponto, ponto + num_pontos_horizontal, ponto + num_pontos_horizontal + 1, ponto, ponto + 1, ponto + 1 + num_pontos_horizontal)
        coordenada_faces += coordenada_faces_aux
        contador += 1
        break

    coordenada_faces_aux = '({:.2f},{:.2f},{:.2f}), ({:.2f},{:.2f},{:.2f}), '.format(ponto, ponto+num_pontos_horizontal, ponto+num_pontos_horizontal+1, ponto, ponto+1, ponto+1+num_pontos_horizontal)
    coordenada_faces += coordenada_faces_aux
    contador += 1

#print('verts = [' + coordenada_l1 + ']')
#print('faces = [' + coordenada_faces + ']')

arquivo = open('coordenadas.txt','w')
arquivo.write('Largura =' + str(largura_cortina) + '\n')
arquivo.write('Altura =' + str(altura_cortina) + '\n')
arquivo.write('verts = [' + coordenada_l1 + ']\n')
arquivo.write('faces = [' + coordenada_faces + ']\n')
arquivo.close()