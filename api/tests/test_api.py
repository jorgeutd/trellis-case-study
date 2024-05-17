from fastapi.testclient import TestClient
from app.main import app
from app.utils import clean_text_content_trellis

client = TestClient(app)

doc_test_trellis = """Van Nistelrooy set to return Manchester United striker Ruud van Nistelrooy may make his comeback after an Achilles tendon injury in the FA Cup fifth round tie at Everton on Saturday.

He has been out of action for nearly three months and had targeted a return in the Champions League tie with AC Milan on 23 February. But Manchester United manager Sir Alex Ferguson hinted he may be back early. He said: "There is a chance he could be involved at Everton but we'll just have to see how he comes through training." The 28-year-old has been training in Holland and Ferguson said: "Ruud comes back on Tuesday and we need to assess how far on he is. "The training he has been doing in Holland has been perfect and I am very satisfied with it.""".strip()

def test_clean_text_content_trellis():
    """
    Test the clean_text_content_trellis function.

    Asserts:
        - The cleaned text content matches the expected output.
    """
    cleaned_text = clean_text_content_trellis(doc_test_trellis)
    expected_output = "Van Nistelrooy set to return Manchester United striker Ruud van Nistelrooy may make his comeback after an Achilles tendon injury in the FA Cup fifth round tie at Everton on Saturday. He has been out of action for nearly three months and had targeted a return in the Champions League tie with AC Milan on 23 February. But Manchester United manager Sir Alex Ferguson hinted he may be back early. He said: "There is a chance he could be involved at Everton but we'll just have to see how he comes through training." The 28-year-old has been training in Holland and Ferguson said: "Ruud comes back on Tuesday and we need to assess how far on he is. "The training he has been doing in Holland has been perfect and I am very satisfied with it.""
    assert cleaned_text == expected_output


def test_classify_document():
    """
    Test the /classify_document endpoint.

    Asserts:
        - The response status code is 200.
        - The response JSON contains the "message" and "label" fields.
    """
    cleaned_text = clean_text_content_trellis(doc_test_trellis)
    response = client.post(
        "/classify_document",
        json={"document_text": cleaned_text},
        auth=("trellisadmin", "trellispassword123")
    )
    assert response.status_code == 200
    assert "message" in response.json()
    assert "label" in response.json()
