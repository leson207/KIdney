from Kidney import logger
from Kidney.config.configuration import ConfigurationManager
from Kidney.components.model_training import Training


STAGE_NAME = 'TRAINING STAGE'

class ModeltrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

if __name__=='__main__':
    try:
        logger.info(f'***************')
        logger.info(f'>>>>>>>> Stage {STAGE_NAME} started <<<<<')
        obj = ModeltrainingPipeline()
        obj.main()
        logger.info(f'>>>>>>> Stage {STAGE_NAME} completed <<<<')
    except Exception as e:
        logger.exception(e)
        raise e