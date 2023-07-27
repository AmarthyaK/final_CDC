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
class ParamsConfig:
    IMAGE_SIZE: list #as per VGG16 model, it s required to have the image size as 224,224,3
    BATCH_SIZE: int
    INCLUDE_TOP: bool
    EPOCHS: int
    CLASSES: int
    WEIGHTS: str
    LEARNING_RATE: float

