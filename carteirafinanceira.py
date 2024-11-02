import numpy as np
import pandas as pd
import yfinance as yf
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações iniciais
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]  # Lista de ativos para análise
start_date = "2020-01-01"  # Data de início para coleta de dados
end_date = "2023-01-01"    # Data final para coleta de dados

# Função para coleta de dados
def get_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    returns = data.pct_change().dropna()
    return returns

# Coletando dados de retorno dos ativos
returns = get_data(tickers, start_date, end_date)

# Funções para cálculo de retorno esperado e risco da carteira
def expected_return(weights, returns):
    return np.sum(weights * returns.mean()) * 252

def portfolio_volatility(weights, returns):
    cov_matrix = returns.cov() * 252
    portfolio_var = np.dot(weights.T, np.dot(cov_matrix, weights))
    return np.sqrt(portfolio_var)

# Função de otimização
def optimize_portfolio(returns, risk_tolerance):
    n = len(returns.columns)
    bounds = tuple((0, 1) for _ in range(n))
    constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1},
                   {'type': 'ineq', 'fun': lambda weights: risk_tolerance - portfolio_volatility(weights, returns)})
    result = minimize(lambda weights: -expected_return(weights, returns),
                      x0=np.ones(n) / n,
                      constraints=constraints,
                      bounds=bounds)
    return result.x, -result.fun

# Obtendo pesos e retorno esperado da carteira otimizada
risk_tolerance = 0.2  # Risco máximo aceitável
optimal_weights, optimal_return = optimize_portfolio(returns, risk_tolerance)

# Exibindo a Fronteira Eficiente
def plot_efficient_frontier(returns):
    risk_levels = np.linspace(0.05, 0.3, 100)
    efficient_portfolios = [optimize_portfolio(returns, risk) for risk in risk_levels]
    risks = [portfolio_volatility(weights, returns) for weights, _ in efficient_portfolios]
    returns_ = [return_ for _, return_ in efficient_portfolios]
    plt.figure(figsize=(10, 6))
    plt.plot(risks, returns_, 'o-', markersize=3, label="Fronteira Eficiente")
    plt.xlabel('Risco (Volatilidade)')
    plt.ylabel('Retorno Esperado')
    plt.title('Fronteira Eficiente')
    plt.legend()
    plt.show()

# Exibindo a Alocação de Ativos
def plot_asset_distribution(weights, tickers):
    plt.figure(figsize=(8, 8))
    plt.pie(weights, labels=tickers, autopct='%1.1f%%')
    plt.title('Distribuição dos Pesos dos Ativos')
    plt.show()

# Exibindo o Desempenho Histórico da Carteira
def plot_return_risk_evolution(returns, weights):
    portfolio_returns = (returns * weights).sum(axis=1)
    cumulative_returns = (1 + portfolio_returns).cumprod() - 1
    plt.figure(figsize=(10, 6))
    plt.plot(cumulative_returns, label='Retorno Acumulado da Carteira')
    plt.xlabel('Data')
    plt.ylabel('Retorno Acumulado')
    plt.title('Evolução do Retorno da Carteira')
    plt.legend()
    plt.show()

# Execução dos gráficos
plot_efficient_frontier(returns)         # Gráfico da Fronteira Eficiente
plot_asset_distribution(optimal_weights, tickers)  # Gráfico de Alocação de Ativos
plot_return_risk_evolution(returns, optimal_weights)  # Histórico de Desempenho da Carteira