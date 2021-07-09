class CompoundInterest:

    def get_interest_total(investment):
        total_return = ((investment["principal"]) * (1 + (investment["rate"] / investment["per_year"])) ** (investment["per_year"] * investment["years"]))
    
        return round(total_return, 2)

    def get_interest_total_deposits(investment):
        rate_over_per_year = investment["rate"] / investment["per_year"]
        amount_of_interest = investment["years"] * investment["per_year"]

        total_return = ((investment["principal"]) * (1 + (investment["rate"] / investment["per_year"])) ** (investment["per_year"] * investment["years"])) + ((investment["investment_per_month"] * ((((1 + rate_over_per_year) ** (amount_of_interest)) - 1))) / rate_over_per_year) * (1 + rate_over_per_year)
       
        return round(total_return, 2)




# PMT × {[(1 + r/n)(nt) - 1] / (r/n)}   # PMT × {[(1 + r/n)(nt) - 1] / (r/n)}   # PMT × {[(1 + r/n)(nt) - 1] / (r/n)}   # PMT × {[(1 + r/n)(nt) - 1] / (r/n)}   # PMT × {[(1 + r/n)(nt) - 1] / (r/n)}

# A = the future value of the investment/loan, including interest
# P = the principal investment amount (the initial deposit or loan amount)
# PMT = the monthly payment
# r = the annual interest rate (decimal)
# n = the number of times that interest is compounded per unit t
# t = the time (months, years, etc) the money is invested or borrowed for