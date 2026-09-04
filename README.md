# ⚡Calculadora de Consumo de Energia Elétrica

Projeto desenvolvido em Python para calcular o consumo diário e mensal de um aparelho elétrico, além de estimar o custo mensal de energia.


## 🎯 Objetivo

O programa solicita:

🔌 Nome do aparelho;<br>
⚡ Potência em watts (W);<br>
⏱️ Tempo diário de uso em horas.<br>

A partir desses dados, calcula o consumo diário, o consumo mensal e o custo mensal estimado.


## 🧮 Cálculos

### Consumo diário
consumo_diario = (potencia × tempo_diario) / 1000

### Consumo mensal
Considerando 30 dias:
consumoMensal = consumo_diario × 30

### Custo mensal
Considerando o valor de R$ 0,787 por kWh:
custoMensalestimado = consumoMensal × 0,787


## ▶️ Como executar

É necessário ter o Python 3 instalado.

No terminal, execute:<br>
python app.py

No Windows, também pode ser utilizado:<br>
py app.py

Depois, basta informar os dados solicitados pelo programa.


## 💻 Exemplo

### ➡️ Entrada de dados

1. Digite o nome do aparelho: Geladeira<br>
2. Digite a potência do aparelho (em watts): 500<br>
3. Digite o tempo diário de uso do aparelho (em horas): 3<br>

### &nbsp;↳&nbsp; Resultados
Aparelho: Geladeira<br>
Consumo Diário: 1.50 kWh<br>
Consumo Mensal: 45.00 kWh<br>
Custo Mensal Estimado: R$ 35.42<br>

<div align="center">

 ### 🐍 <u>Projeto desenvolvido para fins de estudo em Desenvolvimento de Sistemas.</u><br>

</div>

<div align="center">
&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="70"/>&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/github/FFFFFF"
     alt="GitHub"
     width="70"
     height="70">&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.3/assets/svg/26a1.svg"
     alt="Energia"
     width="70"
     height="70">&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.3/assets/svg/1f4b0.svg"
     alt="Economia"
     width="70"
     height="70">&nbsp;&nbsp;&nbsp;&nbsp;
</div>