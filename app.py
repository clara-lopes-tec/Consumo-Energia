
# Coleta dos dados
aparelho = input("Digite o nome do aparelho. ")
potencia = float(input(f"Qual a potência do(a) {aparelho} em Watts (W)? "))
horas_dia = float(input(f"Quantas horas por dia o(a) {aparelho} é usado(a)? "))

# Cálculo do consumo mensal (kWh)
# Fórmula: (Potência * Horas * 30 dias) / 1000
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Cálculo de custo (Bônus: R$ 0,75 por kWh)
custo_estimado = consumo_mensal * 0.75

# 4. Exibição do resultado
print("\n" + "="*30)
print(f"Análise de consumo de {aparelho}")
print(f"Consumo: {consumo_mensal:.2f} kWh/mês")
print(f"Custo Estimado: R$ {custo_estimado:.2f}")
print("="*30)