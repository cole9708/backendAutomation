import json
import configparser
from payLoad import *
from utilities.resources import *
from utilities.configurations import *

import requests

url = getConfig()['API']['endpoint'] + ApiResources.addBook
del_url = getConfig()['API']['endpoint'] + ApiResources.deleteBook
headers = {"Content-Type": "application/json"}
query = 'select * from Books'
addBook_response = requests.post(url,json=addBookPayload(),headers=headers, )
print(addBook_response.json())
assert addBook_response.json()['Msg'] =='successfully added'
response_json = addBook_response.json()
print(type(response_json))

bookId = response_json['ID']
print(f'my book id is : {bookId}')
# Delete Book -
response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={

    "ID": bookId
}
                                    )
print(response_deleteBook.status_code)


