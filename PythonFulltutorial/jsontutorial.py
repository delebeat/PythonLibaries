book ={}
book['tom']={
    'name':'tom',
    'address':'1 red street, NY',
    'phone':98888888,
}
book['bob']={
    'name':'bob',
    'address':'1 green street, NY',
    'phone':6565656565,
}

import json
s=json.dumps(book)
# print(s)
print(book['bob'])
print(book['tom'])
# with open("/home/dele/book.txt","w") as f:
#     f.write(s)
# books=json.load(s)
# print(type(books))

