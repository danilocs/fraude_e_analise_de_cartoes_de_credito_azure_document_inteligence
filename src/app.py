import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analize_credit_card


def configure_interface():
    st.title("Upload de Arquivo DIO - Desafio I - Azure - Fake Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        fileName = uploaded_file.name
        
        #Enviar para o Blob
        blob_url = upload_blob(uploaded_file, fileName)

        if blob_url:
            st.write(f"Arquivo {fileName} enviado com sucesso")
            credit_card_info = analize_credit_card(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        
        else:
            st.write(f"Erro ao enviar o arquivo {fileName} para o Azure Blob Storage")

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem enviada.", use_column_width=True)
    st.write("Resultado da Validação:")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"Cartão de Crédito Válido")
        st.write(f"Nome do Titular: {credit_card_info['card_name']}")
        st.write(f"Número do Cartão: {credit_card_info['card_number']}")
        st.write(f"Data de Validade: {credit_card_info['expire_date']}")
    else:
        st.markdown(f"Este não é um cartão de crédito válido.")


    st.write("Informações da cartão de crédito encontradas:")
    st.write(credit_card_info)


if __name__ == "__main__":
    configure_interface()