class Contact():
    def __init__(self, id, address, correspondence_address, email, phones) -> None:
        self.id = id
        self.address = address
        self.correscpondence_address = correspondence_address
        self.email = email
        self.phones = phones


class Partner():
    def __init__(self, id, url, title) -> None:
        self.id = id
        self.url = url
        self.title = title


import datetime


class Post():
    def __init__(self, id, url, title, title_arabian, subtitle, subtitle_arabian, tag, tag_arabian,
                 updated=None) -> None:
        self.id = id
        self.url = url
        self.title = title
        self.title_arabian = title_arabian
        self.subtitle = subtitle
        self.subtitle_arabian = subtitle_arabian
        self.tag = tag
        self.tag_arabian = tag_arabian
        self.updated = updated or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
