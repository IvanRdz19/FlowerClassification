# 🌸 CNN Flower Classification

**Autor:** Iván Rodríguez Cuevas - A01781284  
**Curso:** TC3002B - Módulo 2

---

Este repositorio contiene el desarrollo de un proyecto de red neuronal convolutiva (CNN) enfocado en la clasificación de imágenes de flores, realizado como parte del curso de aprendizaje profundo.

## 📄 Paper del Proyecto

Toda la información detallada sobre la metodología, limpieza del dataset, arquitecturas utilizadas, procesos de aumentación de datos, entrenamiento y comparación de resultados se encuentra documentada en el siguiente artículo:

📘 **Consulta el paper completo aquí**:  
[🔗 Descargar paper (PDF)](./flower_classification_paper.pdf)

### 🔬 Resumen (Abstract)

> Este artículo científico presenta la comparación de dos modelos de redes neuronales convolucionales (CNN) para la clasificación de cinco especies de flores: margarita, diente de león, rosa, girasol y tulipán. El primer modelo replica una arquitectura compleja propuesta por Prasad et al., mientras que el segundo es una versión optimizada y más ligera. Utilizando un conjunto de datos de aproximadamente 3,200 imágenes y técnicas de aumentación, se expandió el dataset a más de 9,500 imágenes. Tras el entrenamiento, el modelo simplificado alcanzó una precisión de validación del 79.25%, superando al modelo complejo en 9% y con 87% menos parámetros. Los resultados demuestran que, para tareas de clasificación con pocas clases, las arquitecturas livianas pueden ofrecer un mejor equilibrio entre rendimiento y eficiencia computacional.

---

## 📁 Dataset

Se utilizó un conjunto de datos de Kaggle con cinco categorías de flores:

- 🌼 **Daisy**  
- 🌻 **Dandelion**  
- 🌹 **Rose**  
- 🌷 **Tulip**  
- 🌞 **Sunflower**

🔗 [Flowers Dataset en Kaggle](https://www.kaggle.com/datasets/imsparsh/flowers-dataset)

## 🧠 Modelos y Arquitecturas

Se compararon dos modelos CNN:

- 📘 **Modelo 1:** Basado en la arquitectura propuesta por Prasad et al. (alta complejidad, tanh, pooling estocástico).  
- 🧩 **Modelo 2:** Arquitectura optimizada (menos parámetros, ReLU, max pooling, regularización).

> Para ver el diseño completo de ambas arquitecturas y su rendimiento, consulta el [paper](./flower_classification_paper.pdf).

## 🚀 Resultados Generales

- 🧪 **Modelo 1**: 70% de accuracy con alto sobreajuste.  
- 🧪 **Modelo 2**: 79.25% de accuracy y mejor generalización con 87% menos parámetros.

---

## 🗃️ Recursos adicionales

📁 Carpeta de Google Drive con modelos, datasets y scripts:  
[🔗 Modulo2-CNN - Google Drive](https://drive.google.com/drive/folders/1nuC3y95_OiF5_yCtBkUkDkcrK6HXi0-I?usp=drive_link)

