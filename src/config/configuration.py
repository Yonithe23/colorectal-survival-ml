from src.entity.config_entity import DataValidation, DataTransformation, ModelTraining
from src.constants.path import PARAMS_FILE_PATH, CONFIG_FILE_PATH, SCHEMA_FILE_PATH
from src.utils.common import read_yaml, create_directories


class Configrationmanger:
    def __init__(
        self,
        config_file=CONFIG_FILE_PATH,
        params_file=PARAMS_FILE_PATH,
        schema_file=SCHEMA_FILE_PATH,
    ):
        self.config = read_yaml(config_file)
        self.params = read_yaml(params_file)
        self.schema = read_yaml(schema_file)

        create_directories([self.config.artifacts_root])

        def get_data_validation(self) -> DataValidation:
            config = self.config.DataValidation
            create_directories([config.root_dir])
            data_validation = DataValidation(
                root_dir=config.root_dir,
                status_file=config.status_file,
                schema=self.schema,
            )

            return data_validation

        def get_data_transformation(self) -> DataTransformation:
            config = self.config.DataTransformation
            create_directories([config.root_dir])
            data_transformation = DataTransformation(
                root_dir=config.root_dir, data_path=config.data_path
            )
            return data_transformation

        def get_model_training(self) -> ModelTraining:
            config = self.config.ModelTraining
            model_training = ModelTraining(root_dir=config.root_dir)
            return model_training
