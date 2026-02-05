# CH4 — Prática com Bancos Vetoriais e Criação de Sistemas RAG

## Contexto e Objetivo do Capítulo

Este capítulo tem como foco a aplicação prática dos conceitos apresentados nos módulos anteriores, consolidando o uso de embeddings, recuperação de informação e arquiteturas de Retrieval-Augmented Generation (RAG). O objetivo é capacitar o participante a estruturar um pipeline funcional que envolve a criação de um banco vetorial, a ingestão de documentos, a indexação semântica e a construção de um sistema capaz de recuperar conhecimento relevante para alimentar modelos de linguagem.

A proposta deste capítulo é aproximar o participante de cenários reais de produção, nos quais sistemas RAG são utilizados para reduzir alucinações em modelos de linguagem, ampliar o acesso a bases privadas de conhecimento e criar aplicações inteligentes baseadas em busca semântica.

## Criação e Estruturação de um Banco Vetorial

O primeiro componente fundamental abordado neste capítulo é a construção de um banco vetorial, responsável por armazenar embeddings gerados a partir de textos ou documentos. Esses embeddings representam semanticamente o conteúdo textual e permitem a realização de buscas por similaridade.

O banco vetorial atua como a base de um sistema de recuperação semântica, possibilitando a indexação de grandes volumes de informação e a execução de consultas baseadas em proximidade vetorial. Durante a prática, os participantes configuram um serviço de banco vetorial e implementam um pipeline básico de inserção, consulta e recuperação de vetores.

### Quickstart para Instanciar um Banco Vetorial com Docker

```bash
docker run -p 6333:6333 qdrant/qdrant
```

Após a inicialização do serviço, é possível verificar a disponibilidade da instância acessando a API HTTP local.

```bash
curl http://localhost:6333/collections
```

## Geração de Embeddings para Indexação

Com o banco vetorial em execução, o próximo passo consiste na geração de embeddings para os documentos que serão indexados. Essa etapa envolve a utilização de modelos especializados em representação semântica, normalmente disponibilizados via bibliotecas como Sentence Transformers ou APIs de modelos pré-treinados.

Os embeddings gerados são vetores numéricos de alta dimensionalidade que capturam o significado do conteúdo textual, permitindo buscas por similaridade semântica em vez de simples correspondência de palavras-chave.

### Quickstart para Gerar Embeddings com Sentence Transformers

```bash
pip install sentence-transformers
```

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
embedding = model.encode("Exemplo de texto para indexação")
```

## Inserção de Dados no Banco Vetorial

Após a geração dos embeddings, os vetores são persistidos no banco vetorial juntamente com metadados associados, como identificadores, trechos de texto e referências ao documento original. Essa associação é essencial para permitir a reconstrução do contexto no momento da recuperação.

A prática inclui a criação de coleções, a inserção de vetores e a validação do armazenamento correto dos dados.

### Quickstart para Inserção de Vetores no Qdrant

```python
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct

client = QdrantClient(host="localhost", port=6333)

client.upsert(
    collection_name="documentos",
    points=[
        PointStruct(
            id=1,
            vector=embedding.tolist(),
            payload={"texto": "Conteúdo do documento"}
        )
    ]
)
```

## Recuperação de Informação Baseada em Similaridade

Uma vez que os vetores estão indexados, o sistema pode realizar buscas semânticas para recuperar os documentos mais relevantes com base na similaridade vetorial. Esse mecanismo é o núcleo da etapa de recuperação em arquiteturas RAG.

O capítulo explora o funcionamento de consultas vetoriais, métricas de similaridade, parâmetros de busca e técnicas para otimizar a relevância dos resultados recuperados.

### Quickstart para Consulta Semântica

```python
resultados = client.search(
    collection_name="documentos",
    query_vector=model.encode("Pergunta do usuário").tolist(),
    limit=5
)
```

## Construção de um Pipeline de Retrieval-Augmented Generation (RAG)

Com a recuperação semântica funcional, o próximo passo é integrar os resultados obtidos ao contexto de um modelo de linguagem. Essa integração permite que o modelo gere respostas fundamentadas em documentos externos, reduzindo a dependência exclusiva do conhecimento aprendido durante o treinamento.

O pipeline RAG estruturado neste capítulo envolve a consulta ao banco vetorial, a seleção dos trechos mais relevantes, a montagem de um prompt enriquecido e a geração da resposta pelo modelo de linguagem.

### Quickstart para Integração com um Modelo de Linguagem

```python
contexto = "\n".join([r.payload["texto"] for r in resultados])

prompt = f"""
Use o contexto abaixo para responder à pergunta.

Contexto:
{contexto}

Pergunta:
{pergunta}
"""

resposta = llm.generate(prompt)
```

## Criação de um Serviço de API para um Sistema RAG

Como etapa final, o capítulo aborda a disponibilização do sistema RAG como um serviço acessível via API. Essa prática aproxima o participante de cenários reais de produção, nos quais sistemas de recuperação e geração são expostos como microsserviços consumíveis por aplicações web, chatbots ou sistemas corporativos.

A API implementada permite receber uma pergunta do usuário, consultar o banco vetorial, montar o contexto e retornar uma resposta gerada dinamicamente.

### Quickstart para Criar uma API RAG com FastAPI

```bash
pip install fastapi uvicorn
```

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/rag")
def consultar(pergunta: str):
    resultados = buscar_no_banco(pergunta)
    resposta = gerar_resposta(resultados, pergunta)
    return {"resposta": resposta}
```

```bash
uvicorn app:app --reload
```

## Conclusão e Continuidade

Este capítulo consolida o aprendizado prático sobre recuperação semântica e arquiteturas RAG, permitindo que o participante experimente a construção de um sistema funcional que conecta bancos vetoriais, embeddings e modelos de linguagem.

A experiência adquirida aqui serve como base para aplicações mais avançadas em produção, incluindo chatbots corporativos, buscadores semânticos, assistentes inteligentes e sistemas de suporte à decisão baseados em conhecimento.
