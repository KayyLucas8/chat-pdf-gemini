import pypdf #biblioteca para manipulação de pdf

def extract_text_from_pdf(pdf_file)
    """ 
    função para extrair o texto de um pdf carregado no Streamlit.
    
    Parâmetros: 
    pdf_file (UploadedFile) Arquivo pdf carregado pelo usuário
    
    Retorna:
    str: texto extraído do pdf
    """ 
    
    reader = pypdf.PdfReader(pdf_file) #cria um objeto para ler o pdf
    
    # Percorre todas as páginas e extrai o texto disponível
    
    text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return text  
    #retorna o texto extraído