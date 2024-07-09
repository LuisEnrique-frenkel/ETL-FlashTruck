import fs
from fs.osfs import OSFS
from fs.subfs import SubFS
import pandas as pd 
import sqlite3 as db

def mkdir(fs_object: OSFS, path: str) -> SubFS:
    """Ensure the directory exists; create it if it doesn't.
    
    Args:
    - fs (OSFS): An OSFS object representing the file system.
    
    Returns:
    - OSFS: The OSFS object representing the file system.
    """
    return fs_object.makedir(path) if not fs_object.exists(path) else fs_object.opendir(path)

def get_fulldf(SubFS: SubFS) -> pd.DataFrame:
    """
    Connects to databases and concatenate information into a DataFrame.
    
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