class Line:
    def __init__(self, content):
        self.content = content
        self.sanitize_line()

    def sanitize_line(self):
        self.content.rstrip
