#functions for data ETL process

def calculate_cost_of_debt(RF, interest_coverage_ratio):
    if interest_coverage_ratio > 8.5:
        # Rating is AAA
        credit_spread = 0.0063
    if (interest_coverage_ratio > 6.5) & (interest_coverage_ratio <= 8.5):
        # Rating is AA
        credit_spread = 0.0078
    if (interest_coverage_ratio > 5.5) & (interest_coverage_ratio <= 6.5):
        # Rating is A+
        credit_spread = 0.0098
    if (interest_coverage_ratio > 4.25) & (interest_coverage_ratio <= 5.49):
        # Rating is A
        credit_spread = 0.0108
    if (interest_coverage_ratio > 3) & (interest_coverage_ratio <= 4.25):
        # Rating is A-
        credit_spread = 0.0122
    if (interest_coverage_ratio > 2.5) & (interest_coverage_ratio <= 3):
        # Rating is BBB
        credit_spread = 0.0156
    if (interest_coverage_ratio > 2.25) & (interest_coverage_ratio <= 2.5):
        # Rating is BB+
        credit_spread = 0.02
    if (interest_coverage_ratio > 2) & (interest_coverage_ratio <= 2.25):
        # Rating is BB
        credit_spread = 0.0240
    if (interest_coverage_ratio > 1.75) & (interest_coverage_ratio <= 2):
        # Rating is B+
        credit_spread = 0.0351
    if (interest_coverage_ratio > 1.5) & (interest_coverage_ratio <= 1.75):
        # Rating is B
        credit_spread = 0.0421
    if (interest_coverage_ratio > 1.25) & (interest_coverage_ratio <= 1.5):
        # Rating is B-
        credit_spread = 0.0515
    if (interest_coverage_ratio > 0.8) & (interest_coverage_ratio <= 1.25):
        # Rating is CCC
        credit_spread = 0.0820
    if (interest_coverage_ratio > 0.65) & (interest_coverage_ratio <= 0.8):
        # Rating is CC
        credit_spread = 0.0864
    if (interest_coverage_ratio > 0.2) & (interest_coverage_ratio <= 0.65):
        # Rating is C
        credit_spread = 0.1134
    if interest_coverage_ratio <= 0.2:
        # Rating is D
        credit_spread = 0.1512

    cost_of_debt = RF + credit_spread
    return cost_of_debt


def forecast_cashflows_and_terminal_value(wacc, perp_growth_rate, cashflows):
    pass
