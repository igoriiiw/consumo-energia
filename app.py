# Calculadora de Consumo de Energia Elétrica

# Entrada de dados
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho (em watts): "))
tempo_diario = float(input("Digite o tempo diário de uso do aparelho (em horas): "))

# Processamento - Cálculo do consumo diário (em kWh)
consumo_diario = (potencia * tempo_diario) / 1000
consumoMensal = consumo_diario * 30  # Considerando 30 dias no mês
custoMensalestimado = consumoMensal * 0.787  # Considerando o custo de R$ 0,787 por kWh

# Saída de dados
print(f"\nAparelho: {aparelho}")
print(f"Consumo Diário: {consumo_diario:.2f} kWh")
print(f"Consumo Mensal: {consumoMensal:.2f} kWh")
print(f"Custo Mensal Estimado: R$ {custoMensalestimado:.2f}")