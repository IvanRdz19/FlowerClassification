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

Como se nos enseñó en la materia, para poder entrenar una red neuronal convolutiva de manera éxitosa se debe de tener una cantidad de datos casi igual para cada clase, pero después de realizar la limpieza las clases quedaron con los siguientes porcentajes:

| Clase       | Imágenes | Porcentaje (%) |
|-------------|----------|----------------|
| Daisy       | 494      | 19.52%         |
| Dandelion   | 640      | 25.28%         |
| Rose        | 414      | 16.36%         |
| Sunflower   | 481      | 19.01%         |
| Tulip       | 502      | 19.83%         |
| **Total**   | **2531** | **100%**       |

## 🚧 Avances

- [ ] Limpieza y organización del dataset
- [ ] Escalamiento de datos
- [ ] Construcción del modelo CNN
- [ ] Entrenamiento y validación
- [ ] Evaluación de resultados

## 🧠 Librerías utilizadas

```python
import matplotlib.pyplot as plt
import numpy as np
import os
import tensorflow as tf
