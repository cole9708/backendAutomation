from utilities.configurations import *


def addBookPayload():
    body = {

        "name": "Learn trading Automation with pyrhon",
        "isbn": '234566-34555hhkk',
        "aisle": "22447-123nn2",
        "author": "chris"
    }
    return body


def buildPayLoadFromDB(query):

    addBody = {}
    tp = getQuery(query)
    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody
