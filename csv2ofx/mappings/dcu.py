from operator import itemgetter

mapping = {
    "has_header": True,
    "is_split": False,
    "account": "",
    "bank": "Bank",
    "currency": "USD",
    "delimiter": ",",
    "date": itemgetter("DATE"),
    "amount": itemgetter("AMOUNT"),
    "desc": itemgetter("DESCRIPTION"),
    "payee": itemgetter("DESCRIPTION"),
    "notes": "",
    "check_num": "",
    "id": ""
}
