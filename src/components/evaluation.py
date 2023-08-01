from urllib.parse import urlparse
from src.utils.common import save_json

from src.logger import logging

from src.entity.config_entity import EvaluationConfig

import tensorflow as tf
from pathlib import Path

import os


class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    
    def _valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.30
        )
        logging.info(f"dataflow_kwargs")
        dataflow_kwargs = dict(
            target_size=self.config.params_img_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )
        logging.info(f"valid_datagenerator_kwargs")
        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )
        logging.info(f"self_valid_datagenerator")
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.path_of_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

    
    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    

    def evaluation_method(self):

        model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        logging.info(f"performing evaluation")
        self.score = model.evaluate(self.valid_generator)
        logging.info(f"Scores: {self.score}")

    
    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        logging.info(f"Scores: {scores}")
        logging.info(f"the path of scores json is: {self.config.path_scores_json}")
        save_json(path=Path(self.config.path_scores_json), data=scores)