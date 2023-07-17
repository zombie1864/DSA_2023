# be my financial planner 

capital_one_bank = {
    '1st_cd'        : (80000, 0.0415), 
    '2nd_cd'        : (10000, 0.05), 
    'savings_acc'   : (30000, 0.0415)
}


robinhood = {
    'brokerage_acc': (10000, 0.0465)
}


def curr_assets(view_type): 
    '''  '''

    tot_interest_money = 0 

    for acc_val in capital_one_bank.values(): 
        tot_interest_money += acc_val[0] * acc_val[1]

    for acc_val in robinhood.values(): 
        tot_interest_money += acc_val[0] * acc_val[1]

    tot_interest_money_per_month = round(tot_interest_money / 12, 2)

    if view_type == 'per month': 
        print(f'{tot_interest_money_per_month} / month') 
        return tot_interest_money_per_month 
    elif view_type == 'per year': 
        print(f'{tot_interest_money} / year')
        return tot_interest_money
    else: 
        print('Not valid view type')




if __name__ == '__main__':
    print()
    curr_assets('per month')
    print()