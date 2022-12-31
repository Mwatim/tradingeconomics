import logging
import pandas as pd
import time
import tradingeconomics as te
te.login() 
# authentication without which there will be a LoginError 
# raise LoginError('You need to do login before making any request')
# tradingeconomics.indicators.LoginError: You need to do login before making any request

def get_mexico_demo():
    """
    Extracts Mexico GDP Data from Trading Economics API and returns a DataFrame
    """
    try:
        logging.debug("Attempting to Connect to te")
        mexico_data = te.getIndicatorData(country='mexico', indicators='gdp')
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        print("Ran Into a urlopen error:", e)
    else:
        time.sleep(60)
        # Allow 60 seconds for reconnection
    finally:
        mexico_data = te.getIndicatorData(country='mexico', indicators='gdp')     
    return pd.DataFrame.from_records(mexico_data)

def get_kenya_uganda_trade():
    """
    Extracts detailed information about a Comtrade country
    """
    try:
        kenya_uganda_trade = te.getCmtCountryFilterByType(country1='Kenya', country2='Uganda', type='import', output_type='df')
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        print("Ran Into a urlopen error:", e)
    else:
        # Allow 60 seconds for reconnection
        time.sleep(60)
    finally:
        kenya_uganda_trade = te.getCmtCountryFilterByType(country1='Kenya', country2='Uganda', type='import', output_type='df')
    return kenya_uganda_trade

