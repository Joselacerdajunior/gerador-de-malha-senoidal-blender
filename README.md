# gerador-de-malha-senoidal-blender
Script para geração de coordenadas de malha senoidal

Este script tem como função gerar as coordenadas necessárias para criar uma malha de formato senoidal no software Blender, facilitando a criação de cortinas.

### 1) Primeiros passos.
Primeiramente clone o arquivo **"Gerador_de_coordenadas_blender.py"**. Abra o arquivo para pré-configuração.

### 2) Modifique os parametros circulados na imagem de acordo com sua necessidade.

![alt text](https://github.com/Joselacerdajunior/gerador-de-malha-senoidal-blender/blob/main/img/image.png)

Atenção! valores muito altos podem gerar lentidão.
largura_da_cortina, é a largura total que a malha irá preencher no eixo x.
altura_da_cortina, é a altura no eixo z.
dist_pontos, distancia entre cada um dos pontos gerados.
profundidade_gomo, é a amplitude do sinal, possibilitando fazer gomos mais acentuados ou mais redondos.
y, cálculo responsável por gerar as variações no eixo y (a formula pode ser alterada).

### 3) Após configurado, execute o script python e localize o arquivo que foi gerado de nome "coordenadas.txt", abra-o:
Com o documento de texto aberto, copie todo o conteúdo que estiver abaixo da largura e altura.

![alt text](https://github.com/Joselacerdajunior/gerador-de-malha-senoidal-blender/blob/main/img/coordenadas.png)

### 4) Abra o Blender
a) Delete a figura primitiva na tela inicial utilizando o comando (SHIFT + X) e pressione DELETE.
b) Clique na aba de script python (demarcado em vermelho).

![alt text](https://github.com/Joselacerdajunior/gerador-de-malha-senoidal-blender/blob/main/img/blender-home.png)

c) Crie um novo arquivo de texto clicando no botão demarcado em vermelho.

![alt text](https://github.com/Joselacerdajunior/gerador-de-malha-senoidal-blender/blob/main/img/script.png)

d) Copie o conteúdo do arquivo "script_base.txt" e cole no campo de texto do aplicativo Blender.
e) Em seguida substitua os valores de "verts" e "faces" pelos valores copiados no passo 3.
f) Execute o script, e a malha será gerada.

![alt text](https://github.com/Joselacerdajunior/gerador-de-malha-senoidal-blender/blob/main/img/malha.png)
![alt text](https://github.com/Joselacerdajunior/gerador-de-malha-senoidal-blender/blob/main/img/malha2.png)
