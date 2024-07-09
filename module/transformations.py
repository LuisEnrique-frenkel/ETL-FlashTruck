import pandas as pd

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