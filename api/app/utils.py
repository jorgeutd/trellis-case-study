import re
from html import unescape
import json
from typing import Dict
import boto3
from app.config import settings
import logging

logger = logging.getLogger(__name__)

_DEBUG = True

def get_boto_session() -> boto3.Session:
    """
    Initializes and returns a boto3 session.

    Returns:
        boto3.Session: A boto3 session object configured for the specified profile and region.

    Note:
        The _DEBUG global variable controls whether to use a specific AWS profile or the default configuration.
    """
    try:
        if _DEBUG:
            session = boto3.Session(profile_name=settings.aws_profile_name, region_name=settings.aws_region_name)
        else:
            session = boto3.Session(region_name=settings.aws_region_name)
        logger.info("Boto3 session initialized successfully.")
        return session
    except Exception as e:
        logger.error(f"Error initializing boto3 session: {e}", exc_info=True)
        raise

def clean_text_content_trellis(text_content: str) -> str:
    """
    Clean the text content of a document by performing several operations.

    Args:
        text_content (str): The raw text content of the document.

    Returns:
        str: The cleaned text content.
    """
    try:
        # Normalize line breaks to Unix-style
        text_content = re.sub(r'\r\n|\r', '\n', text_content)
        
        # Remove excessive whitespace within lines
        text_content = re.sub(r'\s+', ' ', text_content).strip()
        
        # Strip HTML tags and decode HTML entities
        text_content = re.sub(r'<[^>]+>', '', text_content, flags=re.DOTALL)
        text_content = unescape(text_content)
        
        # Normalize paragraph breaks to ensure readability
        text_content = re.sub(r'\n{3,}', '\n\n', text_content)
        
        return text_content
    except Exception as e:
        logger.error(f"An error occurred while cleaning the text content: {e}")
        return ""
    

def invoke_sagemaker_endpoint(endpoint_name: str, text: str) -> Dict:
    """
    Preprocess the input text and invoke the SageMaker endpoint.

    Args:
        endpoint_name (str): The name of the SageMaker endpoint.
        text (str): The input text to process and send to the model.

    Returns:
        Dict: The response from the SageMaker endpoint.
    """
    try:
        # Preprocess the text using clean_text_content_trellis
        logger.info("Preprocessing the input text.")
        processed_text = clean_text_content_trellis(text)
        
        # Prepare the payload for SageMaker endpoint
        payload = json.dumps({"text": processed_text})
        logger.info(f"Payload prepared: {payload}")
        
        # Create a runtime client using the boto3 session
        session = get_boto_session()
        runtime = session.client('runtime.sagemaker')
        
        # Invoke the endpoint
        logger.info(f"Invoking the SageMaker endpoint: {endpoint_name}")
        response = runtime.invoke_endpoint(
            EndpointName=endpoint_name,
            ContentType='application/json',
            Body=payload
        )
        
        # Parse and return the response
        response_body = response['Body'].read().decode('utf-8')
        logger.info(f"Raw response from SageMaker endpoint: {response_body}")
        
        # Handle the case where the response is a list
        if isinstance(response_body, str):
            response_body = json.loads(response_body)
        elif isinstance(response_body, list):
            response_body = json.loads(response_body[0])
        
        logger.info(f"Parsed response from SageMaker endpoint: {response_body}")
        return response_body
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise