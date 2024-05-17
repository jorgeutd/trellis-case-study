import logging
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.models import DocumentInput, ClassificationResponse
from app.utils import invoke_sagemaker_endpoint
from app.config import settings
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Trellis Law Document Classification API",
    description="API for classifying documents using a sagemaker endpoint with a fine tune distilbert model.",
    version="1.0.0"
)

security = HTTPBasic()

VALID_CREDENTIALS = {
    "username": "trellisadmin",
    "password": "trellispassword123"
}

async def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    """
    Authenticate the user credentials.

    Args:
        credentials (HTTPBasicCredentials): The provided user credentials.

    Returns:
        str: The authenticated username.

    Raises:
        HTTPException: If the provided credentials are invalid.
    """
    if credentials.username != VALID_CREDENTIALS["username"] or \
            credentials.password != VALID_CREDENTIALS["password"]:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return credentials.username

@app.get("/")
async def root():
    return {"message": "Welcome to the Trellis Law Document Classification API"}

@app.post("/classify_document", response_model=ClassificationResponse)
async def classify_document(document: DocumentInput, username: str = Depends(authenticate)):
    """
    Classify a document using the trained model.

    Args:
        document (DocumentInput): The input document to classify.
        username (str): The authenticated username.

    Returns:
        ClassificationResponse: The classification result.

    Raises:
        HTTPException: If an error occurs during document classification.
    """
    try:
        response = invoke_sagemaker_endpoint(settings.endpoint_name, document.document_text)
        if isinstance(response, list):
            response = json.loads(response[0])
        predicted_class = response.get("predicted_class")
        return ClassificationResponse(message="Classification successful", label=predicted_class)
    except Exception as e:
        logger.error(f"An error occurred during document classification: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")