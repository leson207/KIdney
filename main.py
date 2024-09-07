from Kidney import logger
from Kidney.pipeline.stage_1 import DataIngestionTrainingPipeline
from Kidney.pipeline.stage_2_prepare_base_model import PrepareBaseModelTrainingPipeline
from Kidney.pipeline.stage_3_model_training import ModeltrainingPipeline
from Kidney.pipeline.stage_4_evaluation import EvaluationPipeline

# STAGE_NAME = 'Data Ingestion Stage'


# if __name__=='__main__':
#     try:
#         logger.info(f'>>>>> Stage {STAGE_NAME} started <<<<<')
#         obj = DataIngestionTrainingPipeline()
#         obj.main()
#         logger.info(f'>>>>> Stage {STAGE_NAME} completed <<<<<<')
#     except Exception as e:
#         logger.exception(e)
#         raise e

# STAGE_NAME='PREPARE BASE MODEL'

# if __name__=='__main__':
#     try:
#         logger.info(f'***********')
#         logger.info(f'>>>>>>. Stage {STAGE_NAME} started <<<<<<')
#         obj = PrepareBaseModelTrainingPipeline()
#         obj.main()
#         logger.info(f'>>>>>> Stage {STAGE_NAME} completed <<<<<<')
#     except Exception as e:
#         logger.exception(e)
#         raise e


# AUTOTUNE/ PREFETCH
# parallel training
# dagshub URI
# call back
# custome model

# STAGE_NAME = 'MODEL TRAINING'

# if __name__=='__main__':
#     try:
#         logger.info(f'***************')
#         logger.info(f'>>>>>>>> Stage {STAGE_NAME} started <<<<<')
#         obj = ModeltrainingPipeline()
#         obj.main()
#         logger.info(f'>>>>>>> Stage {STAGE_NAME} completed <<<<')
#     except Exception as e:
#         logger.exception(e)
#         raise e

STAGE_NAME = 'MODEL EVALUATION'

if __name__ == '__main__':
    try:
        logger.info(f'****************')
        logger.info(f'>>>>>>>> stage {STAGE_NAME} started <<<<<<')
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f'>>>>>>> stage {STAGE_NAME} completed <<<<')
    except Exception as e:
        logger.exception(e)
        raise e