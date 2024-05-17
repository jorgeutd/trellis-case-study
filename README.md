# Trellis Law Document Classification

This repository contains the code and resources for the Trellis Law Document Classification project, which aims to develop a document classification model for a dataset of text files (.txt) labeled under 11 categories: Technology, Sport, Space, Politics, Medical, Historical, Graphics, Food, Entertainment, Business, and Other. The goal is to classify these documents accurately and expose the functionality through an API.

## Repository Structure

The repository is structured as follows:

```
trellis-case-study/
├── api/
│ ├── app/
│ │ ├── init.py
│ │ ├── config.py
│ │ ├── main.py
│ │ ├── models.py
│ │ └── utils.py
│ ├── tests/
│ │ └── test_api.py
│ ├── Dockerfile
│ ├── README.md
│ └── requirements.txt
│
├── notebooks/
│ ├── 00_data_preprocessing_trellis.ipynb
│ ├── 01_training_model_v1_trellis.ipynb
│ └── 02_model_deployment_sagemaker_endpoint_Trellis_Doc.ipynb
│
├── data/
│ └── training_data.csv_2024-05-17.csv

```

## Dataset

The dataset used for training the document classification model consists of a collection of text files (.txt) labeled under 11 categories: Technology, Sport, Space, Politics, Medical, Historical, Graphics, Food, Entertainment, Business, and Other. The dataset can be accessed via the following link:
[Download Dataset](https://www.dropbox.com/scl/fo/bsx6t0y86eicr15xm2haa/AJvvER3VtuXJ090Bcvnh1mI?rlkey=mf7s184ymqlw7pdz64n1eymc0&e=1&st=6hm47f99&dl=0)

## Model Development

The document classification model was developed by fine-tuning the DistilBERT base model on the labeled dataset provided. The fine-tuning process involved data preprocessing, model training using the Hugging Face Transformers library and its Trainer class, and evaluation using appropriate metrics. The fine-tuned model achieves high accuracy in classifying the documents' content into the predefined categories.

The model development process is documented in the following Jupyter notebooks:
- `notebooks/00_data_preprocessing_trellis.ipynb`: Data preprocessing tasks.
- `notebooks/01_training_model_v1_trellis.ipynb`: Model training.
- `notebooks/02_model_deployment_sagemaker_endpoint_Trellis_Doc.ipynb`: Deploying the model to a SageMaker endpoint.

## API

The Trellis Law Document Classification API is built using the FastAPI framework in Python. It exposes a RESTful interface to allow users to submit the content of documents and receive the predicted category as a response.

For detailed information about the API, including endpoints, request/response formats, deployment, error handling, authentication, and testing, please refer to the [API README](api/README.md).

## Getting Started

To get started with the Trellis Law Document Classification project, follow these steps:

1. Clone the repository:
```
git clone https://github.com/jorgeutd/trellis-case-study.git

```

2. Set up the required dependencies and environment for the API. Refer to the [API README](api/README.md) for detailed instructions.

3. Explore the Jupyter notebooks in the `notebooks/` directory to understand the model development process.

4. Use the provided dataset or add your own dataset files to the `data/` directory.

5. Train the model using the notebooks and save the trained model files to the `models/` directory.

6. Deploy the API using the instructions provided in the [API README](api/README.md).

7. Test the API endpoints and integrate the document classification functionality into your application.


## Contributing

Contributions to the Trellis Law Document Classification project are welcome only for current of the Trellis team! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

