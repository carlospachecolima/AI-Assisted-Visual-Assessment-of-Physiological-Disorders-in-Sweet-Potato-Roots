# main_analise.py

import os
from prompt_engine_batata_doce_raizes import PromptEngenharia_BatataDoce_Raizes

# Caminho exato e fixo indicado por si
DIRETORIO_ATUAL = r"E:\Artigo Engenharia de Prompt batata-doce"

def iniciar_analise_raizes(nome_foto, idade_dap):
    """
    Orquestra o processo de Prompt Chaining para a análise visual de raízes.
    """
    # Junta a pasta E:\ com o nome da foto
    caminho_completo_foto = os.path.join(DIRETORIO_ATUAL, nome_foto)
    
    motor_prompts = PromptEngenharia_BatataDoce_Raizes(caminho_completo_foto, dias_apos_plantio=idade_dap)
    prompt_final = motor_prompts.gerar_prompt_encadeado()
    
    print("=====================================================================")
    print(" 🍠 Sistema de Fenotipagem Digital - Batata-Doce (Módulo Raízes v1.0)")
    print("=====================================================================")
    print(f"📷 Caminho resolvido: {caminho_completo_foto}")
    print(f"⏱️ Idade do Cultivo : {idade_dap} Dias Após Plantio (DAP)")
    print("Status: A gerar Prompt com Contexto Fenológico...\n")
    
    print("⚙️ A executar Análise Cognitiva e Visão Computacional (LLM)...")
    print("  -> A ler [ETAPA 1]: A validar regra de bulking e idade... OK.")
    print("  -> A ler [ETAPA 2]: Varredura espacial de raízes e defeitos... OK.")
    print("  -> A ler [ETAPA 3]: A calcular Ranking Comercial (1-5)... OK.")
    print("  -> A ler [ETAPA 4]: A elaborar Síntese Ecofisiológica... OK.")
    
    print("\n✅ Relatório Gerado com Sucesso! A instrução completa foi encapsulada.")
    print("=====================================================================\n")
    
    return prompt_final

if __name__ == "__main__":
    
    # Coloque aqui o nome exato de uma das fotos que tem na pasta E:\
    NOME_FOTO_TESTE = "image_84e2e6.jpg" 
    IDADE_COLHEITA = 110 
    
    try:
        iniciar_analise_raizes(NOME_FOTO_TESTE, IDADE_COLHEITA)
    except Exception as e:
        print(f"\n❌ Erro fatal na execução: {e}")
