from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Application settings.

    Attributes:
        debug (bool): Whether to run the application in debug mode.
        endpoint_name (str): The name of the SageMaker endpoint.
        aws_profile_name (str): The AWS profile name to use.
        aws_region_name (str): The AWS region name to use.
    """
    debug: bool = True
    endpoint_name: str = 'distilbert-hf-emails-trellis-document-class'
    aws_profile_name: str = 'main'
    aws_region_name: str = 'us-east-1'

    class Config:
        env_file = '.env'

settings = Settings()