from pydantic import BaseModel, Field

class DocumentInput(BaseModel):
    """
    Input model for document classification.

    Attributes:
        document_text (str): The text content of the document.
    """
    document_text: str = Field(..., description="The text content of the document")

class ClassificationResponse(BaseModel):
    """
    Response model for document classification.

    Attributes:
        message (str): The classification result message.
        label (str): The predicted class label.
    """
    message: str = Field(..., description="The classification result message")
    label: str = Field(..., description="The predicted class label")