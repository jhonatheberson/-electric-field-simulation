
# coding: utf-8

# In[1]:


#OBS: POR FAVOR COLOQUE O VALOR DA DISTANCIA INICIALMENTE IGUAL A 4 E CARGA IGUAL A 5 DEPOIS DISTANCIA IGUAL A 3 PARA MELHOR VISUALIZAÇÃO
#TESTE 1: D = 4, CARGA = 5, PERCEBE-SE QUE O COMPRIMENTO DAS SETAS SÃO MENORES POR CAUSA DO INTENCIDADE DO CAMPO SER MENOR DEVIDO TER MAIOR DISTANCIA EM RELAÇÃO A CARGA
#TESTE 2: D = 3, CARGA = 5, PERCEB-SE QUE O COMPRIMENTO DAS SETAS AUMENTOU DEVIDO A DISTANCIA SER MENOR, ASSIM MAIOR INTENCIDADE DO CAMPO
from vpython import*
import numpy as np
import math

#----- entrada de variaveis -----#
vetor = float(input('Digite o valor da distancia entre [1-6] : '))
q1 = float(input('Digite um valor de carga entre [1-6]: '))
while((vetor <= 0 or vetor > 6) or (vetor > q1)):
    print('Entrada incorreta, por favor digite novamente numero entra [0-5] e distancia menor que carga para melhor visualização')
    vetor = float(input('Digite o valor da distancia entre [1-6] : '))
    q1 = float(input('Digite um valor de carga entre [1-6]: '))
    
("")
dx = vetor
dy = vetor
dz = vetor
dx1 = dx/100
dy1 = dy/100
dz1 = dz/100
#----- entrada de variaveis -----#

#----- calculo da magnitude do campo elétrico -----#

d = sqrt(dx1**2+dy1**2+dz1**2) 
k = 9*(10**9)
qf = (q1/100)*(10**-9)
e = float((k*qf)/d**2)

#----- calculo da magnitude do campo elétrico -----#

#----- calculo da direção do vetor -----#

versor_x = (dx1)/d
versor_y = (dy1)/d
versor_z = (dz1)/d
direcao_x = e*versor_x
direcao_y = e*versor_y
direcao_z = e*versor_z
teste = vector(direcao_x,direcao_y,direcao_z)
mag_2 = vector(e,e,e)

#----- calculo da direção do vetor -----#

#----- impressões -----------------------#
print('E = k.q/d²')
print('E = {}'.format(e))
#----- impressões -----------------------#


#----- imagens --------------------------------------------------------------------------------------------------#
ref = sphere(pos=vector(0,0,0), radius = 10, color = color.yellow) # carga localizada no centro
#--------rotacionando vetor posiçao do ponto--------#

v1 = rotate(mag_2, angle=2*pi, axis=vector(0,0,0))
versor_1 = norm(vector(v1))
ortogonal_1 = versor_1*e

#--------rotacionando vetor posiçao do ponto--------#

#--------imprimendo seta e rotacionando seta delimitadora posiçao do ponto--------#

angulo = 0
n = 0
while(n < 24):
    angulo = angulo + 15
    pointer_n = arrow(pos=vector(direcao_x,direcao_y,direcao_z),axis = ortogonal_1, color = color.red,  shaftwidth=4)
    pointer_n.rotate(angle=radians(angulo), axis=vector(e,0,0), origin=vector(0,0,0))
    n = n + 1
    ("")
v2 = rotate(vector(direcao_x,direcao_y,direcao_z), angle=pi, axis=vector(0,0,0))
versor_2 = norm(vector(v2))
ortogonal_v2 = versor_2*e

#--------imprimendo seta e rotacionando seta delimitadora posiçao do ponto--------#

#--------rotacionando vetor posiçao do ponto 2--------#

v3 = rotate(mag_2, angle=pi, axis=vector(0,0,0))
versor_3 = norm(vector(v3))
ortogonal_3 = versor_3*e

#--------rotacionando vetor posiçao do ponto 2--------#

#--------imprimendo seta e rotacionando seta delimitadora posiçao do ponto--------#

k = 0
angulo = 0
while(k < 24):
    angulo = angulo + 15
    pointer_k = arrow(pos=vector(ortogonal_v2) ,axis = vector(ortogonal_3), color = color.red,  shaftwidth=4)
    pointer_k.rotate(angle=radians(angulo), axis=vector(e,0,0), origin=vector(0,0,0))
    k = k + 1
    ("")
    
#--------imprimendo seta e rotacionando seta delimitadora posiçao do ponto--------#   

#--------rotacionando vetor posiçao do ponto 3--------#

v4 = rotate(vector(direcao_x-20,direcao_y,direcao_z), angle=pi/2, axis=vector(0,0,0))
versor_4 = norm(vector(v4)) # nao consegui fazer o lanço condiciona nessa logica deu um bug ele não entra no laço
ortogonal_v4 = versor_4*e

#--------rotacionando vetor posiçao do ponto 3--------#

#--------imprimendo seta e rotacionando seta, entre as setas de delimitação posiçao do ponto--------#

x = 0
angulo_1 = 0
while(x < 24):
        angulo_1 = angulo_1 + 15
        pointer_x = arrow(pos=vector(direcao_x-20,direcao_y,direcao_z) ,axis = vector(ortogonal_v4), color = color.red,  shaftwidth=4)
        pointer_x.rotate(angle=radians(angulo_1), axis=vector(e,0,0), origin=vector(0,0,0))
        x = x + 1
("")

#--------imprimendo seta e rotacionando seta, entre as setas de delimitação posiçao do ponto--------#

#--------repetições da rotacição vetor posiçao do ponto 3 e imprimendo seta e rotacionando seta, entre as setas de delimitação posiçao do ponto
    
v4 = rotate(vector(direcao_x-30,direcao_y,direcao_z), angle=pi/2, axis=vector(0,0,0))
versor_4 = norm(vector(v4))
ortogonal_v4 = versor_4*e

# nao consegui fazer o lanço condiciona nessa logica deu um bug ele não entra no laço
x = 0
angulo_1 = 0
while(x < 24):
        angulo_1 = angulo_1 + 15
        pointer_x = arrow(pos=vector(direcao_x-30,direcao_y,direcao_z) ,axis = vector(ortogonal_v4), color = color.red,  shaftwidth=4)
        pointer_x.rotate(angle=radians(angulo_1), axis=vector(e,0,0), origin=vector(0,0,0))
        x = x + 1
("")
v4 = rotate(vector(direcao_x-40,direcao_y,direcao_z), angle=pi/2, axis=vector(0,0,0))
versor_4 = norm(vector(v4))
ortogonal_v4 = versor_4*e
# nao consegui fazer o lanço condiciona nessa logica deu um bug ele não entra no laço
x = 0
angulo_1 = 0
while(x < 24):
        angulo_1 = angulo_1 + 15
        pointer_x = arrow(pos=vector(direcao_x-40,direcao_y,direcao_z) ,axis = vector(ortogonal_v4), color = color.red,  shaftwidth=4)
        pointer_x.rotate(angle=radians(angulo_1), axis=vector(e,0,0), origin=vector(0,0,0))
        x = x + 1
("")
v4 = rotate(vector(direcao_x-50,direcao_y,direcao_z), angle=pi/2, axis=vector(0,0,0))
versor_4 = norm(vector(v4))
ortogonal_v4 = versor_4*e
# nao consegui fazer o lanço condiciona nessa logica deu um bug ele não entra no laço
x = 0
angulo_1 = 0
while(x < 24):
        angulo_1 = angulo_1 + 15
        pointer_x = arrow(pos=vector(direcao_x-50,direcao_y,direcao_z) ,axis = vector(ortogonal_v4), color = color.red,  shaftwidth=4)
        pointer_x.rotate(angle=radians(angulo_1), axis=vector(e,0,0), origin=vector(0,0,0))
        x = x + 1
("")
        
v4 = rotate(vector(direcao_x-60,direcao_y,direcao_z), angle=pi/2, axis=vector(0,0,0))
versor_4 = norm(vector(v4))
ortogonal_v4 = versor_4*e
# nao consegui fazer o lanço condiciona nessa logica deu um bug ele não entra no laço
x = 0
angulo_1 = 0
while(x < 24):
        angulo_1 = angulo_1 + 15
        pointer_x = arrow(pos=vector(direcao_x-60,direcao_y,direcao_z) ,axis = vector(ortogonal_v4), color = color.red,  shaftwidth=4)
        pointer_x.rotate(angle=radians(angulo_1), axis=vector(e,0,0), origin=vector(0,0,0))
        x = x + 1
("")
v4 = rotate(vector(direcao_x-70,direcao_y,direcao_z), angle=pi/2, axis=vector(0,0,0))
versor_4 = norm(vector(v4))
ortogonal_v4 = versor_4*e

x = 0
angulo_1 = 0
while(x < 24):
        angulo_1 = angulo_1 + 15
        pointer_x = arrow(pos=vector(direcao_x-70,direcao_y,direcao_z) ,axis = vector(ortogonal_v4), color = color.red,  shaftwidth=4)
        pointer_x.rotate(angle=radians(angulo_1), axis=vector(e,0,0), origin=vector(0,0,0))
        x = x + 1
("")
v4 = rotate(vector(direcao_x-80,direcao_y,direcao_z), angle=pi/2, axis=vector(0,0,0))
versor_4 = norm(vector(v4))
ortogonal_v4 = versor_4*e

x = 0
angulo_1 = 0
while(x < 24):
        angulo_1 = angulo_1 + 15
        pointer_x = arrow(pos=vector(direcao_x-80,direcao_y,direcao_z) ,axis = vector(ortogonal_v4), color = color.red,  shaftwidth=4)
        pointer_x.rotate(angle=radians(angulo_1), axis=vector(e,0,0), origin=vector(0,0,0))
        x = x + 1
("")
v4 = rotate(vector(direcao_x-90,direcao_y,direcao_z), angle=pi/2, axis=vector(0,0,0))
versor_4 = norm(vector(v4))
ortogonal_v4 = versor_4*e

x = 0
angulo_1 = 0
while(x < 24):
        angulo_1 = angulo_1 + 15
        pointer_x = arrow(pos=vector(direcao_x-90,direcao_y,direcao_z) ,axis = vector(ortogonal_v4), color = color.red,  shaftwidth=4)
        pointer_x.rotate(angle=radians(angulo_1), axis=vector(e,0,0), origin=vector(0,0,0))
        x = x + 1
("")

v4 = rotate(vector(direcao_x-100,direcao_y,direcao_z), angle=pi/2, axis=vector(0,0,0))
versor_4 = norm(vector(v4))
ortogonal_v4 = versor_4*e

x = 0
angulo_1 = 0
while(x < 24):
        angulo_1 = angulo_1 + 15
        pointer_x = arrow(pos=vector(direcao_x-100,direcao_y,direcao_z) ,axis = vector(ortogonal_v4), color = color.red,  shaftwidth=4)
        pointer_x.rotate(angle=radians(angulo_1), axis=vector(e,0,0), origin=vector(0,0,0))
        x = x + 1
        
v4 = rotate(vector(direcao_x-110,direcao_y,direcao_z), angle=pi/2, axis=vector(0,0,0))
versor_4 = norm(vector(v4))
ortogonal_v4 = versor_4*e

x = 0
angulo_1 = 0
while(x < 24):
        angulo_1 = angulo_1 + 15
        pointer_x = arrow(pos=vector(direcao_x-110,direcao_y,direcao_z) ,axis = vector(ortogonal_v4), color = color.red,  shaftwidth=4)
        pointer_x.rotate(angle=radians(angulo_1), axis=vector(e,0,0), origin=vector(0,0,0))
        x = x + 1
        
v4 = rotate(vector(direcao_x-120,direcao_y,direcao_z), angle=pi/2, axis=vector(0,0,0))
versor_4 = norm(vector(v4))
ortogonal_v4 = versor_4*e

x = 0
angulo_1 = 0
while(x < 24):
        angulo_1 = angulo_1 + 15
        pointer_x = arrow(pos=vector(direcao_x-120,direcao_y,direcao_z) ,axis = vector(ortogonal_v4), color = color.red,  shaftwidth=4)
        pointer_x.rotate(angle=radians(angulo_1), axis=vector(e,0,0), origin=vector(0,0,0))
        x = x + 1
        
v4 = rotate(vector(direcao_x-130,direcao_y,direcao_z), angle=pi/2, axis=vector(0,0,0))
versor_4 = norm(vector(v4))
ortogonal_v4 = versor_4*e

x = 0
angulo_1 = 0
while(x < 24):
        angulo_1 = angulo_1 + 15
        pointer_x = arrow(pos=vector(direcao_x-130,direcao_y,direcao_z) ,axis = vector(ortogonal_v4), color = color.red,  shaftwidth=4)
        pointer_x.rotate(angle=radians(angulo_1), axis=vector(e,0,0), origin=vector(0,0,0))
        x = x + 1 
        
v4 = rotate(vector(direcao_x-140,direcao_y,direcao_z), angle=pi/2, axis=vector(0,0,0))
versor_4 = norm(vector(v4))
ortogonal_v4 = versor_4*e

x = 0
angulo_1 = 0
while(x < 24):
        angulo_1 = angulo_1 + 15
        pointer_x = arrow(pos=vector(direcao_x-140,direcao_y,direcao_z) ,axis = vector(ortogonal_v4), color = color.red,  shaftwidth=4)
        pointer_x.rotate(angle=radians(angulo_1), axis=vector(e,0,0), origin=vector(0,0,0))
        x = x + 1
        
v4 = rotate(vector(direcao_x-150,direcao_y,direcao_z), angle=pi/2, axis=vector(0,0,0))
versor_4 = norm(vector(v4))
ortogonal_v4 = versor_4*e

x = 0
angulo_1 = 0
while(x < 24):
        angulo_1 = angulo_1 + 15
        pointer_x = arrow(pos=vector(direcao_x-150,direcao_y,direcao_z) ,axis = vector(ortogonal_v4), color = color.red,  shaftwidth=4)
        pointer_x.rotate(angle=radians(angulo_1), axis=vector(e,0,0), origin=vector(0,0,0))
        x = x + 1
        
v4 = rotate(vector(direcao_x-160,direcao_y,direcao_z), angle=pi/2, axis=vector(0,0,0))
versor_4 = norm(vector(v4))
ortogonal_v4 = versor_4*e

x = 0
angulo_1 = 0
while(x < 24):
        angulo_1 = angulo_1 + 15
        pointer_x = arrow(pos=vector(direcao_x-160,direcao_y,direcao_z) ,axis = vector(ortogonal_v4), color = color.red,  shaftwidth=4)
        pointer_x.rotate(angle=radians(angulo_1), axis=vector(e,0,0), origin=vector(0,0,0))
        x = x + 1
#--------repetições da rotacição vetor posiçao do ponto 3 e imprimendo seta e rotacionando seta, entre as setas de delimitação posiçao do ponto
#----- imagens -------------------------------------------------------------------------------------------#
#OBS: COMUNICAR QUE ESSES TRABALHOS TEVE MUITO EMPENHO POR MINHA PARTE, A QUAL DEDIQUEI MUITO A ELES, QUE PODERIA ESTAR FAZENDO A LISTA DO SR. QUE ACHO QUE SERIA MAIS PRODUTIVO, CONTUDO NÃO GOSTO DE INICIAR ALGUMA COISA E NÃO TERMINAR, POR ISSO ESPERO A DEVIDA CONTRIBUIÇÃO E MERECEDORA(PONTOS) POR ELES, E ACHO QUE SEREI O ÚNICO A ENTREGALOS.
#Respeitosamente,
#nome: Jhonat Heberson Avelino de Souza
#matrícula: 20160142138


# ##### 
