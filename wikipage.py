import wikipedia

class Wikipage:
  """Representation of wikipedia article"""
  def __init__(self, subject):
    """
      subject (string) : subject of desired wikipedia article
    """

    self.subject = subject
    self.page = wikipedia.page(self.subject)
    self.sections = self.page.sections
    self.paragraphs = {}

  def get_section(self, index):
    """ Returns the corresponding section with utf-8 encoding"""
    return self.sections[index].encode("utf-8") 

  def get_header(self, index):
    """ Formats the corresponding section as wikipedia plaintext does"""
    section = self.get_section(index)
    return "= " + section + " ="

  def write_paragraph(self, section_number, content):
    """ Writes paragraph to paragraph diction with section as key, content as value"""
    if section_number == 0:
      section = "Summary"
    else:
      section = self.get_section(section_number - 1)
    self.paragraphs[section] = content

  def split_paragraphs(self):
    """Splits up a wikipedia article into sections and writes to dictionary"""
    content = self.page.content.encode("utf-8").split("\n")

    section_number = 0
    current_header = self.get_header(section_number)
    current_content = ""

    for line in content:
      current_content += line + "\n"
      if current_header in line:
        self.write_paragraph(section_number, current_content)

        current_content = ""
        section_number += 1
        current_header = self.get_header(section_number)

    self.write_paragraph(section_number, current_content)
    return self.paragraphs

#w = Wikipage("Albert Einstein")
#print w.split_paragraphs()
