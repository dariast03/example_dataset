"""my_dataset dataset."""
import os

import tensorflow_datasets as tfds


class Builder(tfds.core.GeneratorBasedBuilder):
    """DatasetBuilder for my_dataset dataset."""

    VERSION = tfds.core.Version('1.0.1')
    RELEASE_NOTES = {
        '1.0.1': 'Initial release.',
    }

    #lista de clases o tipos de imagenes
    classnames = ['El Chuntunqui', 'El Ch’uta Chuquisaqueño', 'El Huayño Chuquisaqueño', 'El Jula Jula', 'El Potolo', 'El Pujllay', 'El Sicuri', 'El Waca Waca', 'La Cueca Chuquisaqueña', 'La Moseñada']

    shape_image = (None, None, 3)

    def _info(self) -> tfds.core.DatasetInfo:
        """Returns the dataset metadata."""
        return self.dataset_info_from_configs(
            features=tfds.features.FeaturesDict({
                # These are the features of your dataset like images, labels ...
                'image': tfds.features.Image(shape=self.shape_image),
                'label': tfds.features.ClassLabel(names=self.classnames),
            }),

            # If there's a common (input, target) tuple from the
            # features, specify them here. They'll be used if
            # as_supervised=True in builder.as_dataset.
            supervised_keys=('image', 'label'),  # Set to None to disable
            homepage='https://mi-dataset/',
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        """Returns SplitGenerators."""
        # Download the data as specified in `_data_url` and write it to `downloaded_path`.
        #!path = dl_manager.download_and_extract('https://todo-data-url')

        #ruta de los datos
        train_path = 'data'

        return {
            #!'train': self._generate_examples(path / 'train_imgs'),

            #generar ejemplos tipos de datos (train, test, val)
            'train': self._generate_examples(train_path),
        }

    def _generate_examples(self, path):
        for class_name in os.listdir(path):
            class_path = os.path.join(path, class_name)

            if os.path.isdir(class_path):
                for image_name in os.listdir(class_path):
                    print(image_name)
                    image_path = os.path.join(class_path, image_name)
                    yield class_name + '_' + image_name, {
                        'image': image_path,
                        'label': class_name,
                    }
