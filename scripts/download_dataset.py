import requests
import pandas as pd

#  TODO: Make this into function when working - done!
def get_data():
    try:
        url = "https://github.com/Movemaster12/Real-time-Risk-Intelligence/releases/download/pre-release/creditcard.csv"
        response = requests.get(url)
        # Need to download data to a file
        df = pd.DataFrame(response)
        return df
    except Exception as e:
        print(f"Error occured! {e}")
        # return None


# get_data()

