
# LLM-facebook-opt Repository -ko

This repository contains a large language model (LLM) for text generation. We are utilizing the "facebook/opt-125m" model provided by the Transformers library. Although this model is small and primarily intended for trial purposes, you can choose other models for improved accuracy. We have developed a FastAPI application that accepts Korean language input and generates corresponding Korean text output.

To use this repository, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Change your working directory to the repository folder.
4. Launch the FastAPI app using the command `uvicorn main:app --reload`.
5. Access the local server where the FastAPI app is running.

Model Selection:
You can choose a different Hugging Face model for text generation by modifying the following code snippet:
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("facebook/opt-125m")
checkpoint = "facebook/opt-125m"
model = AutoModelForCausalLM.from_pretrained(
    checkpoint, device_map='auto', offload_folder="offload", offload_state_dict=True
)
```
Replace "facebook/opt-125m" with the desired Hugging Face model of your choice.

Running with Docker:
To run the application using Docker, build the Docker image with the following command:
```
docker build -t llm .
```
Then, create a Docker container from the image and run it using:
```
docker run -d --name my-app5 -p 8000:8000 llm
```
The text generation model supports the Korean language and can be utilized accordingly.

Thank you for visiting my Git repository's README. If you have any further questions or need assistance, feel free to reach out.
