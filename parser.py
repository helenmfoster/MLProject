import xml.etree.ElementTree as ET
import os
import sys
import gzip


def build_dataset(input_dir): 
    all_data_files = [os.path.join(input_dir,fn) for fn in next(os.walk(input_dir))[2]]

    for i in range(0, len(all_data_files)):
      parse_gigaword_file(all_data_files[i], i)

def parse_gigaword_file(fname, index):
    print "parsing gigaword file number: " + str(index) 
    try:
      f = gzip.open(fname, 'r')
      text = f.read()    
      root = ET.fromstring("<DATA>"+ text + "</DATA>")
    except:
      return
    headlines = ""
    paragraphs = ""

    for doc in root:
        content = parse_doc(doc)
        if content:
          headline, paragraph = content
          headlines += headline.text + " .\n"
          paragraphs += paragraph.text + " .\n"
    
    headlines_file = open("training_data/headlines/headlines-"+str(index), 'w')
    headlines_file.write(headlines)
    headlines_file.close()

    paragraphs_file = open("training_data/paragraphs/paragraphs-"+str(index), 'w')
    paragraphs_file.write(paragraphs)
    paragraphs_file.close()

def parse_doc(doc):
    headline   = doc.find("HEADLINE")
    text       = doc.find("TEXT")
    paragraphs = text.findall("P")
    if (len(paragraphs) > 0) and (headline is not None):
        paragraph  = text.findall("P")[0]
        return (headline, paragraph)
    else:
        return None

if __name__ == "__main__":
    build_dataset("input_data")
