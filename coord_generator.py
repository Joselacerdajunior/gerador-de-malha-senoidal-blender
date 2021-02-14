import math

#largura e altura em centimetros
widthMesh = 200
heightMesh = 180

verticesDistance = 1
numHorizontalVertices = widthMesh / verticesDistance
numVerticalVertices = heightMesh / verticesDistance
numTotalVertices = numVerticalVertices * numHorizontalVertices

# geração da primeira linha
coord_L1 = ''

for axle_x in range(int(numHorizontalVertices)):
    produndity = 2
    y = produndity * math.sin( verticesDistance * axle_x)

    if axle_x == numHorizontalVertices-1:
        coord_L1 += f'({axle_x:.2f},{y:.2f},0.00)'
        continue

    coord_L1 += f'({axle_x:.2f},{y:.2f},0.00), '

# duplicando a primeira linha, porém com z diferente
coord_L1_bkp = coord_L1
for axle_z in range(int(numVerticalVertices)-1):
    coordenada_aux = coord_L1_bkp
    coord_z = verticesDistance * (axle_z + 1)
    coord_z_str = str('{:.2f}'.format(coord_z))
    coordenada_aux = coordenada_aux.replace('0.00)', str(coord_z_str)+')')
    coord_L1 = coord_L1 + ', ' + coordenada_aux


# preencher faces
coordinatesFace = ''
counter = 0
for point in range(int(numTotalVertices-1-numHorizontalVertices)):
    coordinatesFace_aux = ''
    if counter == numHorizontalVertices-1:
        counter = 0
        continue

    if point == (numTotalVertices-1-numHorizontalVertices-1):
        coordinatesFace_aux = '({:.2f},{:.2f},{:.2f}), ({:.2f},{:.2f},{:.2f})'.format(point, point + numHorizontalVertices, point + numHorizontalVertices + 1, point, point + 1, point + 1 + numHorizontalVertices)
        coordinatesFace += coordinatesFace_aux
        counter += 1
        break

    coordinatesFace_aux = '({:.2f},{:.2f},{:.2f}), ({:.2f},{:.2f},{:.2f}), '.format(point, point+numHorizontalVertices, point+numHorizontalVertices+1, point, point+1, point+1+numHorizontalVertices)
    coordinatesFace += coordinatesFace_aux
    counter += 1

#print('verts = [' + coord_L1 + ']')
#print('faces = [' + coordinatesFace + ']')

archive = open('coordenadas.txt','w')
archive.write('Width =' + str(widthMesh) + '\n')
archive.write('Height =' + str(heightMesh) + '\n')
archive.write('verts = [' + coord_L1 + ']\n')
archive.write('faces = [' + coordinatesFace + ']\n')
archive.close()