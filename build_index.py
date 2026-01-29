from kb import DOCUMENTS
from rag import ingest

if __name__ == "__main__":
    text = " ".join(DOCUMENTS)
    ingest(text)
