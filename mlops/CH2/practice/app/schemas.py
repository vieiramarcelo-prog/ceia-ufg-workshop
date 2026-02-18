from pydantic import BaseModel
from typing import List, Dict, Optional

class IngestRequest(BaseModel):
    texts: List[str]
    source: str = "user_upload"

class IngestResponse(BaseModel):
    collection: str
    inserted: int

class SearchRequest(BaseModel):
    query: str
    top_k: int = 3

class SearchResponse(BaseModel):
    results: List[Dict]

class AskRequest(BaseModel):
    question: str
    top_k: int = 3

class AskResponse(BaseModel):
    answer: str
    context: List[Dict]
    # Educational fields
    retrieved_docs: List[str] # Simple list of texts
    built_prompt: str         # The exact prompt sent to LLM
