import requests
import os

def test_downloading_one_image():
    # Define your client token
    client_token = os.getenv("CLIENT_TOKEN")

    # Define the image ID you want to retrieve information for
    image_id = "550092599700936"

    # Define the endpoint URL
    endpoint_url = f"https://graph.mapillary.com/{image_id}"

    # Define the headers with the client token
    params = {
        "fields": "id,computed_geometry,detections.value",
    }

    headers = {
            "Authorization": f"Bearer {client_token}",
    }

    # Make the GET request to retrieve information about the image
    response = requests.get(endpoint_url, params=params, headers=headers)


    # Check if the request was successful
    assert (response.status_code == 200) and (response.json()["id"] == image_id)