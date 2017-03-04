class Paragraph:
    def __init__(self, index, title, content):
      self.index = index
      self.title = title
      self.content = content

    def __str__(self):
      return "Title: " + self.title + "\nIndex: " + str(self.index) + "\nContent: " + str(self.content)
