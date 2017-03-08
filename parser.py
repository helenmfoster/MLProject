import xml.etree.ElementTree as ET
import os.path.isdir as isdir
import os.path.isfile as isfile
import os.path.exists as exists
import os.glob as glob
import sys




def get_dir_files(path_to_dir):
    pass


def parse_gigaword_file(fname):
    root = ET.parse(fname).getroot() 

    for doc in root:
        headline, paragraph = parse_doc(doc)


def parse_doc(doc):
    headline   = doc.find("HEADLINE")
    text       = doc.find("TEXT")
    paragraph  = text.findall("P")[0]

    return (headline, paragraph)
        
    


if __name__ == "__main__"
    input_path = sys.argv[1] if len(sys.argv) >= 2 else "./input"
    output_path = sys.argv[2] if len(sys.argv) >= 3 else "./output"
    
    if not exists(input_path):
        sys.exit(0)

    if not exists(output_path):
        mkdir() # needs to be imported

    if isdir(input_path):
        files = get_dir_files(input_path)

        for f in files:
            output = parse_gigaword_file(f)
            save_output(output, output_path)
    else:
        #isfile
        output = parse_gigaword_file(input_path)
        save_output(output, output_path)
