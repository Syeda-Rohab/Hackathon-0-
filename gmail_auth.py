"""
Gmail Authentication Setup for AI Employee Foundation
This script handles OAuth 2.0 authentication for Gmail API access
"""

import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scopes required for reading Gmail
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    """
    Authenticate and return Gmail service object
    """
    creds = None
    
    # Token file stores the user's access and refresh tokens
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # If there are no valid credentials, request authorization
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # You'll need to download credentials.json from Google Cloud Console
            if not os.path.exists('credentials.json'):
                print("Error: credentials.json not found!")
                print("Please download it from Google Cloud Console:")
                print("1. Go to https://console.cloud.google.com/")
                print("2. Create a new project or select existing one")
                print("3. Enable Gmail API")
                print("4. Create credentials for Desktop Application")
                print("5. Download the JSON file as 'credentials.json'")
                return None
            
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save credentials for next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    # Build and return the Gmail service
    service = build('gmail', 'v1', credentials=creds)
    return service

if __name__ == "__main__":
    service = authenticate_gmail()
    if service:
        print("Gmail authentication successful!")
        # Test the connection by getting profile info
        profile = service.users().getProfile(userId='me').execute()
        print(f"Authenticated as: {profile['emailAddress']}")
    else:
        print("Authentication failed!")