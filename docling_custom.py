from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    PdfPipelineOptions,
    TesseractCliOcrOptions,
    TesseractOcrOptions,
)
from docling.document_converter import DocumentConverter, PdfFormatOption
import sys


# Function to process a document
def process_document(file_path):
    # Set lang=["auto"] with a tesseract OCR engine: TesseractOcrOptions, TesseractCliOcrOptions
    # ocr_options = TesseractOcrOptions(lang=["auto"])
    ocr_options = TesseractCliOcrOptions(lang=["auto"])

    pipeline_options = PdfPipelineOptions(
        do_ocr=True, ocr_options=ocr_options
    )

    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(
                pipeline_options=pipeline_options,
            )
        }
    )

    doc = converter.convert(file_path).document
    md = doc.export_to_markdown()
    print(md)


# Main  function
if __name__ == "__main__":
    # Retrieve document name from command line arguments
    if len(sys.argv) != 2:
        print("Usage: python docling_simple.py <document>")
        sys.exit(1)
    # Call the function to process the document
    process_document(sys.argv[1])