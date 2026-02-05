# CH1 — Introdução ao NLP, Métodos Clássicos, Tokenização e Embeddings

Este capítulo marca o início do módulo de Processamento de Linguagem Natural (NLP) no workshop. O foco está em apresentar a evolução histórica e conceitual das técnicas que possibilitam a interpretação e manipulação de texto por máquinas. O participante será guiado por uma narrativa que vai desde as abordagens “clássicas” de NLP até os fundamentos das representações vetoriais de linguagem, destacando não apenas como as técnicas funcionam, mas por que elas surgiram, quais problemas pretendem resolver e quais limitações enfrentam. A construção desse entendimento é essencial para fundamentar os capítulos subsequentes, que lidam com modelos neurais avançados, arquiteturas Transformer e sistemas de recuperação semântica.

A abordagem pedagógica deste capítulo enfatiza compreensão conceitual profunda, contextualização histórica e aplicação prática, permitindo que os participantes internalizem os motivos pelos quais certas técnicas foram desenvolvidas e como elas se conectam às metodologias modernas.

---

## O Papel das Técnicas “Clássicas” em NLP

Antes da popularização de redes neurais e de modelos de linguagem baseados em atenção, o NLP se apoiava em métodos derivados da linguística, estatística e análise simbólica. Esses métodos investem em regras explícitas, contagem de frequências, análise morfológica e sintática para extrair significado de texto. O termo “métodos clássicos” se refere, portanto, a abordagens como bag-of-words, n-gramas, TF-IDF e transformações baseadas em coocorrência de termos. Embora atualmente superados em muitos cenários pelos métodos baseados em redes neurais, esses métodos permanecem úteis por sua simplicidade, interpretabilidade e eficiência computacional em contextos com restrições de recursos.

No decorrer deste capítulo, o participante explorará como representar texto de forma que possa ser manipulado por algoritmos, quais são os trade-offs de diferentes representações e como tokenização, vetorização e normalização contribuem para esse processo.

---

## Tokenização — Dividindo Texto em Unidades Significativas

Tokenização refere-se ao processo de quebrar texto bruto em unidades menores que fazem sentido para a análise computacional. Essas unidades podem ser palavras, subpalavras ou até caracteres. O objetivo da tokenização é reduzir a complexidade da linguagem natural em elementos discretos que possam ser processados por funções matemáticas e algoritmos.

Neste capítulo, a tokenização é apresentada não apenas como uma etapa técnica, mas como um ponto de contato entre linguística e ciência de dados. Os participantes verão como decisões aparentemente simples, como a escolha entre tokenizar por palavras ou por subpalavras, têm implicações profundas sobre a capacidade de um sistema de lidar com vocabulário aberto, diferenças morfológicas e variação linguística.

A tokenização também é contextualizada historicamente: desde os primeiros sistemas que tratavam texto como sequência de palavras até as técnicas modernas que utilizam algoritmos de segmentação capazes de lidar com subpalavras e vocabulários dinâmicos.

---

## Embeddings — Representações Vetoriais de Textos

Com a tokenização definida, o próximo passo é aprender a mapear essas unidades textuais para espaços numéricos que preservem significado e similaridade semântica. Embeddings são vetores de números reais que representam palavras ou frases de forma que relações semânticas e sintáticas sejam preservadas geometricamente.

Este capítulo introduz os conceitos que levaram ao desenvolvimento de embeddings, explicando como representações vetoriais podem capturar padrões de uso e contexto, como medir similaridade entre vetores e por que embeddings transformaram a forma como sistemas de linguagem representam significado. A narrativa descreve o caminho desde abordagens baseadas em frequências até representações densas que capturam nuances semânticas, preparando o terreno para o estudo de embeddings contextuais em modelos mais avançados.

---

## Estrutura e Exercícios Incluídos

O material deste capítulo apresenta notebooks e scripts que permitem a experimentação prática das técnicas descritas. Os participantes terão a oportunidade de aplicar tokenizadores simples, construir representações vetoriais e observar, de forma prática, como diferentes escolhas de pré-processamento afetam a representação e a análise de texto.

A experiência prática está alinhada à narrativa conceitual: ao experimentar tokenização e vetorização, o participante reforça a compreensão de por que essas etapas são essenciais e como elas influenciam os resultados em tarefas posteriores de NLP.

---

## Ambiente e Pré-requisitos

Este capítulo pressupõe que o participante tenha conhecimentos básicos em Python e esteja familiarizado com o uso de terminal/linha de comando. É esperado que o ambiente de desenvolvimento contenha Python 3.9 ou superior e as bibliotecas necessárias para manipulação de texto e vetores. A instalação de dependências e a execução dos exemplos são facilitadas por meio de um ambiente virtual que isola os pacotes utilizados.

---

## Quickstart: Preparação do Ambiente

Comece clonando o repositório principal do workshop e navegando até o diretório do CH1 de NLP.

```bash
git clone https://github.com/seu-repo/workshop-nlp-mlops.git
cd workshop-nlp-mlops/nlp/CH1
```

Crie um ambiente virtual Python para isolar as dependências deste capítulo. Ative o ambiente e instale as bibliotecas listadas nos requisitos.

```bash
python -m venv .venv
source .venv/bin/activate   # Para sistemas Unix (Linux/Mac)
.venv\Scripts\activate      # Para Windows

pip install -r requirements.txt
```

---

## Quickstart: Executando Exemplos de Tokenização

Dentro do diretório do capítulo, um notebook está disponível para experimentação com técnicas de tokenização. Execute o notebook com o ambiente virtual ativado para observar diferentes formas de segmentar texto.

```bash
jupyter notebook notebooks/tokenization_demo.ipynb
```

Esse notebook inclui exemplos de tokenização baseada em espaços, regras simples de tokenização e exemplos de tokenizadores baseados em dicionários.

---

## Quickstart: Construindo Embeddings Simples

Um script está disponível para gerar representações vetoriais simples de tokens e visualizar similaridades. Com o ambiente virtual ativado, execute:

```bash
python scripts/run_embeddings_demo.py
```

Esse script carrega um conjunto de textos de exemplo, aplica tokenização e constrói vetores representativos utilizando técnicas clássicas como CountVectorizer e TF-IDF, permitindo observar como diferentes representações numéricas afetam a similaridade entre termos e frases.

---

## Resultados Esperados e Aplicações

Ao final deste capítulo, o participante deverá ser capaz de explicar por que a tokenização é uma etapa essencial em qualquer pipeline de NLP, como diferentes escolhas de representação influenciam a capacidade de máquinas lidar com texto, e como embeddings básicos já representam um avanço significativo em relação às representações simbólicas e discretas.

Esse entendimento servirá de base para os próximos capítulos, onde serão explorados modelos neurais avançados como RNNs, mecanismos de atenção, Transformers e arquiteturas modernas que impulsionaram o estado da arte em NLP.

---

## Conectando com os Próximos Capítulos

Com os conceitos de tokenização e embeddings consolidados, o participante estará preparado para mergulhar nos desafios associados a redes neurais sequenciais e mecanismos de atenção, que serão abordados no CH2. Esses tópicos ampliam a capacidade de representar e contextualizar significado em sequências de texto mais complexas, preparando o caminho para o uso de modelos Transformer e aplicações avançadas.
