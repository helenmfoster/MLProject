#!/usr/bin/python
import os
import sys
from slideswrapper import SlidesWrapper
from simplesummarizer import SimpleSummarizer
from smartsummarizer import SmartSummarizer
from wikipage import Wikipage

__author__ = "Helen and Adel"


class Presentation():
  def __init__(self, subject, summarizer):
    self.g_slides = SlidesWrapper()
    self.w_page = Wikipage(subject)
    self.summarizer = summarizer
    self.g_slides_presentation = self.g_slides.create_presentation(subject)
    
  def build_presentation(self):
    content = self.w_page.split_paragraphs()
    brief_content = self.summarizer.summarize(content)
    self.g_slides.add_slides(self.g_slides_presentation, brief_content)

if __name__ == '__main__':
  subject = "Barack Obama"
  s = SmartSummarizer("textsum_epoch8_54.87.t7")
  #s = SimpleSummarizer()
  p = Presentation(subject, s)
  p.build_presentation()

