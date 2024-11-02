# aps-carteira-financeira
Atividade Supervisionada – Otimização de Sistemas
Atividade Supervisionada
Professor: Sérgio Assunção Monteiro
1. A atividade deve ser entregue individualmente no local apropriado do AVA
2. As resoluções da atividade devem ser digitadas
3. A atividade deve conter:
• Otimização de Sistemas
• Código da Turma: 962
• José Alexandre
Matrícula: 2020100528
4. A data de entrega é até 04/Novembro/2024.
5. Todas as respostas devem ser justificadas.

Carteira de Investimentos
Descrição
Este projeto é uma ferramenta de carteira de investimentos que permite aos usuários criar e gerenciar suas próprias carteiras de investimentos. A ferramenta utiliza dados de mercado para calcular o retorno e o risco dos ativos e fornece recomendações de alocação de ativos.

1. Definição do Problema e Objetivo
O problema é similar ao problema clássico da mochila, onde queremos maximizar o "valor" (neste caso, o retorno esperado) da "mochila" (a carteira de investimentos) sem ultrapassar um "peso" máximo (o risco aceitável). No caso da carteira de investimentos, os ativos têm dois atributos principais:
    Retorno Esperado: Analogamente ao valor dos itens em uma mochila.
    Risco (Volatilidade): Considerado como o "peso" ou custo de cada ativo em termos de variabilidade ou incerteza.
2. Modelo Matemático
Função Objetivo:
A função objetivo aqui é maximizar o retorno esperado da carteira, definido como a média ponderada dos retornos dos ativos, onde temos:
 o retorno esperado do ativo;
  a fração alocada ao ativo;
  o número de ativos na carteira.
Restrições:
Além de maximizar o retorno, a solução deve:
   2.1 Respeitar um Limite de Risco Tolerado:
        Esse limite é implementado usando a volatilidade (desvio padrão) da carteira, calculada com base na matriz de covariância dos ativos, o que permite capturar a correlação entre eles.
2.2 Soma dos Pesos Igual a 1:
    Como todos os recursos são alocados em ativos, a soma das alocações deve ser igual a 1.
2.3 Limites de Alocação em Cada Ativo:
    Cada peso deve estar entre 0 e 1, pois não queremos alocar mais de 100% do capital em um único ativo, nem permitir posições "short" (vendidas).

3. Método de Otimização
Para resolver o problema de otimização, utilizamos o método de minimização da biblioteca scipy.optimize:
    Função a Ser Minimizada: Como queremos maximizar o retorno esperado da carteira, mas scipy.optimize.minimize minimiza uma função, fazemos a minimização da função negativa do retorno esperado.
Restrições:
    A primeira restrição, {'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1}, garante que a soma dos pesos seja igual a 1.
    A segunda restrição, {'type': 'ineq', 'fun': lambda weights: risk_tolerance - portfolio_volatility(weights, returns)}, assegura que o risco total (volatilidade) da carteira esteja abaixo do limite de risco máximo tolerado.
Limites:
 Utilizamos limites entre 0 e 1 para cada ativo, garantindo que os pesos estejam dentro de um intervalo válido e positivo.

4. Geração da Fronteira Eficiente
Para visualizar as possíveis carteiras que equilibram risco e retorno de maneira ideal, geramos a fronteira eficiente. Variamos o nível de risco tolerado entre diferentes valores (de 0.05 a 0.3, por exemplo) e, para cada limite de risco, recalculamos os pesos ideais. Assim, obtemos a combinação de retorno e risco ideal para cada valor tolerado, criando uma curva que mostra o melhor retorno possível para cada nível de risco.

5. Visualizações da Carteira Otimizada
As visualizações da carteira incluem:
Fronteira Eficiente:
    Mostra a relação entre risco (volatilidade) e retorno esperado para diferentes combinações de risco tolerado.
    A curva representa o "melhor" retorno possível para um dado nível de risco.

Alocação de Ativos:
    Exibe a proporção de cada ativo no portfólio otimizado com base nos pesos resultantes.

Histórico de Desempenho da Carteira:
    Apresenta o retorno acumulado ao longo do tempo, permitindo visualizar como a carteira teria se comportado ao longo do período analisado.

Passo a Passo Completo

Configuração e Coleta de Dados
        Escolha de ativos para a carteira e definição do período de análise.
        Coleta de dados usando yfinance.

Otimização da Carteira
        Maximização do retorno esperado respeitando o limite de risco.

Geração e Visualização dos Gráficos
        Fronteira Eficiente (Risco x Retorno).
        Alocação de Ativos (Distribuição dos Pesos).
        Histórico de Desempenho da Carteira.

Funcionalidades

    Criação de carteiras de investimentos personalizadas
    Cálculo do retorno e do risco dos ativos
    Recomendações de alocação de ativos
    Análise de desempenho da carteira
    Gráficos de desempenho da carteira

Requisitos
    Python 3.8 ou superior
    Bibliotecas necessárias: yfinance, numpy, pandas, scipy, matplotlib, seaborn

Instalação
 Instale as bibliotecas necessárias: 
• numpy` e `pandas` para manipulação de dados;
• `scipy.optimize` ou outros pacotes para resolver o problema de otimização;
• `matplotlib` e `seaborn` para a visualização dos resultados.
• A coleta dos dados de ativos deve ser feita via API do Yahoo Finanças usando a
biblioteca `yfinance`.
• Execute o arquivo main.py para iniciar a ferramenta
Uso

    Crie uma nova carteira de investimentos: python main.py --criar-carteira
    Adicione ativos à carteira: python main.py --adicionar-ativo
    Calcule o retorno e o risco dos ativos: python main.py --calcular-retorno-risco
    Veja as recomendações de alocação de ativos: python main.py --recomendar-alocacao
    Analise o desempenho da carteira: python main.py --analise-desempenho

Gráficos

    Fronteira Eficiente: um gráfico que mostra a relação entre o retorno esperado e o risco dos ativos.
    Alocação de Ativos: um gráfico que mostra a alocação dos ativos na carteira.
    Histórico de Desempenho da Carteira: um gráfico que mostra o desempenho da carteira ao longo do tempo.