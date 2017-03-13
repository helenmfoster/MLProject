import xml.etree.ElementTree as ET

import re
import os
import sys
import gzip

# regex = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s'
regex = r"[\.?!]\s"

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
      print("Failed to open file")
      return
    headlines = ""
    sentences = ""

    for doc in root:
        try:
	    content = parse_doc(doc)
            if content is not None:
                headline, sentence = content
                headlines += headline.replace("\n", "") + "\n"
                sentences += sentence.replace("\n", " ")+ " .\n"
        except:
            print("Parsed failed")

    headlines_file = open("training_data/headlines/good-headlines-"+str(index), 'w')
    headlines_file.write(headlines.encode("utf-8"))
    headlines_file.close()

    sentences_file = open("training_data/sentences/good-sentences-"+str(index), 'w')
    sentences_file.write(sentences.encode("utf-8"))
    sentences_file.close()

def parse_doc(doc):
    headline   = doc.find("HEADLINE")
    text       = doc.find("TEXT")
    paragraphs = text.findall("P")
    
    if (len(paragraphs) > 0) and headline is not None:
        paragraph      = text.findall("P")[0]
	first_sentence = get_first_sentence(paragraph.text)
        if first_sentence is not None:
            return (headline.text, first_sentence)
    return None


def get_first_sentence(paragraph):
    result = re.split(regex, paragraph, 1, re.MULTILINE)
    if result is None:
        return None
    return result[0]

if __name__ == "__main__":
    build_dataset("input_data")
