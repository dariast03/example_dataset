
import example_dataset_dataset_builder
import os
import tensorflow_datasets as tfds
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Cargar el dataset
dataset, info = tfds.load(
    'example_dataset', with_info=True, as_supervised=True)

data_train = dataset['train']

print(data_train)

