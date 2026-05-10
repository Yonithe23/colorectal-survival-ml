from pathlib import Path
from dataclasses import dataclass


@dataclass
class DataValidation:
    root_dir: Path
    status_file: str
    schema: dict


@dataclass
class DataTransformation:
    root_dir: Path
    data_path: Path


@dataclass
class ModelTraining:
    root_dir: Path
