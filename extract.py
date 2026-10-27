
import requests

def extract_data():
    url = "https://www.fema.gov/api/open/v2/PublicAssistanceFundedProjectsDetails"

    print("Fetching FEMA data...")

    try:
        api_data = requests.get(url, timeout=30)
        api_data.raise_for_status()

        records = api_data.json().get(
            "PublicAssistanceFundedProjectsDetails", []
        )

        print(f"Records fetched: {len(records)}")
        return records

    except requests.RequestException as error:
        print(f"API request failed: {error}")
        return []
    except ValueError as error:
        print(f"Invalid JSON response: {error}")
        return []

