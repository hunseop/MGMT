# device.py
import pandas as pd
import logging
from features.logging_config import setup_logging


# Preliminary setting
setup_logging() # Log format setting
pd.set_option('display.max_rows', None) # Set pandas options to display all rows

def handle_device_command(args):
    try:
        logging.info("Read the Device file.")
        df = pd.read_excel('./devices.xlsx')
    except:
        logging.debug("Please check the 'devices.xlsx' file.")
        exit()

    if not args.query:
        print(df)
    else:
        # Define the substring you are looking for
        substring = args.query

        # Use a lambda function to filter the DataFrame, converting everything to lower case for the comparison
        filtered_df = df[df.apply(lambda row: row.astype(str).str.lower().str.contains(substring).any(), axis=1)]

        # Print the filtered DataFrame
        if filtered_df.empty:
            print("No results were found for your search.")
        else:
            print(filtered_df)
            