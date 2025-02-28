import requests
import json
import os

def get_company_info(company_name, api_key):
    """
    Retrieves business information about a company using a third-party API.

    Args:
        company_name (str): The name of the company.
        api_key (str): Your API key for the data provider.

    Returns:
        dict: A dictionary containing company information, or None if an error occurs.
    """
    api_url = f"YOUR_API_ENDPOINT?company={company_name}&api_key={api_key}"  # Replace with actual API endpoint

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def extract_relevant_info(company_data):
    """
    Extracts relevant business information from the API response.

    Args:
        company_data (dict): The company data returned by the API.

    Returns:
        dict: A dictionary containing extracted information, or None if input data is invalid.
    """
    if not isinstance(company_data, dict):
        return None

    try:
        extracted_info = {
            "name": company_data.get("name"),
            "founding_members": company_data.get("founding_members"),
            "investments": company_data.get("investments"),
            "mergers_acquisitions": company_data.get("mergers_acquisitions"),
            "company_type": company_data.get("company_type"), # public or private
            "location": company_data.get("location"),
            "industry": company_data.get("industry"),
            # Add more fields as needed based on the API response structure
        }
        return extracted_info

    except AttributeError:
        print("Invalid company data structure.")
        return None

def main():
    """
    Main function to demonstrate company information retrieval.
    """

    api_key = os.environ.get("YOUR_API_KEY") #Get API key from environment variables.
    if not api_key:
      print("Error: API key not found. Please set the YOUR_API_KEY environment variable.")
      return

    company_name = input("Enter the company name: ")

    company_data = get_company_info(company_name, api_key)

    if company_data:
        extracted_info = extract_relevant_info(company_data)
        if extracted_info:
            print(json.dumps(extracted_info, indent=4))
        else:
            print("Could not extract relevant information.")
    else:
        print("Failed to retrieve company information.")

if __name__ == "__main__":
    main()