import Funcoes.Funcoescopa as F

dados = F.Importar_dados()
melhoretimespor_grupo = F.Fase_de_grupo(dados)
F.Exibir_resultado_fase_grupo(melhoretimespor_grupo)

# Criando vaiáveis para as 2 melhores seleções de cada grupo:
c = F.Classificados_to_oitavas(melhoretimespor_grupo)

# Confrontos das oitavas
oit = F.Confrontos_oitavas(c)

# Conforntos das quartas de finais:
quar = F.Confrontos_quartas(oit)

# Confrontos das semifinais:
fi = F.Confrontos_semis(quar)

# Jogos finais:
F.Finais(fi)

