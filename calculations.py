def calculate_npv(initial_investment, cash_flows, discount_rate):
    npv = -initial_investment
    for i, cash_flow in enumerate(cash_flows):
        npv += cash_flow / ((1 + discount_rate) ** (i + 1))
    return npv


def calculate_payback_period(initial_investment, cash_flows):
    cumulative_cash_flow = 0
    for i, cash_flow in enumerate(cash_flows):
        cumulative_cash_flow += cash_flow
        if cumulative_cash_flow >= initial_investment:
            return i + 1
    return None
