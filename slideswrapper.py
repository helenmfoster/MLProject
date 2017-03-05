from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from paragraph import Paragraph

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


class SlidesWrapper():
  """Wrapper for Google Slides API"""
  def __init__(self):
    self.credentials = self.get_credentials()
    self.http = self.credentials.authorize(httplib2.Http())
    self.service = discovery.build('slides', 'v1', http=self.http)

  def get_credentials(self):
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """

    # If modifying these scopes, delete your previously saved credentials
    # at ~/.credentials/slides.googleapis.com-python-quickstart.json
    SCOPES = 'https://www.googleapis.com/auth/drive'
    CLIENT_SECRET_FILE = 'client_secret.json'
    APPLICATION_NAME = 'Google Slides API ML Project'

    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
      os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'slides.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
      flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
      flow.user_agent = APPLICATION_NAME
      if flags:
        credentials = tools.run_flow(flow, store, flags)
      else: # Needed only for compatibility with Python 2.6
        credentials = tools.run(flow, store)
      print('Storing credentials to ' + credential_path)
    return credentials

  def create_presentation(self, title):
    """
    Creates a new, blank presentation with given title and returns presentation object
    """
    presentation = {
      'title': title 
    }
    presentation = self.service.presentations().create(body=presentation).execute()
    print('Created presentation with ID: {0}'.format(presentation.get('presentationId')))
    return presentation

  def create_slide(self, index, title):
    pageId = str(index)*5
    titleId = "a-"+pageId
    bodyId = "b-"+pageId

    requests = [
      {
        "createSlide": {
          "objectId": pageId,
          "slideLayoutReference": {
            "predefinedLayout": "TITLE_AND_BODY"
          },
          "placeholderIdMappings": [
            {
              "layoutPlaceholder": {
                "type": "TITLE",
                "index": 0
              },
              "objectId": titleId,
             },
            {
              "layoutPlaceholder": {
                "type": "BODY",
                "index": 0
              },
              "objectId": bodyId,
             },
          ],
        }
      },
      {
        "insertText": {
          "objectId": bodyId,
          "text": "CATS CATS CATS",
        }
      },
{
        "insertText": {
          "objectId": titleId,
          "text": title,
        }
      }
    ]
    return requests

  def add_slides(self, presentation, content):
    requests = []
    for paragraph in content:
      new_slide_request = self.create_slide(paragraph.index, paragraph.title)
      for element in new_slide_request:
        requests.append(element)

    body = {
        'requests': requests
    }
    response = self.service.presentations().batchUpdate(presentationId=presentation.get("presentationId"),
                                                          body=body).execute()
    create_slide_response = response.get('replies')[0].get('createSlide')
    print('Created slide with ID: {0}'.format(create_slide_response.get('objectId')))

if __name__ == '__main__':
  s = SlidesWrapper()
  s.create_presentation("My Test Presentation")
