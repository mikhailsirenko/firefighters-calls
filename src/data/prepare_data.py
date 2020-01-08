import pandas as pd
import geopandas
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
	
def select_ny(df, year, delta=1):
    """Select New Year's Eve period of a specific year
    
    Args:
        df (DataFrame) : Complete data set (not sliced by date)
        year (int) : Year of interest
        delta (int) : How many days +- take into account
    
    Returns:
        df (DataFrame) : A subset of a specific year and delta
    """
    begin = pd.to_datetime(str(year-1) + "-12-" + str(31 - delta))
    end = pd.to_datetime(str(year) + "-01-" + str(1 + delta))
    
    df = data[data["pmeTimeStamp"] > begin]
    df = df[df["pmeTimeStamp"] < end]

    print(f"The number of firefigthers calls made from {begin} to {end} : {df.shape[0]}")
    
    return df