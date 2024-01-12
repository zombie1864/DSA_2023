''' this file deals w creating a dir and database json files
'''
from flashCLI import SUCC_CODE_0, FILE_ERR_CODE_2, DB_DIR_PATH


def init_app(db_name:str) -> int:
    """Initialize the application""" 
    database_code = _create_database(db_name)

    if database_code != SUCC_CODE_0:
        return database_code
    
    return SUCC_CODE_0


def _create_database(db_name:str, type='flash_cards') -> int:
    '''  '''
    if type == 'flash_cards': 
        try:
            DB_DIR_PATH.mkdir(exist_ok=True)
            DB_DIR_PATH.joinpath(f'{db_name}_flashcards_db.json').touch(exist_ok=False)
        except OSError:
            return FILE_ERR_CODE_2
    else: 
        try: 
            DB_DIR_PATH.mkdir(exist_ok=True)
            DB_DIR_PATH.joinpath(f'{db_name}_keywords_db.json').touch(exist_ok=False)
        except OSError:
            return FILE_ERR_CODE_2
        
    return SUCC_CODE_0


def init_kws_list(db_name:str) -> int: 
    '''  '''
    database_code = _create_database(db_name, 'keywords')

    if database_code != SUCC_CODE_0: 
        return database_code 
    
    return SUCC_CODE_0 
