import requests

"""
Shows Changes for a given file using the https://api.dropboxapi.com/2/files/history endpoint
"""

# Get your Dropbox API key from https://www.dropbox.com/developers/apps
API_KEY = "YOUR_API_KEY"

# Set the path to the file you want to get the history of changes for
FILE_PATH = "/My Documents/my_file.txt"

# Make a request to the Dropbox API to get the history of changes for the specified file
response = requests.get("https://api.dropboxapi.com/2/files/history",
                         params={"path": FILE_PATH},
                         headers={"Authorization": "Bearer " + API_KEY})

# Check the response status code
if response.status_code == 200:
    # The request was successful, so parse the response body
    changes = response.json()["entries"]

    # Print the history of changes
    for change in changes:
        print(change["rev"], change["type"], change["timestamp"])
else:
    # The request failed, so print the error message
    print(response.status_code, response.reason)
