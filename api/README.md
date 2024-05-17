# FastAPI API - Trellis Law Document Classification API

This repository contains the code and resources for the Trellis Law Document Classification API service, which provides a RESTful interface to classify documents content into predefined categories using a fine-tuned DistilBERT model deployed on a SageMaker endpoint.

## Introduction
The Trellis Law Document Classification API is designed to accurately classify documents into predefined categories. It utilizes a fine-tuned DistilBERT model, which has been trained on a labeled dataset of what it looks like are news documents, to provide reliable and efficient document classification functionality.

## Dataset
The dataset used for training the document classification model consists of a collection of text files (.txt) labeled under 11 categories: Technology, Sport, Space, Politics, Medical, Historical, Graphics, Food, Entertainment, Business, and Other. The dataset can be accessed via the following link:
[Download Dataset](https://www.dropbox.com/scl/fi/nylcr21k4aw5xqmb72fgu/trellis_document_classification.zip?rlkey=1dhlovdnltg1r7pjdd9wkymo6&st=8570qec3&dl=0)

## Model Development ( Notebook 01_training_model_v1_trellis)
The document classification model was developed by fine-tuning the DistilBERT base model on the labeled dataset provided. The fine-tuning process involved data preprocessing, model training using the Hugging Face Transformers library and its Trainer class, and evaluation using appropriate metrics. The fine-tuned model achieves high accuracy in classifying the documents content into the predefined categories.

The fine-tuned model achieved an accuracy of 0.978 and an F1 score of 0.978 on the test set.

## Model Deployment (Notebook 02_model_deployment)
The fine-tuned DistilBERT model was deployed to a SageMaker endpoint for inference. The deployment process involved the following steps:

Model Serialization: The trained model and tokenizer were saved to a directory (deployment_package_dir) using the save_pretrained method from the Transformers library.

Tarball Creation: The serialized model directory was compressed into a tarball (model.tar.gz) using the create_tarball function. This function takes the source directory (deployment_package_dir) and the output tarball filename (output_tarball) as input and creates the tarball using the tarfile module.

S3 Upload: The created tarball was uploaded to an S3 bucket using the upload_to_s3 function. This function takes the file path (output_tarball), bucket name (bucket_name), and S3 key (s3_key) as input and uses the boto3 library to upload the file to the specified S3 location.

Model Deployment: The uploaded model tarball was deployed to a SageMaker endpoint using the deploy_huggingface_model function. This function takes the S3 URI of the model tarball (s3_model_path), the SageMaker execution role (role), the instance type (instance_type), and the number of instances (instance_count) as input. It creates a HuggingFaceModel object with the specified configurations and deploys the model to the endpoint.

The deployed model endpoint can be accessed using the predictor object returned by the deploy_huggingface_model function.

## Inference Code
The inference code (inference.py) defines the necessary functions for loading the model, processing input data, generating predictions, and formatting the output.

model_fn: Loads the model and tokenizer from the specified directory and moves the model to the appropriate device (GPU if available, otherwise CPU).
input_fn: Processes the input data from the request body. It expects the input data to be in JSON format and returns the parsed data.
predict_fn: Generates predictions from the input data using the loaded model and tokenizer. It tokenizes the input text, passes it through the model, and returns the predicted class label. If the predicted class is not one of the existing classes, it returns "other".
output_fn: Formats the prediction output based on the specified accept type (JSON).

## API Development
The Trellis Law Document Classification API is built using the FastAPI framework in Python. It exposes a RESTful interface to allow users to submit the content of the documents input content and receive the predicted category as a response.

### API Endpoints
The API exposes the following endpoints:
- `GET /`: Serves as a welcome message when accessing the root URL of the API.
- `POST /classify_document`: Accepts a JSON payload containing the document_text field and returns the predicted category as a response. This endpoint requires HTTP Basic Authentication.

### Request Body
The request body for the `/classify_document` endpoint should be in JSON format (as requsted on the PDF document) and include the following field:
```json
{
  "document_text": "string, required"
}
```

Success Response (200 OK):

```json
Copy code
{
  "message": "Classification successful",
  "label": "contract"
}

```

Error Response (401 Unauthorized):

```json
{
  "detail": "Invalid credentials"
}

```

Error Response (500 Internal Server Error):

```json
{
  "detail": "Internal Server Error"
}

```

### Deployment
The Trellis Document Classification API is designed to be deployed using Docker. The provided Dockerfile contains the necessary instructions to build a Docker image of the application.

#### Prerequisites

Python 3.10 or higher
Docker installed on your system

### Installation



### Error Handling and Validation

The API implements appropriate error handling and validation mechanisms. It validates the request payload to ensure the required document_text field is present and handles potential errors that may occur during the classification process. Meaningful error messages are provided to the client for debugging and troubleshooting purposes.

### Authentication

The API uses HTTP Basic Authentication to secure the endpoints. The authenticate function in main.py verifies the provided credentials against the VALID_CREDENTIALS dictionary. Make sure to update the VALID_CREDENTIALS with your desired username and password to test the endpoint.

### Configuration

Update the VALID_CREDENTIALS in main.py with your desired username and password for authentication.
Set the appropriate AWS credentials and region in config.py for accessing the SageMaker endpoint.

### Running the API

1.- Build the Docker image:

docker build -t trellis-law-document-classification-api .

2.- Run the Docker container:

Copy docker run -p 8000:8000 trellis-law-document-classification-api

Access the API at http://localhost:8000 using your preferred API client or tool.

### Testing

The repository includes a tests directory with test cases for the API endpoints and utility functions. To run the tests, execute the following command:

pytest tests/


### UI Swagger test data examples

#1: 
```json
{
  "document_text": "Van Nistelrooy set to return\n\nManchester United striker Ruud van Nistelrooy may make his comeback after an Achilles tendon injury in the FA Cup fifth round tie at Everton on Saturday.\n\nHe has been out of action for nearly three months and had targeted a return in the Champions League tie with AC Milan on 23 February. But Manchester United manager Sir Alex Ferguson hinted he may be back early. He said: \"There is a chance he could be involved at Everton but we'll just have to see how he comes through training.\" The 28-year-old has been training in Holland and Ferguson said: \"Ruud comes back on Tuesday and we need to assess how far on he is. \"The training he has been doing in Holland has been perfect and I am very satisfied with it.\" Even without Van Nistelrooy, United made it 13 wins in 15 league games with a 2-0 derby victory at Manchester City on Sunday. But they will be boosted by the return of the Dutch international, who is the club's top scorer this season with 12 goals. He has not played since aggravating the injury in the 3-0 win against West Brom on 27 November. Ferguson was unhappy with Van Nistelrooy for not revealing he was carrying an injury. United have also been hit by injuries to both Alan Smith and Louis Saha during Van Nistelrooy's absence, meaning Wayne Rooney has sometimes had to play in a lone role up front. The teenager has responded with six goals in nine games, including the first goal against City on Sunday."
}

```
#2: 
```json
{
  "document_text": "Scissor Sisters win top gig award\n\nNew York band Scissor Sisters have won a gig of the year award for their performance at this year's V Festival.\n\nThe award was voted for by listeners of Virgin Radio, which compiled a top 10 mostly dominated by newcomers on the music scene this year. The quirky disco-rock band beat The Red Hot Chili Peppers, who came second for their Hyde Park performance in June. Virgin Radio DJ Pete Mitchell said: \"This year has seen an amazing array of talent come into the mainstream.\" He added: \"The Scissor Sisters are one of the most original, eccentric bands to come through and it's no surprise the British public are lapping up their performances.\" Newcomers Keane came in third place for their August gig at the V Festival, followed by Maroon 5 and Snow Patrol.\n\nMusic veterans The Who and David Bowie both earned places on the list, at number eight and 10 respectively. At number seven was Oxfam's Make Fair Trade gig at London's Hammersmith Apollo in October, which featured performances by REM, Razorlight, and Coldplay's Chris Martin. Glasgow's Franz Ferdinand earned a place at number nine for their home-town performance in April. The annual survey was voted for by nearly 4,000 listeners."
}
```


### Service Structure :

| Folder/File       | Path                     |
|-------------------|--------------------------|
| TRELLIS-SERVICE   |                          |
| ├── app           | /app                     |
| │   ├── __init__.py | /app/__init__.py       |
| │   ├── config.py  | /app/config.py          |
| │   ├── main.py    | /app/main.py            |
| │   ├── models.py  | /app/models.py          |
| │   ├── utils.py   | /app/utils.py           |
| ├── tests         | /tests                   |
| │   ├── test_api.py| /tests/test_api.py      |
| ├── Dockerfile    | /Dockerfile              |
| ├── README.md     | /README.md               |
| ├── requirements.txt | /requirements.txt      |