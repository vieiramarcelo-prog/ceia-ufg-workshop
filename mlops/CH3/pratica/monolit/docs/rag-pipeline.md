# RAG Pipeline

This API implements a Retrieval-Augmented Generation (RAG) pipeline using LangChain. Documents are ingested once on upload and queried on demand. The vector store runs in a dedicated ChromaDB container.

## Supported File Formats

| Extension | Loader | Notes |
|-----------|--------|-------|
| `.pdf` | `PyPDFLoader` | Extracts text from each page |
| `.txt` | `TextLoader` | UTF-8 encoding assumed |

Other file types (e.g. `.docx`, `.xlsx`) are accepted by the upload endpoint and saved to disk, but **not** indexed for RAG.

---

## Ingestion Flow

```
Uploaded file
    │
    ▼
Load document
  ├── .pdf  → PyPDFLoader  (one Document per page)
  └── .txt  → TextLoader   (one Document for the whole file)
    │
    ▼
RecursiveCharacterTextSplitter
  chunk_size   = 1 000 characters
  chunk_overlap = 150 characters
    │
    ▼
OpenAIEmbeddings
  model: text-embedding-ada-002
    │
    ▼
ChromaDB (via HTTP client)
  collection: "documents" (configurable via CHROMA_COLLECTION)
  vs.add_documents(chunks)
```

> Ingestion is protected by an `asyncio.Lock` so concurrent uploads do not produce duplicate writes within the same API process.

---

## Query Flow

```
POST /rag/query { "question": "..." }
    │
    ▼
ChromaDB: collection.count() > 0?  →  No → 404
    │ Yes
    ▼
Retriever: similarity search, k=4
  → returns top-4 most relevant chunks
    │
    ├── Collect source paths for the response
    │
    ▼
LangChain LCEL chain:
  {"context": retriever | format_docs, "question": passthrough}
    │
    ▼
ChatPromptTemplate
  "Answer the question based on the following context:
   {context}

   Question: {question}"
    │
    ▼
ChatOpenAI
  model: gpt-4o-mini (configurable via OPENAI_MODEL)
  temperature: 0
    │
    ▼
StrOutputParser
    │
    ▼
Response { "answer": "...", "sources": [...] }
```

---

## Storage

| Path (container) | Content |
|------------------|---------|
| `/app/uploads/` | Raw uploaded files (backed by `rag_data` volume) |
| `/chroma/chroma/` | ChromaDB collection data (backed by `chromadb_data` volume) |

Both volumes persist across container restarts.

---

## Limitations

- ChromaDB does **not deduplicate** by default: uploading the same file twice adds its chunks twice.
- A single collection (`documents`) is shared globally; there is no per-user or per-collection separation.
- Large PDFs with many pages may increase ingestion time significantly because each page triggers an embedding API call batch.
