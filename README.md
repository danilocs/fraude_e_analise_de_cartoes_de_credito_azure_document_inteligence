# fraude_e_analise_de_cartoes_de_credito_azure_document_inteligence

# 💳 Upload de Arquivo DIO - Desafio I - Azure - Fake Docs

Este projeto foi desenvolvido como parte de um desafio da **DIO** utilizando os serviços da **Azure**.  
A aplicação permite que o usuário faça o upload de uma imagem de cartão de crédito, que é enviada para o **Azure Blob Storage** e processada pelo serviço **Azure Document Intelligence**.  
O sistema então retorna os dados extraídos do cartão e valida se o documento é um cartão de crédito válido.

---

## 🚀 Tecnologias Utilizadas
- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/) para a interface web
- [Azure Blob Storage](https://azure.microsoft.com/services/storage/blobs/) para armazenamento dos arquivos
- [Azure Document Intelligence](https://learn.microsoft.com/azure/ai-services/document-intelligence/) para análise e extração dos dados do cartão

---

## 🖥️ Como funciona
1. O usuário acessa a interface web criada com **Streamlit**.
2. Faz o upload de uma imagem (`.png`, `.jpg`, `.jpeg`) de um cartão de crédito.
3. O arquivo é enviado para o **Azure Blob Storage**.
4. O **Azure Document Intelligence** processa a imagem e retorna os dados extraídos:
   - Nome do titular
   - Número do cartão
   - Data de validade
   - Banco emissor (quando disponível)
5. A aplicação exibe os resultados na tela, informando se o cartão é válido ou não.

---

## 📸 Exemplo de Uso
Após o upload de uma imagem de cartão, a aplicação exibe o resultado da validação e os dados extraídos.  

<img width="454" height="901" alt="Sem título" src="https://github.com/user-attachments/assets/fff245e3-91e8-4156-bba8-ff46a11c061b" />

---


## ⚙️ Bibliotecas a serem instaladas na Venv (PIP)

azure.core
azure-ai-documentintelligence
azure-storage-blob
python-dotenv
streamlit

## ⚙️ Como executar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git

### 2. Ao entrar na Venv, execute o comando abaixo e o arquivo app.py como parâmetro.
```bash
streamlit run .\src\app.py
