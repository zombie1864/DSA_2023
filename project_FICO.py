from typing import Any, Dict, Union, Tuple
''' 
5 yr CD rates  
BMO: 4.50 
FIB: 4.59
C1
'''


_capital_one_bank = {
    '1st_cd'        : (80000, 0.0415), 
    '2nd_cd'        : (10000, 0.05), 
    'savings_acc'   : (30000, 0.0415) # rate changes over time
}
_robinhood = {
    'brokerage_acc': (10000, 0.0465) # rate changes over time
}
_jeff__tot_contr = 1700 
_tiff__tot_contr = 4600 
_tot_contr = _jeff__tot_contr + _tiff__tot_contr 
_monthly_payout = 1500 



def interest_pymt_from(acc:Dict[str, Tuple], view_type:str) -> Union[float, int, str]: 
    '''  Calc the tot interest pymt from an acc 
        Returns the interest pymt amt either per month or per year 
    '''

    tot_interest_money:Union[float, int] = 0 

    for balance in acc.values(): # acc:Dict[str, Tuple]
        acc_val:Union[float, int]       = balance[0]
        interest_rate:Union[float, int] = balance[1]

        tot_interest_money += acc_val * interest_rate

    tot_interest_money_per_month:Union[float, int] = round(tot_interest_money / 12, 2)

    if view_type == 'per month': 
        return tot_interest_money_per_month 
    elif view_type == 'per year': 
        return tot_interest_money
    else: 
        return 'Not valid view type'



def interest_calculator(principle:Union[float, int], rate:float, time:int): 
    ''' 
    formula used to calculate interest: A = P(1 + r/n)^(nt) 
    A = the total amount (including both the principal and interest)
    P = the principal amount (initial deposit) = $44,000
    r = the annual interest rate (expressed as a decimal) = 4.1% = 0.041
    n = the number of times interest is compounded per year (typically, CDs are compounded annually, so n = 1)
    t = the number of years the money is invested for = 5 years
    '''
    return round(principle * pow((1 + (rate)), time) - principle, 2)



def update_account_balance_4(acc:Dict[str, Tuple], contr_freq:int=1) -> Dict[str, Tuple]:
    ''' Create a new dictionary with the updated value for 'savings_acc' '''

    updated_acc:Dict[str, Tuple] = {
        key : ((contr_freq * _tot_contr) + acc_val, rate) 
        if key == 'savings_acc' else 
        (acc_val, rate) for key, (acc_val, rate) in acc.items()
    }

    return updated_acc # returns an updated acc 




def project(time:Union[float, int], unit:str) -> Union[int, float]: 
    '''  '''
    if unit == 'month': 
        updated_capital_one_bank = update_account_balance_4(_capital_one_bank, time)
        updated_robinhood_acc = update_account_balance_4(_robinhood, time)


        projected_capital_one_interest_pymt = interest_pymt_from(updated_capital_one_bank, 'per month')
        projected_robinhood_interest_pymt = interest_pymt_from(updated_robinhood_acc, 'per month')

        tot_project_interest_pymt = projected_capital_one_interest_pymt + projected_robinhood_interest_pymt

        return tot_project_interest_pymt




if __name__ == '__main__':
    print()
    print('--Current Monthly Earnings--')
    capital_one_interest_pymt   = interest_pymt_from(_capital_one_bank, 'per month')
    robinhood_interest_pymt     = interest_pymt_from(_robinhood, 'per month')
    tot_interest_pymt           = round(capital_one_interest_pymt + robinhood_interest_pymt, 2)
    capital_one_msg             = f'Capital one payment: \t{capital_one_interest_pymt}'
    robinhood_msg               = f'Robinhood payment: \t{robinhood_interest_pymt}'
    tot_pyment_msg              = f'\nTotal payment: \t\t{tot_interest_pymt}\n'
    print(capital_one_msg)
    print(robinhood_msg)
    print(tot_pyment_msg)
    # print(update_account_balance_4(_capital_one_bank, 67))
    # print(project(67,'month'))
    print(f'Amt need to pay: {_monthly_payout - tot_interest_pymt} \nLeft over: {round(1700 - _monthly_payout + tot_interest_pymt, 2)}') 
    _amt = 44000
    _time = 5
    _month = 60 
    _rate = 0.046
    print(f'Interest pymt earned in {_time} year {interest_calculator(_amt, _rate, _time)}')
    print(f'Monthly interest payment {round(interest_calculator(_amt, _rate, _time) / _month, 2)}')
