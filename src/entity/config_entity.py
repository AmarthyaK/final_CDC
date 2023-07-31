from dataclasses import dataclass
from pathlib import Path

#we created this class to store the paths of the data, this will be used later on to create directories
#So here, DataIngestionConfig is an entity!
@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class BaseModelConfig:
    root_dir: str
    base_model_path: Path
    updated_base_model_path: Path
    params_img_size: list #as per VGG16 model, it s required to have the image size as 224,224,3
    params_batch_size: int
    params_include_top: bool
    params_epochs: int
    params_classes: int
    params_weights: str
    params_learning_rate: float

@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_file_path: Path

@dataclass(frozen=True)
class ModelTrainConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_image_size: int
    params_is_augmentation: bool

#evaluation

@dataclass(frozen = True)
class EvaluationConfig:
    path_of_model: Path
    path_of_data: Path
    all_params: dict
    params_img_size: list
    params_batch_size: int

