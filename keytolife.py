import datetime
import json

treez = [
    [
        {
            "data": {
                "parent_thread": 1,
                "user": 1,
                "created": datetime.datetime(
                    2022, 5, 26, 21, 32, 34, 85891, tzinfo=datetime.timezone.utc
                ),
                "text": "lklkhj",
                "likes": 0,
                "dislikes": 0,
            },
            "id": 8,
            "children": [
                {
                    "data": {
                        "parent_thread": 1,
                        "user": 1,
                        "created": datetime.datetime(
                            2022,
                            5,
                            29,
                            16,
                            35,
                            44,
                            277801,
                            tzinfo=datetime.timezone.utc,
                        ),
                        "text": "i don't think so\r\n",
                        "likes": 0,
                        "dislikes": 0,
                    },
                    "id": 51,
                    "children": [
                        {
                            "data": {
                                "parent_thread": 1,
                                "user": 1,
                                "created": datetime.datetime(
                                    2022,
                                    5,
                                    29,
                                    16,
                                    38,
                                    38,
                                    868647,
                                    tzinfo=datetime.timezone.utc,
                                ),
                                "text": "another one\r\n",
                                "likes": 0,
                                "dislikes": 0,
                            },
                            "id": 52,
                        }
                    ],
                }
            ],
        }
    ],
    [
        {
            "data": {
                "parent_thread": 1,
                "user": 1,
                "created": datetime.datetime(
                    2022, 5, 29, 16, 35, 33, 606410, tzinfo=datetime.timezone.utc
                ),
                "text": "okay dokey smokey",
                "likes": 0,
                "dislikes": 0,
            },
            "id": 50,
        }
    ],
    [
        {
            "data": {
                "parent_thread": 1,
                "user": 1,
                "created": datetime.datetime(
                    2022, 5, 29, 16, 35, 44, 277801, tzinfo=datetime.timezone.utc
                ),
                "text": "i don't think so\r\n",
                "likes": 0,
                "dislikes": 0,
            },
            "id": 51,
            "children": [
                {
                    "data": {
                        "parent_thread": 1,
                        "user": 1,
                        "created": datetime.datetime(
                            2022,
                            5,
                            29,
                            16,
                            38,
                            38,
                            868647,
                            tzinfo=datetime.timezone.utc,
                        ),
                        "text": "another one\r\n",
                        "likes": 0,
                        "dislikes": 0,
                    },
                    "id": 52,
                }
            ],
        }
    ],
    [
        {
            "data": {
                "parent_thread": 1,
                "user": 1,
                "created": datetime.datetime(
                    2022, 5, 29, 16, 38, 38, 868647, tzinfo=datetime.timezone.utc
                ),
                "text": "another one\r\n",
                "likes": 0,
                "dislikes": 0,
            },
            "id": 52,
        }
    ],
]

# for branch in treez:
#     for each in branch:
#         try:
#             x = bool(branch[0]["children"])
#             if x == True:
#                 print(x)
#         except KeyError:

#             print(each)


seen = set()
temp = []
for d in treez:
    for each in d:

        t = tuple(each)
        if t not in seen:
            seen.add(t)
            temp.append(each)

print(temp)
