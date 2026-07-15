def parse_file(filepath):
    """
    Read TXT, LOG or PDF file and return its text.
    """

    if filepath.endswith(".txt") or filepath.endswith(".log"):
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()

    elif filepath.endswith(".pdf"):
        import PyPDF2

        text = ""

        with open(filepath, "rb") as f:
            reader = PyPDF2.PdfReader(f)

            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted

        return text

    else:
        return ""