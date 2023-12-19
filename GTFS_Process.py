# Install packages
import pandas as pd
import requests
import zipfile
import io

#pull GTFS
gtfs_path = 'https://www.itsmarta.com/google_transit_feed/google_transit.zip'

# Create functions to access GTFS and store files in memory
def load_gtfs_data(
        url,
        files = [
            'stops.txt', 'routes.txt', 'trips.txt', 'stop_times.txt',
            'calendar.txt', 'calendar_dates.txt', 'shapes.txt'
        ]):
    """
    Load GTFS data from a URL and convert each required .txt file into a pandas DataFrame, all in memory.
    """
    response = requests.get('https://www.itsmarta.com/google_transit_feed/google_transit.zip')
    zip_file = zipfile.ZipFile(io.BytesIO(response.content))

    # Define the required GTFS files
    required_files = files

    # Load each file into a DataFrame
    dataframes = {}
    for file in required_files:
        try:
            with zip_file.open(file) as f:
                df = pd.read_csv(f)
                dataframes[file] = df
        except KeyError:
            print(f"{file} not found in the GTFS feed.")

    return dataframes

feed = load_gtfs_data(gtfs_path)
x = 5