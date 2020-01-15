import pandas as pd
import geopandas as gpd
import numpy as np
def prepare_gdf(data):
    """
    Prepare data and convert it to GeoDataFrame
    
    Args:
        data (DataFrame) : Initial raw data set
        
    Returns:
        gdf (GeoDataFrame) : Data set with cleaned and converted coordinates
    
    """
    # Clean the coordinates
    data['pmeLatitude'] = data['pmeLatitude'].replace(to_replace='\\N', value=np.nan)
    data['pmeLongitude'] = data['pmeLongitude'].replace(to_replace='\\N', value=np.nan)

    data['pmeLatitude'] = data['pmeLatitude'].dropna()
    data['pmeLongitude'] = data['pmeLongitude'].dropna()

    data["pmeLatitude"] = data["pmeLatitude"].astype(float)
    data["pmeLongitude"] = data["pmeLongitude"].astype(float)

    # Create a GeoDataFrame
    gdf = gpd.GeoDataFrame(
        data, geometry=gpd.points_from_xy(data["pmeLongitude"], data["pmeLatitude"])
    )

    gdf.crs = {"init": "epsg:4326"}

    print(f"Total number of records collected with assigned coordinates : {gdf.shape[0]}")
    
    return gdf

def select_ny(data, year, delta=1):
    """
    Select New Year's Eve period of a specific year
    
    Args:
        data (DataFrame or GeoDataFrame) : Complete data set (not sliced by date)
        year (int) : Year of interest
        delta (int) : How many days +- take into account
    
    Returns:
        result (DataFrame or GeoDataFrame) : A subset of a specific year and delta
    """
    if year == 2017:
        begin = pd.to_datetime("2017-01-01")
        end = pd.to_datetime("2017-01-" + str(delta))
        
    else:
        begin = pd.to_datetime(str(year-1) + "-12-" + str(31 - delta + 1))
        end = pd.to_datetime(str(year) + "-01-" + str(1 + delta))
    
    result = data[data["pmeTimeStamp"] > begin]
    result = result[result["pmeTimeStamp"] < end]

    print(f"The number of firefigthers calls made from {begin} to {end} : {result.shape[0]}")
    
    return result

def extract_categories(data, year, categories):
    ny = select_ny(data, year)
    j = []
    l = []
    for index, row in ny['pmeStrippedMessage'].iteritems():
        for category in categories:
            if category in row:
                j.append(index)
                l.append(category)
                break
    result = ny.loc[j,:]
    result['pmeCategory'] = l
    return result