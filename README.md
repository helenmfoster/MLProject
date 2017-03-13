# On Demand Slides
## How to Use
  ` pip install git+https://github.com/lucasdnd/Wikipedia.git --upgrade `
  
  Add google slides secret to client_secret.json. Install lua and torch.

#### Data Proprocessing
Make a home for the output of the parser:
  ```
  mkdir training_data 
  mkdir training_data/headlines #empty
  mkdir training_data/paragraphs #empty
  ```
  
  Add name of directory where input data is stored to line 67 of parser. Data must be formatted identically to gigaword dataset. Run the parser:
  
  ```
  python parser.py
  ```
  
  Divide the data as you choose into training, testing, and verification. Then, combine all training data into one file:
  
  ```
  cat training_data_files > training_data
  ```
  
  Repeat for testing and verification data. Run the OpenNMT preprocess script:
  
  ```
  th preprocess.lua -train_src training_source.txt -train_tgt training_target.txt -valid_src valid_source.txt -valid_tgt valid_target.txt -save_data final_training_data
  ```
  
#### Training the Model
  ```
  th train.lua -data data/final_training_data.t7 -save_model model_name -gpuid 1
  ```
  
#### Running the Model
  Edit presentation.py by adding your desired slide subject to line 19.The first time you run it, the application will ask for read-write priveledges to your google drive. This is so the model can add a slide deck to your drive. When the command finishes running, look for a slide deck in your google drive with the same name as your subject.
  
  ```
  python presentation.py
  ```
  
