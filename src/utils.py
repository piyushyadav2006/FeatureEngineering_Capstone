import pandas as pd

def build_business_features(df):
   
    # Make a safe copy so we don't alter the original data
    df_out = df.copy()
    
    # Calculate business metrics
    df_out['total_nights'] = df_out['stays_in_weekend_nights'] + df_out['stays_in_week_nights']
    df_out['total_guests'] = df_out['adults'] + df_out['children'] + df_out['babies']
    
    # +1 prevents dividing by zero!
    df_out['price_per_person'] = df_out['adr'] / (df_out['total_guests'] + 1)
    df_out['special_requests_rate'] = df_out['total_of_special_requests'] / (df_out['total_nights'] + 1)
    
    # Family flag (1 if kids/babies are present, 0 if not)
    df_out['is_family'] = (df_out['children'] + df_out['babies'] > 0).astype(int)
    df_out['total_revenue'] = df_out['adr'] * df_out['total_nights']
    
    return df_out