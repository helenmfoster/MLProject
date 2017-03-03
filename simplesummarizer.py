class SimpleSummarizer():
  """"
    This simple summarizer returns the first sentance from every paragraph of text.

    content: Dictionary where values are blocks of text, possible multiple paragraphs delineated by new line chars
  """
  def summarize(self, content):
    summarized_content = {}
    for key in content:
      summarized_content[key] = self.get_first_sentance(content[key])

    return summarized_content

  def get_first_sentance(self, value):
    first_sentances = []
    terminating_characters = ".?!"

    for line in value.split("\n"):
      print line
      current_sentance = ""
      for char in line:
        current_sentance += char
        if char in terminating_characters:
          break

      if len(current_sentance) > 0:
        first_sentances.append(current_sentance) 
    return first_sentances
