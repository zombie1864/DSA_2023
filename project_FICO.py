from typing import Any, Dict, Union, Tuple

# be my financial planner 

_capital_one_bank = {
    '1st_cd'        : (80000, 0.0415), 
    '2nd_cd'        : (10000, 0.05), 
    'savings_acc'   : (30000, 0.0415)
}


_robinhood = {
    'brokerage_acc': (10000, 0.0465)
}


savings_contr = 4600 + 1400


def interest_pymt_from(acc, view_type:str): 
    '''  '''

    tot_interest_money = 0 

    for acc_val in acc.values(): 
        tot_interest_money += acc_val[0] * acc_val[1]

    tot_interest_money_per_month = round(tot_interest_money / 12, 2)

    if view_type == 'per month': 
        return tot_interest_money_per_month 
    elif view_type == 'per year': 
        return tot_interest_money
    else: 
        print('Not valid view type')



def update_account_balance_4(acc:Dict[str, Tuple], contr_freq:int=1) -> Dict[str, Tuple]:
    # Create a new dictionary with the updated value for 'savings_acc'

    updated_acc = {
        key: ((contr_freq * savings_contr) + balance, rate) 
        if key == 'savings_acc' else 
        (balance, rate) for key, (balance, rate) in acc.items()
    }

    return updated_acc




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
    capital_one_interest_pymt = interest_pymt_from(_capital_one_bank, 'per month')
    robinhood_interest_pymt = interest_pymt_from(_robinhood, 'per month')
    tot_interest_pymt = capital_one_interest_pymt + robinhood_interest_pymt
    print(f'{capital_one_interest_pymt} / month')
    print(f'{robinhood_interest_pymt} / month')
    print(f'Tot: {tot_interest_pymt} / month')
    print(update_account_balance_4(_capital_one_bank, 19))
    print(project(19,'month'))
    print()