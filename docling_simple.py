from docling.document_converter import DocumentConverter
import sys


# Function to process a document
def process_document(file_path):
    converter = DocumentConverter()
    result = converter.convert(file_path)
    print(result.document.export_to_markdown())


# Main  function
if __name__ == "__main__":
    # Retrieve document name from command line arguments
    if len(sys.argv) != 2:
        print("Usage: python docling_simple.py <document>")
        sys.exit(1)
    # Call the function to process the document
    process_document(sys.argv[1])
