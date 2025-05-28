# 🌸 CNN Flower Classification

**Autor:** Iván Rodríguez Cuevas - A01781284  
**Curso:** TC3002B - Módulo 2

---

Este repositorio contiene el desarrollo de un proyecto de red neuronal convolutiva (CNN) enfocado en la clasificación de imágenes de flores.

## 📌 Descripción del Proyecto

El objetivo es crear y entrenar una CNN capaz de clasificar imágenes de cinco categorías distintas de flores.

## 🌼 Clases del Dataset

Se eligió un dataset de Kaggle que contiene imágenes de las siguientes clases:

- 🌼 **Daisy** (Margarita)  
- 🌻 **Dandelion** (Diente de león)  
- 🌹 **Rose** (Rosa)  
- 🌷 **Tulip** (Tulipán)  
- 🌞 **Sunflower** (Girasol)

📁 Dataset original disponible en:  
[🔗 Flowers Dataset en Kaggle](https://www.kaggle.com/datasets/imsparsh/flowers-dataset)

## 🗂️ Estructura del Dataset

Afortunadamente el dataset ya viene dividido en dos carpetas:

- `train/` – contiene **2746 imágenes**
- `test/` – contiene **924 imágenes**

Esto me ayudó, dado que me ahorró el tiempo de hacer la separación de los datos manualmente para entrenamiento y pruebas.

## 🧹 Limpieza del Dataset (train)

La carpeta de `train/` contiene 5 carpetas, las cuales contienen imagenes de los 5 tipos de flores que clasificaremos.

Al explorar las carpetas pude observar que a pesar de que los datos ya vienen separados, no vienen del todo correctos. En varias carpetas encontré imagenes mal clasificadas o simplemente que no tenían nada que ver con flores. Por esto mismo tuve que hacer una revisión manual de todas mis imagenes para eliminar las imagenes erroneas y validar que tuviera las correctas.

Después de limpiar los datos, la carpeta de `train/`  quedó de la siguiente manera:

| Clase       | Antes | Después |
|-------------|--------|---------|
| Daisy       | 501    | 494     |
| Dandelion   | 646    | 640     |
| Rose        | 497    | 414     |
| Sunflower   | 495    | 481     |
| Tulip       | 607    | 502     |
| **Total**   | **2746** | **2531** |

## 📊 Distribución del Dataset (después de la limpieza)

Como se nos enseñó en la materia, para poder entrenar una red neuronal convolutiva de manera éxitosa se debe de tener una cantidad de datos casi igual para cada clase, después de realizar la limpieza las clases quedaron con los siguientes porcentajes:

| Clase       | Imágenes | Porcentaje (%) |
|-------------|----------|----------------|
| Daisy       | 494      | 19.52%         |
| Dandelion   | 640      | 25.28%         |
| Rose        | 414      | 16.36%         |
| Sunflower   | 481      | 19.01%         |
| Tulip       | 502      | 19.83%         |
| **Total**   | **2531** | **100%**       |

## 📚 Separación train y validation

Posterior a la limpieza del dataset se hizo la separación de datos entre los datos de entrenamiento (train) y los datos con los que se validará el modelo (validation). Separamos el 20% de los datos que tenemos en la carpeta de `train/` y los movimos a una carpeta llamada `validation_data/`. El 20% de los datos son 506, para fines practicos se redondeó este número y se seleccionaron 500 imágenes en total para validación (100 imágenes por cada clase de flor).

## 💉 Data Augmentation

Para poder entrenar un modelo de mejor manera se necesitan más datos, para esto realizamos una técnica de data augmentation que se nos enseñó en clase.
Esta técnica consiste en tomar las imagenes y cambiarlas levemente, ya sea rotandolas o invirtiéndolas verticalmente.
Adaptamos el código proporcionado por el profesor a nuestro código y generamos aproximadamente el triple de imágenes.

| Clase       | Imágenes |
|-------------|----------|
| Daisy       | 1576     |
| Dandelion   | 2160     |
| Rose        | 1296     |
| Sunflower   | 1524     |
| Tulip       | 1608     |
| **Total**   | **8164** |

Estas nuevas imagenes las guardé en una carpeta llamada `augmented_train/` y al igual que con la carpeta de `train/`, esta carpeta se seccionó en 5 nuevas carpetas con cada clase de flor que tenemos.

## 🛠️ Construcción de la CNN

Para poder empezar a construir la red neuronal convolutiva primero indagué y busqué artículos (papers) sobre este tema. Después de leer unos cuantos y ver las arquitecturas y resultados que obtenian opté por implementar la arquitectura mencionada en el siguiente paper:

[🔗 An efficient classification of flower images with
convolutional neural networks](https://d1wqtxts1xzle7.cloudfront.net/80918318/3444-libre.pdf?1645009408=&response-content-disposition=inline%3B+filename%3DAn_efficient_classification_of_flower_im.pdf&Expires=1748469315&Signature=bdfRdsCHZU8Rb44msRGHyl043bniMC2ADfZza0q7eBaq8wAubqtcQ5AeGa8Jv~~-1FXD5RBtYMap4WUzv9WPYhLyU2jTGEm32rTHc1fOdq4rKkRp7L4np004X6PebWLeXgM6ljEmuNvbANFNDqSnLz4Y5bT97QQfO~uGPz2pPo6H551QuQYc9xwMdtYGryFOAEyccIvry1tDvHi9~7dm8gr9om2q1GJZhkmxcESvQRbxjY3PZx23MC9dVbejE35VuOtG2cRZEDrwltmz96RpRX4aT-DFtr4UE0pz1DNbYlVYaBtkeKdJSGMqxOWX9V1SLkDj~ozhdKfJNC3x1DYL9Q__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)

La arquitectura propuesta en el paper consiste en lo siguiente:

| Capa               | Tipo                     |
|--------------------|--------------------------|
| Input              | Input de la imagén       |
| Conv1              | Convolución (16x16)      |
| Conv2              | Convolución (9x9)        |
| StochPool1         | Pooling Estocástico      |
| Dropout1           | Regularización           |
| Conv3              | Convolución (5x5)        |
| Conv4              | Convolución (5x5)        |
| StochPool2         | Pooling Estocástico      |
| Dropout2           | Regularización           |
| Flatten            | Aplanamiento             |
| Dense1             | Capa Dense               |
| Dropout3           | Regularización           |
| Output             | Clasificación            |

Algo importante, es que cabe recalcar que esta arquitectura utiliza activación 'tanh' en lugar de 'Relu'. Esto con el fin de capturar mejores texturas o colores en los petalos de las flores.
En el paper mencionan que utilizando tanh alcanzaron un **97.78%** de accuracy, a diferencia de ReLU con la cuál alcanzaron **94%**.

Debido a que mi GPU no es tan potente y además yo solo clasifico 5 tipos de flores, decidí reducir la red para adaptarla a mi caso. Mi arquitectura quedó de la siguiente manera:

| Capa               | Tipo                     |
|--------------------|--------------------------|
| Input              | Input de la imagén       |
| Conv1              | Convolución (16x16)      |
| MaxPool            | Max Pooling              |
| Dropout1           | Regularización (0.25)    |
| Conv2              | Convolución (9x9)        |
| MaxPool            | Max Pooling              |
| Dropout2           | Regularización (0.25)    |
| Conv3              | Convolución (5x5)        |
| Conv4              | Convolución (5x5)        |
| MaxPool            | Max Pooling              |
| Dropout            | Dropout (0.25)           |
| Flatten            | Aplanado                 |
| Dense              | Densa (64)               |
| Dropout            | Dropout (0.5)            |
| Dense              | Densa (5)                |
| Output             | Clasificación            |


## 🗃️ Google Drive

El link a la carpeta de Drive donde se puede encontrar todo lo relacionado al proyecto, incluyendo el modelo, es el siguiente:

[🔗 Modulo2-CNN](https://drive.google.com/drive/folders/1nuC3y95_OiF5_yCtBkUkDkcrK6HXi0-I?usp=drive_link)

## 🚧 Avances

- [X] Limpieza y organización del dataset
- [X] Escalamiento de datos
- [X] Construcción del modelo CNN
- [ ] Entrenamiento y validación
- [ ] Evaluación de resultados

## 🧠 Librerías utilizadas

```python
import matplotlib.pyplot as plt
import numpy as np
import os
import tensorflow as tf
