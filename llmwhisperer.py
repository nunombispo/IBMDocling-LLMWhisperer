from unstract.llmwhisperer import LLMWhispererClientV2
from unstract.llmwhisperer.client_v2 import LLMWhispererClientException
import sys


# Function to process a document
def process_document(file_path):
    # Initialize the client with your API key
    client = LLMWhispererClientV2(base_url="https://llmwhisperer-api.us-central.unstract.com/api/v2",
                                  api_key='<your-api-key>')
    # Call the sync method with the file path
    try:
        result = client.whisper(
            file_path=file_path,
            wait_for_completion=True,
            wait_timeout=200,
        )
        print(result['extraction']['result_text'])
    except LLMWhispererClientException as e:
        print(e)


# Main  function
if __name__ == "__main__":
    # Retrieve document name from command line arguments
    if len(sys.argv) != 2:
        print("Usage: python docling_simple.py <document>")
        sys.exit(1)
    # Call the function to process the document
    process_document(sys.argv[1])