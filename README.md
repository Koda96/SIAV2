#   Trabajo final - Modelo de Hopfield - SIA 2021

##  Integrantes
-   Asis, Butros
-   Barozzi Behr, Juan Ignacio
-   Varela, Gaspar

##  Introducción
El trabajo consiste en construir una red neuronal artificial de Hopfield que sea capaz de reconocer imágenes en blanco y negro.  

Dicha red neuronal logra manejar dos conjuntos de vectores de entrada: un conjunto es  utilizado  para  entrenamiento  y  otro  para  test  y  reconocimiento.  
Esta red es capaz de entrenar y reconocer imágenes.  

##  Fundamentos teóricos
El Modelo de Hopfield es un modelo neuronal muy bueno para entrenar y reconocer patrones.  
Se lo denomina de memoria asociativa ya que permite siempre reconocer, a partir de un patrón de entrada, alguno de los patrones entrenados.  
Junto con la ventaja de que la red siempre converja a un patrón entrenado, trae consigo el inconveniente de que esa convergencia sea errónea.  

Debemos tener en cuenta que los elementos del conjunto de entrada deben ser lo más ortogonales posible, es decir, que sean lo más diferentes posible.  

Se utiliza un modelo discreto a través de una función escalón: se utilizan los valores 1 y -1.  

Es un modelo no supervisado, es decir que conocemos las entradas y las salidas, pero el proceso por el cual se llegó a ese resultado es desconocido.  

Se necesitan muchas neuronas y mucho poder de cálculo.  


##  Por qué lo elegimos
Nos pareció más interesante a la hora de programar y poder comprender mejor cómo fuciona una red neuronal.  
Además, nos dio la posibilidad de poder plantear una aplicación que nos permita utilizar esta red programándola de una manera modular, teniendo por un lado una API que se encarga del procesamiento de datos en el backend y una interfaz gráfica amigable que pueda ser utilizada por el usuario final.  


##  Aplicación final
Nuestra aplicación cuenta con una interfaz amigable para el usuario en la cual se puede elegir una imagen desde el disco duro para posteriormente procesarla y poder de esta forma visualizar la imagen a la que convergió la red en base al entrenamiento previamente realizado.  

Por otro lado, también contamos con una API REST encargada de realizar el procesamiento de datos y el manejo de peticiones desde la aplicación.  
Al correr la API en el backend, se comienza a realizar el entrenamiento para calcular la matriz de pesos W y de esta forma ahorrarle futuras esperas al usuario.  
Para el cálculo de la matriz de pesos W, se recorren todas las imágenes de entrenamiento convirtiéndolas a una matriz y posteriormente a un vector (habiéndolas transformado a formato blanco y negro, y redimensionándolas a un tamaño único para todas antes de comenzar).  
Luego se utiliza este vector resultante para multiplicarlo por su transpuesta y así conseguir su matriz de peso correspondiente (con la diagonal principal en 0, ya que no se permiten relaciones de un nodo consigo mismo).  
Para finalizar y conseguir la matriz de pesos W resultante, realizamos la suma de todas las matrices conseguidas de cada imagen.  

La primera petición que se realiza desde la aplicación es la de poder añadir al conjunto de pruebas la imagen elegida por el usuario.  
Una vez realizado esto, se procede a procesar dicha imagen consiguiendo una convergencia a alguno de los patrones de entrenamiento, para posteriormente mostrar dicha imagen en la aplicación como resultado del proceso.  

Para procesar la imagen de entrada, lo que se hace es convertir la imagen a una matriz (previamente habiéndola pasado a formato blanco y negro) para luego pasarla a un vector, el cual se utilizará para realizar el producto punto con la matriz de pesos W calculada con anterioridad y así conseguir una convergencia en la red.  
Como último paso, procedemos a transformar este vector resultante nuevamente en una imagen, para finalmente almacenarla como una salida de la red en un directorio específico y que así pueda ser mostrada al usuario.  

Mientras estuvimos realizando las pruebas pertinentes, pudimos notar algunas inconsistencias con los patrones a los que se convergía.  
Debido a la transformación de las imágenes a blanco y negro y su posterior redimensionamiento, existe una pequeña pérdida de información la cual es responsable de los pequeños píxeles de diferencia que pueden observarse en los patrones convergidos.  