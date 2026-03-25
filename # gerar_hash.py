# gerar_hash.py

import os
import zipfile
import hashlib

# Caminho exato e fixo indicado por si
DIRETORIO_ATUAL = r"E:\Artigo Engenharia de Prompt batata-doce"
NOME_ARQUIVO_ZIP = "Pacote_INPI_BatataDoce.zip"
CAMINHO_ZIP = os.path.join(DIRETORIO_ATUAL, NOME_ARQUIVO_ZIP)

def empacotar_e_gerar_hash():
    """Cria o ZIP com os códigos fonte e gera o Hash SHA-256 para o INPI."""
    
    print("📦 1. A compactar os ficheiros Python para o INPI...")
    
    # Cria o arquivo ZIP diretamente na sua pasta E:
    with zipfile.ZipFile(CAMINHO_ZIP, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for arquivo in os.listdir(DIRETORIO_ATUAL):
            # Pega apenas os arquivos Python, ignorando o próprio ZIP se já existir
            if arquivo.endswith('.py'):
                caminho_completo = os.path.join(DIRETORIO_ATUAL, arquivo)
                zipf.write(caminho_completo, arquivo)
                print(f"  + Adicionado ao pacote: {arquivo}")

    print(f"\n🔐 2. A calcular o Hash SHA-256 do ficheiro '{NOME_ARQUIVO_ZIP}'...")
    
    hash_sha256 = hashlib.sha256()
    with open(CAMINHO_ZIP, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            hash_sha256.update(byte_block)
            
    return hash_sha256.hexdigest()

if __name__ == "__main__":
    print("\n" + "="*65)
    print(" 🔐 GERADOR AUTOMÁTICO DE PACOTE E HASH - INPI")
    print("="*65)
    
    try:
        resultado_hash = empacotar_e_gerar_hash()
        
        print("\n✅ SUCESSO! CÓDIGO HASH GERADO:")
        print("-" * 65)
        print(resultado_hash)
        print("-" * 65)
        print(f"\n📋 INSTRUÇÃO: ")
        print(f"1. Copie o código acima e cole no formulário do e-Software.")
        print(f"2. Guarde o ficheiro '{NOME_ARQUIVO_ZIP}' que acabou de ser criado na pasta E:\\")
        print("="*65 + "\n")
        
    except Exception as e:
        print(f"\n❌ Erro durante a execução: {e}")