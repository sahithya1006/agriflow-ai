from pathlib import Path

import pytesseract
from PIL import Image

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def extract_text(image_path):
    """Extract text from an image using Tesseract OCR."""

    path = Path(image_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {image_path}")

    # Check if Tesseract exists
    if not Path(pytesseract.pytesseract.tesseract_cmd).exists():
        raise FileNotFoundError(
            "Tesseract executable not found.\n"
            f"Expected at: {pytesseract.pytesseract.tesseract_cmd}"
        )

    image = Image.open(path)

    text = pytesseract.image_to_string(image, lang="eng")

    return text.strip()


if __name__ == "__main__":
    print("=" * 50)
    print("AgriFlow-AI OCR Module")
    print("=" * 50)

    sample_path = input("Enter image path: ").strip()

    try:
        extracted_text = extract_text(sample_path)

        print("\nExtracted Text\n")
        print("-" * 50)
        print(extracted_text)
        print("-" * 50)

    except Exception as e:
        print("\nError:")
        print(e)