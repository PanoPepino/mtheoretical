import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../mtheoretical/src/tools')))
from extract_eq_from_tex import * #I do not know how to make the interpreter recognise the methods without invoking the whole package.

tex_file_relative_path= input('What is the .tex file you would like to extract the equations from? (Add the relative path):')
output_file_relative_path= input('What is the output .txt file you would like to write down the equations at? (Add the relative path):')

tex_content = read_tex_file(tex_file_relative_path) #Reads the chosen .tex file given as input. (equation_dictionaries/fake_tex_file.tex)
equations_dict = extract_equations(tex_content) #Extracts the dictionary.
write_dict_to_file(equations_dict, output_file_relative_path) #Pours the dictionary in the .txt file chosen as output in the given input. (equation_dictionaries/eq_fake_file.txt)
print(f"Equations have been extracted and written to {output_file_relative_path}")