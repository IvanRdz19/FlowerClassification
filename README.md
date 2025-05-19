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

## 🚧 Avances

- [ ] Limpieza y organización del dataset
- [ ] Exploración de datos
- [ ] Construcción del modelo CNN
- [ ] Entrenamiento y validación
- [ ] Evaluación de resultados
- [ ] Exportación del modelo

## 🧠 Librerías utilizadas

(Agrega esta sección más adelante cuando empieces a codificar, por ejemplo:)

```python
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
