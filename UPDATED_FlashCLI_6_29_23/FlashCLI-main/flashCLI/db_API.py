''' this file is for the COMM w db, containing the data exhange mechanism logic  
data container/ data model used to allow sending and retrieve data from db_dir 
this file will also contain a `DatabaseHandler` to read and write data to the db. 
'''

import os
import json 
from pathlib import Path 
from typing import Dict, Tuple, NamedTuple, List
from flashCLI import SUCC_CODE_0, DB_READ_ERR_CODE_3, DB_WRITE_ERR_CODE_4, JSON_ERR_CODE_5, DB_DIR_PATH

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
            file_path:Path = DB_DIR_PATH / f"{db_name}_keywords_db.json"
            file_path.write_text("{}")
            return SUCC_CODE_0
        except OSError:
            return DB_WRITE_ERR_CODE_4


class DBResponse(NamedTuple):
    ''' data model/ data container for flashcards dataset this class is for COMM w DB inherits from NamedTuple 
    i.e. DSReponse is a subclass of typing.NamedTuple. subclassing from NamedTuple allows to create named tuples 
    with type hints for their field names 
    '''
    dataset: Dict[int,Tuple[str]]
    COMM_CODE: int 



class KWDBResponse(NamedTuple): 
    '''  '''
    dataset: List[str]
    COMM_CODE: int 



class DBHandler:
    ''' data model for reading and writing data to the db using json module from STD_Lib '''
    def __init__(self, file_path:Path) -> None:
        ''' inst:DBHandler contain path to the db as ATTR'''
        self._db_file_path = file_path



    def read_flashcard_dataset(self, type:str='flashcards') -> DBResponse:
        ''' reads data from db and deserializes it returns inst of class DSResponse '''
        try:
            with self._db_file_path.open('r') as db:
                try:
                    if type == 'flashcards': 
                        return DBResponse(json.load(db), SUCC_CODE_0)
                    else: 
                        return KWDBResponse(json.load(db), SUCC_CODE_0) 
                except json.JSONDecodeError: # catches wrong json file format 
                    if type == 'flashcards': 
                        return DBResponse({}, JSON_ERR_CODE_5) 
                    else: 
                        return KWDBResponse([], JSON_ERR_CODE_5)
        except OSError: #catches file IO ERR
            if type == 'flashcards': 
                return DBResponse({}, DB_READ_ERR_CODE_3)
            else: 
                return KWDBResponse([], DB_READ_ERR_CODE_3)
        


    def write_flashcard_dataset(self, dataset:Dict[int, Tuple[str]], type='flashcards') -> DBResponse:
        '''  data taken from CLI, added to dataset, and writes to db updated dataset'''
        try:
            with self._db_file_path.open('w') as db:
                json.dump(dataset, db, indent=4)

                if type == 'flashcards': 
                    return DBResponse(dataset, SUCC_CODE_0) 
                else: 
                    return KWDBResponse(dataset, SUCC_CODE_0)
        except OSError:
            if type == 'flashcards': 
                return DBResponse(dataset, DB_WRITE_ERR_CODE_4)
            else: 
                return KWDBResponse(dataset, DB_WRITE_ERR_CODE_4)



    def delete_flashcard_dataset(self) -> DBResponse:
        '''  '''
        try:
            os.remove(self._db_file_path)
            return DBResponse({}, SUCC_CODE_0)
        except OSError:
            return DBResponse({}, DB_READ_ERR_CODE_3)