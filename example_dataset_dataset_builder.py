"""my_dataset dataset."""
import os

import tensorflow_datasets as tfds


class Builder(tfds.core.GeneratorBasedBuilder):
    """DatasetBuilder for my_dataset dataset."""

    VERSION = tfds.core.Version('1.0.0')
    RELEASE_NOTES = {
        '1.0.0': 'Initial release.',
    }

    classnames = ['cueca', 'diablada', 'morenada', 'tinku', 'caporales', 'chacarera', 'chamame', 'cuarteto', 'cumbia',
                  'malambo', 'saya', 'tango', 'zamba', 'zamba_cueca', 'bachata', 'bolero', 'merengue', 'salsa', 'samba',  'vallenato']

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
            description="""
            Este dataset contiene imágenes de ropa típica de diversas danzas de Bolivia, ideal para entrenar modelos de clasificación de imágenes.
            La versión 1.0.0 incluye imágenes clasificadas en las siguientes 26 categorías:
            - cueca
            - diablada
            - morenada
            - tinku
            - caporales
            - chacarera
            - chamame
            - cuarteto
            - cumbia
            - folklore
            - malambo
            - saya
            - tango
            - zamba
            - zamba_cueca
            - bachata
            - bolero
            - merengue
            - salsa
            - samba
            - vallenato
            - bambuco
            - joropo
            - pasillo
            - porro
            - tropical
            - villancico

            Cada clase contiene múltiples imágenes que muestran trajes tradicionales usados en las danzas correspondientes.
            Las imágenes son de diversos tamaños pero tienen 3 canales de color (RGB).
            """
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        """Returns SplitGenerators."""
        # Download the data as specified in `_data_url` and write it to `downloaded_path`.
        #!path = dl_manager.download_and_extract('https://todo-data-url')
        train_path = 'data'

        return {
            #!'train': self._generate_examples(path / 'train_imgs'),
            'train': self._generate_examples(train_path),
        }

    def _generate_examples(self, path):
        """Yields examples."""

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
