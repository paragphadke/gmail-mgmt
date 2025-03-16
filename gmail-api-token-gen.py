import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import json

# Paths
CREDENTIALS_PATH = "/Users/pphadke/Documents/Personal/coding-projects/gmail-mgmt/credentials.json"
TOKEN_PATH = "/Users/pphadke/Documents/Personal/coding-projects/gmail-mgmt/token.json"

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

def authenticate_gmail():
    creds = None

    # If token.json exists, load the credentials
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, "rb") as token_file:
            creds = pickle.load(token_file)

    # If credentials are not valid, reauthenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for future use
       
        with open(TOKEN_PATH, "w") as token_file:
            token_file.write(creds.to_json())

    return creds

# Run authentication and generate token.json
authenticate_gmail()
print(f"✅ Authentication successful! token.json has been created at {TOKEN_PATH}")
