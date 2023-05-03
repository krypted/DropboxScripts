import requests

# Get your Dropbox API key from https://www.dropbox.com/developers/apps
API_KEY = "YOUR_API_KEY"

# Set the path to the folder you want to list files in
FOLDER_PATH = "/My Documents"

# Make a request to the Dropbox API to list the files in the specified folder
response = requests.get("https://api.dropboxapi.com/2/files/list_folder",
                         params={"path": FOLDER_PATH},
                         headers={"Authorization": "Bearer " + API_KEY})

# Check the response status code
if response.status_code == 200:
    # The request was successful, so parse the response body
    files = response.json()["entries"]

    # Print the list of files
    for file in files:
        print(file["name"])
else:
    # The request failed, so print the error message
    print(response.status_code, response.reason)
