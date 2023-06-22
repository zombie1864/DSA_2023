# on __main__.py 
#==========================[NOTE new feature: START]==========================#


@main.command()
@click.argument('db_name') 
def initkws4(db_name) -> None: 
    '''  '''
    code_res = config.init_kws_list(db_name)

    if code_res == SUCC_CODE_0: 
        db_API.init_database(db_name, 'keywords') 
        click.echo(click.style("\n[Success]:", fg="bright_green") + ': Database created\n')
    elif code_res == 2: 
        click.echo(click.style("\n[Error]", fg="red") + f': Database for {db_name} already created\n')



@main.command()
@click.argument('db_name')
def supplykw(db_name) -> None: 
    ''' Provide keywords that will be used in conjunction with the cmd `teach` '''


@main.command()
@click.argument('db_name')
def teach(db_name) -> None: 
    ''' Prompts user to teach '''


#==========================[NOTE new feature: END]==========================#

# on utils.py 
#==========================[NOTE new feature: START]==========================#
    def add_kws(self, kws:str):
        '''  '''
        keywords = [] 

        for word in kws.split(' '): 
            keywords.append(word) #puts words into keywords list 

# config.py 
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


# db_API.py 

def init_database(db_name:str, type='flash_cards') -> int:
    '''  '''
    if type == 'flash_cards': 
        try: 
            file_path:Path = DB_DIR_PATH / f"{db_name}_flashcards_db.json"
            file_path.write_text("{}")
            return SUCC_CODE_0
        except OSError:
            return DB_WRITE_ERR_CODE_4
    else: 
        try: 
            file_path:Path = DB_DIR_PATH / f"{db_name}_flashcards_db.json"
            file_path.write_text("[]")
            return SUCC_CODE_0
        except OSError:
            return DB_WRITE_ERR_CODE_4