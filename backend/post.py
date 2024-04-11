import datetime
class Post():
    def __init__(self, id, url, title, subtitle, tag, updated=None) -> None:
        self.id = id
        self.url = url
        self.title = title
        self.subtitle = subtitle
        self.tag = tag
        self.updated = updated or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")