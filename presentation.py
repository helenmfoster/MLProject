import os
from slideswrapper import SlidesWrapper
from wikipage import Wikipage

class Presentation():
  def __init__(self, subject):
    self.g_slides = SlidesWrapper()
    self.w_page = Wikipage(subject)
    self.g_slides_presentation = self.g_slides.create_presentation(subject)
    
  def build_presentation(self):
    self.content = "go cats"
    #self.content = self.w_page.split_paragraphs()
    self.g_slides.add_slides(self.g_slides_presentation, self.content)

if __name__ == '__main__':
  subject = "Albert Einstein"
  p = Presentation(subject)
  p.build_presentation()

