from paragraph import Paragraph

class SimpleSummarizer():
  """"
    This simple summarizer returns the first sentance from every paragraph of text.

    content: Dictionary where values are blocks of text, possible multiple paragraphs delineated by new line chars
  """
  def summarize(self, content):
    summarized_content_array = []
    for paragraph in content:
      summarized_content = self.get_first_sentance(paragraph.content)
      title = paragraph.title
      index = paragraph.index
      summarized_paragraph = Paragraph(index, title, summarized_content)

      summarized_content_array.append(summarized_paragraph)

    return summarized_content_array

  def get_first_sentance(self, value):
    first_sentances = []
    terminating_characters = ".?!"

    for line in value:
      current_sentance = ""
      for char in line:
        current_sentance += char
        if char in terminating_characters:
          break

      if len(current_sentance) > 0:
        first_sentances.append(current_sentance) 
    return first_sentances

#from wikipage import Wikipage
#w = Wikipage("Albert Einstein")
#s = SimpleSummarizer()
#content = w.split_paragraphs()
#print s.summarize(w.paragraphs)
