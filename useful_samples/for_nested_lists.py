"""
    For with nested lists
"""

nested = [['TSLA', 'MSFT', 'AMZN'],  ['AAPL', 'NVDA']]

# ['TSLA', 'MSFT', 'AMZN', 'AAPL', 'NVDA']
print( [company for companies in nested for company in companies] )


nested = [[['META', 'TSLA'], 'MSFT', 'AMZN'],  ['AAPL', 'NVDA']]

# [[['META', 'TSLA'], 'MSFT', 'AMZN'],  ['AAPL', 'NVDA']]
print( [companies for companies in nested] )

# [[['META', 'TSLA'], 'MSFT', 'AMZN'],  ['AAPL', 'NVDA']]
print( [[company for company in companies] for companies in nested] )

# [['META', 'TSLA'], 'MSFT', 'AMZN', 'AAPL', 'NVDA']
print( [each_company_bloc for companies in nested for each_company_bloc in companies ] )

# ['META', 'TSLA', 'M', 'S', 'F', 'T', 'A', 'M', 'Z', 'N', 'A', 'A', 'P', 'L', 'N', 'V', 'D', 'A']
print( [company for nested_part in nested for company_list in nested_part for company in company_list ] )

# ['AAPL', 'AMZN', 'META', 'MSFT', 'NVDA', 'TSLA']
print(
    sorted(
        [ *set( company if type(company_list) is list else company_list
               for nested_part in nested
               for company_list in nested_part
               for company in company_list)
        ]
    )
)
