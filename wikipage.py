import re
import wikipedia
from paragraph import Paragraph

class Wikipage:
  """Representation of wikipedia article"""
  def __init__(self, subject):
    """
      subject (string) : subject of desired wikipedia article
    """
    self.subject = subject
    self.page = wikipedia.page(self.subject)
    self.sections = self.page.sections
    self.paragraphs = []

  def get_section(self, index):
    """ Returns the corresponding section with utf-8 encoding"""
    return re.sub('<[^<]+?>', '', self.sections[index].encode("utf-8"))

  def get_header(self, index):
    """ Formats the corresponding section as wikipedia plaintext does"""
    section = self.get_section(index)
    return "= " + section + " ="

  def write_paragraph(self, section_number, content):
    """ Writes paragraph to paragraph diction with section as key, content as value"""
    if section_number == 0:
      title = "Summary"
    else:
      title = self.get_section(section_number - 1)

    paragraph = Paragraph(section_number, title, content)
    self.paragraphs.append(paragraph)

  def clean_paragraphs(self):
    """
      Removes sections that are empty
    """
    clean_paragraphs = []
    counter = 0
    for paragraph in self.paragraphs:
      content = paragraph.content
      if len(content) > 1:
        paragraph.index = counter
        counter += 1
        clean_paragraphs.append(paragraph)
      self.paragraphs = clean_paragraphs

  def split_paragraphs(self):
    """Splits up a wikipedia article into sections and writes to dictionary"""
    content = self.page.content.encode("utf-8").split("\n")
    section_number = 0
    num_sections = len(self.sections)
    current_header = self.get_header(section_number)
    current_content = []

    for line in content:
      if current_header in line:
        self.write_paragraph(section_number, current_content)
        current_content = []
        section_number += 1

        if section_number < num_sections:
          current_header = self.get_header(section_number)
        else:
          break

      elif len(line.strip()) > 0:
        current_content.append(line)

    self.write_paragraph(section_number, current_content)
    self.clean_paragraphs()
    return self.paragraphs

#w = Wikipage("Albert Einstein")
#print w.split_paragraphs()
