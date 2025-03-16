from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# Replace with the actual full path of token.json
TOKEN_PATH = "/Users/pphadke/Documents/Personal/coding-projects/gmail-mgmt/token.json"

creds = Credentials.from_authorized_user_file(TOKEN_PATH)
service = build("gmail", "v1", credentials=creds)

# Example: Fetch unread emails
results = service.users().messages().list(userId="me", labelIds=["INBOX"], q="is:unread").execute()
messages = results.get("messages", [])
print(f"Number of unread emails: {len(messages)}")

#for msg in messages:
 #   msg_detail = service.users().messages().get(userId="me", id=msg["id"]).execute()
  #  print(msg_detail["snippet"])  # Print email snippet
