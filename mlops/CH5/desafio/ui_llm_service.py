"""
Desafio CH5 — Interface de Chat para o Serviço LLM

Objetivo: construir uma UI de chat com Streamlit que consome
a API do serviço LLM rodando no Cloud Run.

Siga os comentários marcados com TODO para implementar cada parte.
Não existe uma única forma certa — use a estrutura abaixo como guia.

Dependências:
    pip install streamlit requests

Como rodar:
    export API_URL=https://seu-servico-xxxx-uc.a.run.app
    streamlit run ui_llm_service.py
"""

# TODO: importe as bibliotecas necessárias
# Dica: você vai precisar de streamlit e requests

import streamlit as st
import requests
import os

# ------------------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# Dica: st.set_page_config() deve ser a primeira chamada Streamlit
# ------------------------------------------------------------
st.set_page_config(page_title="LLM ChatBot", layout="wide")
                   
# TODO: configure o título da página e um ícone (opcional)


# ------------------------------------------------------------
# TÍTULO E DESCRIÇÃO
# ------------------------------------------------------------

# TODO: adicione um título e uma breve descrição do que este chat faz
st.title("🤖 Interface de Serviço LLM")
st.caption("Conectado ao Cloud Run + Gemini. Assistente virtual para responder todas suas perguntas.")

# ------------------------------------------------------------
# URL DA API
# Dica: nunca cole a URL diretamente no código.
#       Leia de uma variável de ambiente com os.getenv().
#       Defina um valor padrão para facilitar testes locais.
# ------------------------------------------------------------
API_URL = os.getenv("https://api-blackbox-68490838153.us-central1.run.app"," http://localhost:8080")
ENDPOINT = f"https://api-blackbox-68490838153.us-central1.run.app/chat"
st.info(f"Conectado em: https://api-blackbox-68490838153.us-central1.run.app")
# TODO: leia a variável de ambiente API_URL


# ------------------------------------------------------------
# HISTÓRICO DE MENSAGENS
# Para que o chat "lembre" das mensagens anteriores durante
# a sessão, você precisa armazená-las em st.session_state.
#
# Estrutura sugerida para cada mensagem:
#   {"role": "user" | "assistant", "content": "texto aqui"}
#
# Dica: inicialize a lista apenas se ela ainda não existir.
# ------------------------------------------------------------

# TODO: inicialize st.session_state["messages"] se necessário
if "messages" not in st.session_state:
    st.session_state.messages = []
with st.sidebar:
    st.header("Configurações")
    if st.button("Limpar Histórico"):
        st.session_state["messages"] = []
        st.rerun()
    st.caption(f"Conectado em: {API_URL}")
# ------------------------------------------------------------
# EXIBIÇÃO DO HISTÓRICO
# Renderize as mensagens já existentes na tela.
# Dica: st.chat_message(role) cria o balão correto para cada papel.
# ------------------------------------------------------------

# TODO: percorra st.session_state["messages"] e exiba cada uma

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ------------------------------------------------------------
# FUNÇÃO DE CHAMADA À API
# Encapsule a lógica HTTP em uma função separada.
# Isso facilita testes e deixa o código mais organizado.
#
# Assinatura sugerida:
#   def call_llm(messages: list[dict]) -> str
#
# O que ela deve fazer:
#   1. Montar o payload no formato que a API espera
#      (consulte /docs do seu serviço para ver o schema)
#   2. Fazer um POST para {API_URL}/chat
#   3. Extrair e retornar apenas o texto da resposta
#   4. Em caso de erro, retornar uma mensagem amigável
#      (não deixe o erro estourar na tela do usuário)
#
# Dica: use requests.post() com o parâmetro json= para o payload
# Dica: inspecione response.json() para ver o que a API retorna
# ------------------------------------------------------------

# TODO: implemente a função call_llm

def call_llm(messages):
    payload ={
            "messages": [{"role": "user", "content": prompt}],
            "model": "gemini-2.5-flash"
            }
    try:
            response = requests.post(
                ENDPOINT,
                json=payload,
                timeout=30 
            ) 
            
            if response.status_code == 200:
                return response.json().get("message").get("content")
            else:
                return f"Erro na API ({response.status_code}): {response.text}"
            
    except requests.exceptions.RequestException as e:
        return f"Falha de conexão: {e}"

# ------------------------------------------------------------
# CAIXA DE ENTRADA DO USUÁRIO
# Dica: st.chat_input() fica fixo na parte inferior da tela
#       e retorna o texto digitado (ou None se vazio).
# ------------------------------------------------------------
if prompt := st.chat_input("Olá! Como posso ajudar você hoje?"):

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("O Assistente está processando..."):

            resposta_llm = call_llm(st.session_state.messages)
            
            st.markdown(resposta_llm)
    
    st.session_state.messages.append({"role": "assistant", "content": resposta_llm})

# TODO: capture a entrada do usuário com st.chat_input()

# Quando o usuário enviar uma mensagem, você deve:
#   1. Adicioná-la ao histórico (role: "user")
#   2. Exibi-la na tela imediatamente
#   3. Chamar a função call_llm com o histórico completo
#   4. Adicionar a resposta ao histórico (role: "assistant")
#   5. Exibir a resposta na tela

# TODO: implemente o fluxo acima


# ------------------------------------------------------------
# DICAS FINAIS
#
# - st.spinner("...") exibe um indicador de carregamento
#   enquanto a API responde — melhora muito a experiência
#
# - st.error("...") exibe mensagens de erro em vermelho
#
# - Se quiser limpar o histórico, st.button("Nova conversa")
#   combinado com del st.session_state["messages"] funciona bem
#
# - Explore st.sidebar para colocar configurações (ex: URL da API,
#   temperatura do modelo) fora da área principal do chat
# ------------------------------------------------------------
