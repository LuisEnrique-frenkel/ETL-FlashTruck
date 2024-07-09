from fs.osfs import OSFS
from fs.subfs import SubFS
import sqlite3 as db
import pandas as pd
import fs

def get_fulldf(SubFS: SubFS) -> pd.DataFrame:
    """
    Connects to SQLite databases and concatenate information into a DataFrame.
    
    Parameters:
    SubFS (SubFS): Object representing file system operations.
    
    Returns:
    pd.DataFrame: DataFrame containing concatenate information from databases.
    """
    df = pd.DataFrame()  # DataFrame para almacenar los datos combinados
    
    try:
        for index, path in enumerate(SubFS.walk.files()):
            # Create connection to the DB
            conn = db.connect(SubFS.getsyspath(path))
            
            # Read data from the database
            query = 'SELECT * FROM LoggedProcessValue;'
            data = pd.read_sql_query(query, conn)
            
            # Concatenate the data to df
            df = pd.concat([df, data], ignore_index=True)
            
            # Close the connection
            conn.close()
            
    except Exception as e:
        print(f"Error processing database at {path}: {str(e)}")
    
    return df

def get_full_steam(path_LoggingTag: str, path_TLG: str, TLG: int) -> pd.DataFrame:
    """ Get join from logging tag and the data frame values 
    Args:
    - path_LoggingTag: Path for the LoggingTag csv file
    - path_TLG: Path for the TLG csv file
    - TLG: The number of the TLG
    
    Returns:
    - df: df of the inner join
    """
    df_LoggingTag = pd.read_csv(path_LoggingTag)
    df_LoggingTag = df_LoggingTag[["pk_Key", "tag_name", "fk_LogId", "DataType"]]
    df_TLG = pd.read_csv(path_TLG)
    return pd.merge(df_TLG, df_LoggingTag[df_LoggingTag['fk_LogId'] == TLG], 
                        left_on='pk_fk_Id', right_on='pk_Key', how='inner')