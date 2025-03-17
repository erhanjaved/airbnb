import pandas as pd
import numpy as np

# def prepare_dataset(df: pd.DataFrame)-> pd.DataFrame:
#     rename_map = {'neighbourhood group':{
#         'brookln': 'Brooklyn',
#         'manhatan': 'Manhattan'}}
    
#     clean_and_convert_to_int_columns = ['service fee', 'price']    

#     df = rename_values(df, rename_map)
    
#     df = clean_float_fields(df, clean_and_convert_to_int_columns)
    
#     df = change_dtype_to_int(df)

#     df = impute_values(df)
    
#     return df


# def rename_values(df:pd.DataFrame, column_value_map = dict) -> pd.DataFrame:
#     for column, values in column_value_map.items():
#         if (column not in df.columns):
#             raise Exception(f"{column}: column not found ")
        
#         df[column] = df[column].replace(values)
    
    
#     return df

# def clean_float_fields(df: pd.DataFrame, columns: list) -> pd.DataFrame:
#     """
#     clean pd.DataFrame columns by getting rid of special characters and white space and convert
#     {dtype: string, pd.Series} to {dtype: float, pd.Series}
#     """
#     for column in columns:
#         df[column] = df[column].astype(str).str.replace(r"[^0-9.]", "", regex=True
#                                                         ).str.strip().replace("", "-1"
#                                                                             ).to_numeric()
#     return df

# def change_dtype_to_int(df: pd.DataFrame) -> pd.DataFrame:
#     df["minimum nights"] = np.array(df["minimum nights"], dtype = np.int16)
#     df["number of reviews"] = np.array(df["number of reviews"], dtype = np.int16)
#     df["review rate number"] = np.array(df["review rate number"], dtype=np.int8)
    
#     return df

# def impute_values(df: pd.DataFrame)-> pd.DataFrame:
#     df[df.select_dtypes(include=['int64', 'float64']).columns] = df.select_dtypes(include=['int64', 'float64']).fillna(-1)
#     df['last review'] = df['last review'].fillna(pd.Timestamp("2099-01-01"))
#     df[df.select_dtypes(include=['object']).columns] = df.select_dtypes(include=['object']).fillna("Unknown")

#     return df


def drop_columns(df: pd.DataFrame)-> pd.DataFrame:
    df = df.drop(columns=['listing_url', 'scrape_id', 'last_scraped', 'source', 'picture_url', 'host_url', 'host_about', 'host_thumbnail_url', 'host_picture_url', 'host_has_profile_pic', 'neighbourhood', 'bathrooms_text', 'calendar_last_scraped', 'license'])
    return df

def columns_to_numeric(df:pd.DataFrame) -> pd.DataFrame:
    
    return df