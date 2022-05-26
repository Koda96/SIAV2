import json
import collections

import numpy as npy
import random
import re
import os
from PIL import Image

size = (75, 75)
threshold = 60
tiempo = 20000
w = [[], []]

directorio = os.getcwd()

direntrenamiento = []
path = directorio + "/entrenamiento/"
for i in os.listdir(path):
    if re.match(r'[0-9a-zA-Z-_]*.jp[e]*g', i):
        direntrenamiento.append(path+i)

dirpruebas = []
def calcDir():
    path = directorio + "/pruebas/"
    
    dirpruebas.clear()
    dirpruebas.append(path + "image.jpg")

    '''for i in os.listdir(path):
        if re.match(r'[0-9a-zA-Z-_]*.jp[e]*g', i):
            dirpruebas.append(path + i)'''


def start():
    entradas = direntrenamiento
    global w


    print ("Creando matriz de peso")
    archivos = 0
    for path in entradas:
        print(path)
        x = ImagenaMatriz(file = path, size = size, threshold = threshold)
        x_vec = MatrizaVector(x)
        
        print (len(x_vec))

        if archivos == 0:
            w = matrizPeso(x_vec)
            archivos = 1
        else:
            aux_w = matrizPeso(x_vec)
            w = w + aux_w
            archivos += 1
    print ("La matriz de pesos ha sido creada")
    print (npy.matrix(w))
    calcDir()

def process():
    print(w)
    hopfield(pruebas = dirpruebas, tiempo = tiempo, size = size, threshold = threshold, directorio = directorio)

    return {"error": 0, "status": 'Success', "dir": directorio + "/output/after.jpeg"}


def upload_image(request):
    if request.method == 'POST':
        if 'file1' not in request.files:
            return {"error": 1, "status": 'No file sent'}
        else:
            file1 = request.files['file1']
            
            path = directorio + "/pruebas/image.jpg"
            file1.save(path)

            return {"error": 0, "status": 'Success', "dir": path}
    else:
        return {"error": 1, "status": 'Method not allowed'}






def MatrizaVector(x):
    m = x.shape[0] * x.shape[1]
    aux = npy.zeros(m)
    c = 0
    for i in range (x.shape[0]):
        for j in range (x.shape[1]):
            aux[c] = x[i,j]
            c += 1
    return aux

def matrizPeso(x):
    if len(x.shape) != 1:
        print("La entrada no es un vector")
        return
    else:
        w = npy.zeros([len(x),len(x)])
        for i in range(len(x)):
            for j in range (len(x)):
                if i != j:
                    w[i,j] = x[i]*x[j]
                    w[j,i] = w[i,j]
    return w
        
def ImagenaMatriz(file, size, threshold = 145):
    imagen = Image.open(file).convert(mode = "L") #Abrir la imagen y pasarla a blanco y negro
    imagen = imagen.resize(size)
    vectorimagen = npy.asarray(imagen, dtype = npy.uint8)
    x = npy.zeros(vectorimagen.shape, dtype = npy.float64)
    x[vectorimagen > threshold] = 1
    x[vectorimagen <= threshold] = -1
    return x

def ArrayaJPG(data, outFile = None):
    y = npy.zeros(data.shape, dtype = npy.uint8)
    y[data == 1] = 255
    y[data == -1] = 0
    imagen = Image.fromarray(y, mode = "L")
    if outFile is not None:
        imagen.save(outFile)
    return imagen

def update(m1_vec, tiempo = 100):
    global w
    for s in range(tiempo):
        m = len(m1_vec)
        i = random.randint(0, m-1)
        u = npy.dot(w[i][:], m1_vec)
        if u > 0:
            m1_vec[i] = 1
        elif u < 0:
            m1_vec[i] = -1
    return m1_vec

def hopfield(pruebas, tiempo = tiempo, size = size, threshold = threshold, directorio = None):
    
    c = 0

    print(pruebas)

    for path in pruebas:
        print("Path: " + path)
        m1 = ImagenaMatriz(file = path, size = size, threshold=threshold)
        oshape = m1.shape
        m1_vec = MatrizaVector(m1)
        m1_vec_aux = update(m1_vec = m1_vec, tiempo = tiempo)
        m1_vec_aux = m1_vec_aux.reshape(oshape)

        if directorio is not None:
            outfile = directorio + "/output/after.jpeg"
            print("file")
            ArrayaJPG(m1_vec_aux,outFile=outfile)
        else:
            print("file2")
            img = ArrayaJPG(m1_vec_aux, outFile = None)
            img.show()
        c += 1