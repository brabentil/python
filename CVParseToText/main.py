import os
import pdfplumber


def extract_text_and_links_from_pdf(pdf_path):
    """Extracts text and hyperlinks from a PDF file."""
    with pdfplumber.open(pdf_path) as pdf:
        text_parts = []
        links = []

        for page in pdf.pages:
            text = page.extract_text()
            if text:
                text_parts.append(text)

            # Extract hyperlinks (annotations)
            if page.annots:
                for annot in page.annots:
                    if "/URI" in annot:
                        links.append(annot["/URI"])

        full_text = "\n".join(text_parts)
        links_text = "\n".join(links)

    return full_text, links_text


def process_pdfs(pdf_folder, output_folder, max_cvs_per_file=5):
    """Processes PDF CVs and saves extracted text and links in multiple text files."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith(".pdf")]
    chunked_texts = []
    temp_texts = []
    count = 0

    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_folder, pdf_file)
        text, links = extract_text_and_links_from_pdf(pdf_path)

        if text.strip() or links.strip():
            entry = f"CV: {pdf_file}\n{text}\nLinks:\n{links}\n{'-' * 80}\n"
            temp_texts.append(entry)

        if len(temp_texts) >= max_cvs_per_file:
            chunked_texts.append(temp_texts)
            temp_texts = []

    if temp_texts:
        chunked_texts.append(temp_texts)

    for i, chunk in enumerate(chunked_texts):
        output_path = os.path.join(output_folder, f"CV_Text_Part_{i + 1}.txt")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(chunk))
        print(f"Saved {output_path}")


if __name__ == "__main__":
    pdf_folder = ""
    output_folder = ""
    process_pdfs(pdf_folder, output_folder)
