import json
# mydict = {
#     "store": {
#         "book": [
#             {"category": "reference",
#              "author": "Nigel Rees",
#              "title": "Sayings of the Century",
#              "price": 8.95
#              },
#             {"category": "fiction",
#              "author": "Evelyn Waugh",
#              "title": "Sword of Honour",
#              "price": 12.99
#              },
#         ],
#     }
# }
# print(type(mydict))
#
# #dict----->json
# json_data = json.dumps(mydict)
# print(json_data)
# print(type(json_data))
#
# #json----->dict
# dict_data = json.loads(json_data)
# print(type(dict_data))

from jsonpath import jsonpath
book_dict = {
    "store": {
        "book": [
            { "category": "reference",
              "author": "Nigel Rees",
              "title": "Sayings of the Century",
              "price": 8.95
              },
            { "category": "fiction",
              "author": "Evelyn Waugh",
              "title": "Sword of Honour",
              "price": 12.99
              },
            { "category": "fiction",
              "author": "Herman Melville",
              "title": "Moby Dick",
              "isbn": "0-553-21311-3",
              "price": 8.99
              },
            { "category": "fiction",
              "author": "J. R. R. Tolkien",
              "title": "The Lord of the Rings",
              "isbn": "0-395-19395-8",
              "price": 22.99
              }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    }
}
# data = jsonpath(book_dict,"$..book[@.length-1]")
# print(data)
# data = jsonpath(book_dict,"$..price")
# print(data)
# data = jsonpath(book_dict,"$.store.bicycle[?(@.color)].price")
# print(data)
data = jsonpath(book_dict,"$.store.bicycle[?(@.title)].book")
print(data)