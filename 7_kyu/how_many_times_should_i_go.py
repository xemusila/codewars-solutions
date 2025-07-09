def how_many_times(annual_price, individual_price):
    return annual_price // individual_price + (annual_price % individual_price != 0)