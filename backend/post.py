class Post():
    def __init__(self, id, url, title, subtitle, tag, block=None) -> None:
        self.id = id
        self.url = url
        self.title = title
        self.subtitle = subtitle
        self.tag = tag
        self.block = block