from monitor_meteorologico_ve.openmeteo import OpenMeteoAPIClient


def test_get_historical_data():
    api_client = OpenMeteoAPIClient()
    lat = 8.80
    lon = -70.86
    start_date = "2025-06-20"
    end_date = "2025-06-30"
    data = api_client.get_historical_data(lat, lon, start_date, end_date)
    assert data
    