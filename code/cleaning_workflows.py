import pandas as pd
import numpy as np

def prepare_dataset(df:pd.DataFrame):
    # Make a copy of the dataset
    df_cleaned = df.copy()

    # Drop columns
    drop_columns = [
    'id',  # Unique identifier 
    'scrape_id',  # Only one unique value, provides no variation
    'last_scraped',  # Only one unique value, not useful for analysis
    'source',  # Only two unique values, not relevant for analysis
    'neighbourhood',  # No clear semantic meaning
    'calendar_updated',  # No clear semantic meaning, all values missing
    'license',  # Mostly missing values, not useful for analysis
    'host_name', # Not useful for analysis 
    'host_thumbnail_url',  # Just a link, not useful for analysis
    'host_picture_url',  # Just a link, not useful for analysis
    'host_url',  # Just a link, not useful for analysis
    'listing_url',  # Just a link, not useful for analysis
    'picture_url',  # Just a link, not useful for analysis
    'bathrooms_text',  # Redundant, `bathrooms` already provides numerical info
    'minimum_minimum_nights',  # Redundant, covered by `minimum_nights`
    'maximum_minimum_nights',  # Redundant, covered by `minimum_nights`
    'minimum_maximum_nights',  # Redundant, covered by `maximum_nights`
    'maximum_maximum_nights',  # Redundant, covered by `maximum_nights`
    'calendar_last_scraped'  # Similar to `last_scraped`, unnecessary
    "calendar_updated", "license"
    ]

    df_cleaned.drop(columns=drop_columns, inplace=True, errors="ignore")

    # Fill missing values for categorical variables
    categorical_fill_values = {
        "name": "Unknown",
        "description": "No description available",
        "neighborhood_overview": "No overview available",
        "host_name": "Unknown",
        "host_location": "Not provided",
        "host_response_time": "No response time",
        "host_is_superhost": "f",
        "has_availability": "f",
        "instant_bookable": "f"
    }
    df_cleaned.fillna(value=categorical_fill_values, inplace=True)

    # Convert date columns
    date_cols = ["host_since", "first_review", "last_review", "calendar_last_scraped"]
    for col in date_cols:
        df_cleaned[col] = pd.to_datetime(df_cleaned[col], errors="coerce")
        df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].mode()[0])

    # Convert percentage columns to numeric
    percentage_cols = ["host_response_rate", "host_acceptance_rate"]
    for col in percentage_cols:
        df_cleaned[col] = df_cleaned[col].str.replace("%", "", regex=True).astype(float) / 100
        df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].median())

    # Convert price column to numeric
    df_cleaned["price"] = df_cleaned["price"].str.replace(r"[\$,]", "", regex=True).astype(float)
    df_cleaned["price"] = df_cleaned["price"].fillna(df_cleaned["price"].median())

    # Fill missing numerical values with median
    numerical_cols = df_cleaned.select_dtypes(include=["number"]).columns.tolist()
    for col in numerical_cols:
        df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].median())

    # Fill missing values in categorical columns with the most common value
    categorical_cols = df_cleaned.select_dtypes(include=['object']).columns
    df_cleaned[categorical_cols] = df_cleaned[categorical_cols].apply(lambda x: x.fillna(x.mode()[0]))

    # Strip leading/trailing spaces from string columns
    df_cleaned = df_cleaned.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    # Convert 't' and 'f' values to boolean (True/False) for binary columns
    binary_columns = ['instant_bookable', 'host_is_superhost', 'host_has_profile_pic', 'host_identity_verified', 'has_availability']
    for col in binary_columns:
        df_cleaned[col] = df_cleaned[col].map({'t': True, 'f': False})
    
    return df_cleaned