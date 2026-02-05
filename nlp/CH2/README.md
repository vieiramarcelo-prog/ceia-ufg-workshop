# CH2 – Redes Recorrentes, Atenção e Transformers

## Visão Geral do Capítulo

Este capítulo aprofunda a evolução dos modelos neurais aplicados ao Processamento de Linguagem Natural, partindo das redes recorrentes clássicas, passando pelos mecanismos de atenção e culminando na arquitetura Transformer. O objetivo é construir uma compreensão conceitual sólida sobre como modelos modernos lidam com sequências textuais, capturam contexto de longo alcance e superam limitações estruturais das abordagens anteriores.

Ao longo deste módulo, o participante compreende não apenas como esses modelos funcionam matematicamente e arquiteturalmente, mas também como utilizá-los na prática por meio de bibliotecas modernas, com foco em prototipagem, experimentação e preparação para aplicações em produção.

## Redes Neurais Recorrentes e Modelagem Sequencial

As Redes Neurais Recorrentes foram desenvolvidas para lidar com dados sequenciais, nos quais a ordem dos elementos importa. Diferentemente de redes feedforward tradicionais, as RNNs mantêm um estado interno que permite incorporar informações de passos anteriores ao processar um novo token. Isso torna possível modelar dependências temporais em textos, como concordância gramatical, coesão semântica e relações entre palavras distantes em uma frase.

Apesar de sua relevância histórica, as RNNs apresentam limitações estruturais importantes. O treinamento sequencial impede paralelização eficiente, o que aumenta o custo computacional. Além disso, problemas como desvanecimento e explosão de gradientes dificultam o aprendizado de dependências de longo prazo, mesmo em variações como LSTM e GRU.

Este contexto motiva o surgimento de mecanismos mais sofisticados para lidar com memória, contexto e escalabilidade.

## Mecanismos de Atenção e o Fim da Dependência Sequencial Estrita

Os mecanismos de atenção introduzem um novo paradigma no qual o modelo não precisa depender exclusivamente do estado anterior para interpretar uma sequência. Em vez disso, ele aprende a atribuir pesos dinâmicos à relevância de diferentes tokens ao construir uma representação contextual.

Na prática, a atenção permite que o modelo foque seletivamente em partes mais informativas do texto ao processar uma palavra específica. Esse processo é formalizado por meio de vetores de consulta, chave e valor, que determinam como cada token se relaciona com os demais. Isso possibilita capturar relações de longo alcance sem as restrições impostas pelas estruturas recorrentes.

A autoatenção, em especial, aplica esse princípio dentro da própria sequência, permitindo que cada token seja interpretado com base em todos os outros simultaneamente.

## Transformers e a Arquitetura Baseada em Atenção

A arquitetura Transformer surge como uma ruptura com RNNs e CNNs ao eliminar completamente a recorrência e basear-se exclusivamente em mecanismos de atenção e camadas feedforward. Essa abordagem permite processamento paralelo de tokens, melhor aproveitamento de hardware moderno e maior escalabilidade para grandes volumes de dados.

Transformers são organizados em blocos compostos por camadas de autoatenção multi-head, normalização, redes feedforward e codificações posicionais, que preservam a informação de ordem sem exigir processamento sequencial.

Essa arquitetura tornou-se a base de modelos como BERT, GPT, T5 e outras famílias de modelos de linguagem de larga escala, sendo hoje o padrão dominante em NLP moderno.

## Aplicações Práticas em NLP Moderno

A adoção de Transformers impulsionou avanços significativos em tarefas como tradução automática, sumarização, análise de sentimento, recuperação de informação, geração de texto e sistemas conversacionais. A flexibilidade da arquitetura permite adaptação tanto para tarefas supervisionadas quanto para pré-treinamento em larga escala seguido de fine-tuning.

Além disso, a combinação entre Transformers e embeddings contextuais redefiniu como representações semânticas são utilizadas em pipelines modernos, incluindo sistemas de RAG, busca semântica e agentes baseados em linguagem.

## Quickstart: Ambiente para Experimentos com RNNs e Transformers

Para reproduzir os experimentos deste capítulo, recomenda-se configurar um ambiente Python com bibliotecas modernas de deep learning e NLP.

Criação do ambiente virtual e instalação das dependências principais:

```bash
python -m venv .venv
source .venv/bin/activate
pip install torch transformers datasets sentencepiece accelerate
```

Verificação rápida do funcionamento do PyTorch:

```bash
python -c "import torch; print(torch.__version__)"
```

## Quickstart: Executando um Modelo Transformer Pré-Treinado

O comando abaixo demonstra como carregar um modelo Transformer e gerar embeddings ou inferência textual utilizando a biblioteca Hugging Face.

```bash
python - << 'EOF'
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "This workshop on NLP is extremely valuable."
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)

logits = outputs.logits
pred = torch.argmax(logits, dim=1)

print("Prediction:", pred.item())
EOF
```

## Quickstart: Comparando RNN e Transformer em Modelagem de Texto

O trecho abaixo ilustra como estruturar um experimento simples para comparar arquiteturas sequenciais tradicionais e Transformers em tarefas de NLP.

```bash
python - << 'EOF'
from transformers import AutoTokenizer, AutoModel
import torch

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

text = "Neural networks revolutionized natural language processing."
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)

embedding = outputs.last_hidden_state.mean(dim=1)
print("Embedding shape:", embedding.shape)
EOF
```

## Conexão com os Próximos Capítulos

Este capítulo estabelece a base teórica e prática para compreender os modelos que sustentam embeddings modernos, recuperação de informação e sistemas RAG. O entendimento profundo de RNNs, atenção e Transformers prepara o terreno para os próximos módulos, que exploram embeddings avançados, vetorização semântica, bancos vetoriais e arquiteturas de busca aumentada por recuperação.

Caso queira, posso manter o mesmo padrão e criar o README do CH3 de NLP com continuidade conceitual direta a partir deste capítulo.
