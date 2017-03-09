from paragraph import Paragraph
import time
import subprocess

class SmartSummarizer():
  """"
    This smart summarizer summarizes paragraphs of text using a seq2seq neural net.
    content: Dictionary where values are blocks of text, possible multiple paragraphs delineated by new line chars
  """
  def __init__(self, model, first_sentance_only=True):
    self.model = model
    self.first_sentance_only = first_sentance_only 

  def get_file(self, filename):
    try:
      f = open(filename, 'w')
      return f
    except:
      return None
  
  def summarize_paragraph(self, paragraph):
    source_paragraph = " ".join(self.get_first_sentance(paragraph.content)) 
    output_file = "output-" + str(paragraph.index) + ".txt"
    input_file = "/home/helenmfoster/opennmt/input-" + str(paragraph.index) + ".txt"
    i = open(input_file, 'w')
    print source_paragraph
    i.write(source_paragraph + " .\n")
    i.close()
		
    command = "th translate.lua -model " + self.model + " -src "+ input_file +" -output " + output_file
    p = subprocess.Popen(["th translate.lua", "-model " + self.model, "-src " + input_file, "-output " + output_file], cwd="/home/helenmfoster/opennmt/")
    p.wait()
    print "executed command to translate the jawn"

    f = self.get_file(output_file)
	
    summarized_content = f.read()
    print summarized_content
    
  def summarize(self, content):
    summarized_content_array = []
    for paragraph in content:
      summarized_content_array.append(self.summarize_paragraph(paragraph))
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

from wikipage import Wikipage
print "waiting on wikipedia...."
w = Wikipage("Albert Einstein")
print "waiting on wikipedia..."
s = SmartSummarizer("textsum_epoch13_633.76.t7")
content = w.split_paragraphs()
print "okay jumping into the good stuff"
print s.summarize(w.paragraphs)
