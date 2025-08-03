import os
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

def get_chunks() -> list[str]:
    file_path = "data.md"
    markdown_text = ""

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            markdown_text = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        exit(1)

    CHUNK_SIZE = 250
    CHUNK_OVERLAP = 50

    print(f"Splitting text into chunks of size {CHUNK_SIZE} with overlap of {CHUNK_OVERLAP}...")

    md_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.MARKDOWN,
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    print("\n--- Splitting text using split_text() (return list of strings) ---\n")
    text_chunks = md_splitter.split_text(markdown_text)
    return text_chunks

if __name__ == '__main__':
    chunks = get_chunks()
    for c in chunks:
        print(c)
        print("--------------")
