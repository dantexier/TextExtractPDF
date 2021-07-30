#**************************************************
# Autor: John Atkinson. Fecha: 20/05/21
# Descripción:
#       - Clasificación de sentimientos (Inglés) basados en modelos BERT
#       - Se utiliza una versión más "liviana" llamada Roberta:
#        https://huggingface.co/transformers/model_doc/roberta.html
#  INSTALAR:
#      conda install pytorch torchvision torchaudio cpuonly -c pytorch   
#      pip install transformers
#************************************************************************
import numpy
import torch
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from transformers import RobertaTokenizer, RobertaModel
import warnings
warnings.filterwarnings('ignore')


# Dado un texto u oración, lo tokenizamos según formato BERT y retornamos
# el embedding de la oración (vector de largo 768)
def ObtenerEmbeddingOracion(texto):
   # Codificar entrada y tokenizar
   encoded_input = tokenizer(texto, return_tensors='pt')
   # aplicar el modelo a la entrada codificada
   output = model(**encoded_input)
   # generar el embeddings como un promedio de los embeddings de 
   # las palabras de la oración
   embedding = torch.mean(output[0], dim=1).detach().numpy()
   return(embedding[0]) 

# Importar un archivo CSV que contiene dos columnas: opinion y sentimiento (0 o 1)

df = pd.read_csv('https://github.com/clairett/pytorch-sentiment-classification/raw/master/data/SST2/train.tsv', delimiter='\t', header=None)

# Por temas de velocidad sólo usaos las 800 primeras oraciones:
oraciones = df[:800]

# Inicializamos BERT (Roberta) con  un modelo pre-entrenado
tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
model = RobertaModel.from_pretrained('roberta-base')

# Preparamos el dataset para la clasificación
# Generar el embedding para cada una de las oraciones del dataset
features = [ObtenerEmbeddingOracion(opinion) for opinion in oraciones[0]]
features = numpy.array(features)
labels = numpy.array(oraciones[1])

# A partir de ls features y labels, hacemos un split para generar los sets 
# de entrenamiento y de prueba
train_features, test_features, train_labels, test_labels = train_test_split(features, labels)

# Ahora entrenamos un modelo de clasificación.
# En este caso, usamos un modelo de regresión logística (podría ser cualquier otro).

lr_clf = LogisticRegression()
# Ajustamos el modelo con la proporción de datos de entrenamiento y sus labels
lr_clf.fit(train_features, train_labels)

# Evaluamos el modelo con los datos de prueba para clasificar oraciones nuevas
# Utilizamos la medida ACCURACY 
accuracy = lr_clf.score(test_features, test_labels)
print(accuracy)
