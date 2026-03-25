# prompt_engine_batata_doce_raizes.py

class PromptEngenharia_BatataDoce_Raizes:
    """
    Módulo exclusivo para análise visual e diagnóstico ecofisiológico de 
    raízes tuberosas de batata-doce (Ipomoea batatas).
    """
    def __init__(self, caminho_foto: str, dias_apos_plantio: int):
        self.caminho_foto = caminho_foto
        self.dias_apos_plantio = dias_apos_plantio
        
        # ----------------------------------------------------------------------
        # PROMPT 1: PERSONA (Especialista em Tuberosas)
        # ----------------------------------------------------------------------
        self.P1_PERSONA = (
            "Assuma a persona de um Engenheiro Agrónomo e Ecofisiologista, "
            "especialista em qualidade comercial e desenvolvimento de raízes tuberosas "
            "(Ipomoea batatas). O seu foco é diagnosticar o histórico de estresses abióticos "
            "(seca, calor extremo ou flutuação hídrica) com base na anatomia final da raiz."
        )
        
        # ----------------------------------------------------------------------
        # PROMPT 2: CONTEXTO E FENOLOGIA (A Regra do Dreno)
        # ----------------------------------------------------------------------
        self.P2_CONTEXTO = (
            f"CONTEXTO DA AMOSTRA:\n"
            f"- Ficheiro de imagem: '{self.caminho_foto}'\n"
            f"- Idade do cultivo informada: {self.dias_apos_plantio} Dias Após o Plantio (DAP).\n\n"
            f"REGRA FENOLÓGICA (Obrigatória):\n"
            f"O período crítico de enchimento (bulking) ocorre antes dos 90-100 DAP. "
            f"Se a idade informada for superior a 90 DAP e as raízes apresentarem calibre "
            f"muito fino, fibroso ou lignificado, classifique rigorosamente como falha de "
            f"translocação de fotoassimilados (estresse crónico), e não como raiz imatura."
        )
        
        # ----------------------------------------------------------------------
        # PROMPT 3: FENOTIPAGEM VISUAL (Atributos Anatómicos)
        # ----------------------------------------------------------------------
        self.P3_OBSERVACAO = (
            "Analise as raízes visíveis na imagem (se houver mais de uma, descreva os "
            "padrões predominantes ou isole-as espacialmente). Descreva:\n"
            "1) Calibre e Formato: Houve expansão radial adequada (raízes elípticas/ovais) "
            "ou há constrições centrais (estrangulamento) e formato filiforme/cordão?\n"
            "2) Integridade da Periderme (Pele): Identifique a presença de rachaduras "
            "longitudinais (growth cracks), ranhuras ou textura excessivamente fibrosa.\n"
            "3) Desordens Secundárias: Sinais de brotamento precoce (sprouting) ou podridão."
        )
        
        # ----------------------------------------------------------------------
        # PROMPT 4: RANKING COMERCIAL (A Métrica Prática)
        # ----------------------------------------------------------------------
        self.P4_RANKING = (
            "Atribua uma Nota de Qualidade Comercial e Resiliência (1 a 5):\n"
            "- Nota 5 (Excelente): Raiz lisa, formato uniforme, sem rachaduras. Calibre ideal.\n"
            "- Nota 4 (Boa): Leves deformações superficiais ou tortuosidade.\n"
            "- Nota 3 (Moderada): Constrições visíveis (crescimento irregular) ou calibre subdesenvolvido.\n"
            "- Nota 2 (Ruim): Rachaduras longitudinais profundas (cracking) ou raízes muito finas aos >90 DAP.\n"
            "- Nota 1 (Falha/Refugo): Lignificação total, raízes filiformes sem amido ou dano físico catastrófico.\n\n"
            "Saída obrigatória:\n"
            "Avaliação: [Resumo visual da raiz]\n"
            "Diagnóstico: [Raiz Normal / Estresse por Flutuação Hídrica / Déficit Crónico de Dreno]\n"
            "Nota: [1-5]"
        )
        
        # ----------------------------------------------------------------------
        # PROMPT 5: SÍNTESE ECOFISIOLÓGICA (Justificação Científica)
        # ----------------------------------------------------------------------
        self.P5_SINTESE = (
            "Sintetize a avaliação ecofisiológica conectando o fenótipo ao ambiente:\n"
            "1. Se detetar rachaduras (*cracking*): Explique a mecânica da flutuação hídrica "
            "(seca que enrijece a casca, seguida de rápida reidratação que rompe o parênquima).\n"
            "2. Se detetar afinamento/fibrose: Explique a falha na força do dreno (*sink strength*) "
            "devido à inibição da fotossíntese na parte aérea durante a fase de *bulking*.\n"
            "3. Se a raiz for ideal (Nota 5): Confirme a manutenção da homeostase e do fluxo de carbono."
        )

    def gerar_prompt_encadeado(self) -> str:
        """
        Combina os módulos num único fluxo de pensamento lógico (Chain-of-Thought).
        """
        return (
            f"{self.P1_PERSONA}\n\n"
            f"[ETAPA 1 - CONTEXTUALIZAÇÃO FENOLÓGICA]\n{self.P2_CONTEXTO}\n\n"
            f"[ETAPA 2 - FENOTIPAGEM DA RAIZ]\n{self.P3_OBSERVACAO}\n\n"
            f"[ETAPA 3 - RANKING DE DESEMPENHO]\n{self.P4_RANKING}\n\n"
            f"[ETAPA 4 - SÍNTESE ECOFISIOLÓGICA]\n{self.P5_SINTESE}"
        )

# Exemplo de uso no seu main.py:
# motor = PromptEngenharia_BatataDoce_Raizes(caminho_foto="raiz_experimento.jpg", dias_apos_plantio=110)
# prompt_para_llm = motor.gerar_prompt_encadeado()