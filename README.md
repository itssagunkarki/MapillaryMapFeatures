# MapillaryMapFeatures
Using various APIs from mapillary, extract specific features on streets

## Installation
This project uses mapillary API, please follow the instructions provided by Mapillary to get your own API key. [Mapillary API](https://www.mapillary.com/developer)

After getting the API key, create a file named `.env` in the root directory of the project and add the following lines to the file:

    ```bash
        CLINET_ID = <your-client-id>
        CLIENT_TOKEN = <your-client-token>
        CLIENT_SECRET = <your-client-secret>
        AUTH_URL = <your-auth-url>
    ```