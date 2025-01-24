import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mtheoretical.src.tools import *

##THIS REQUIRES SOME THOUGHTS. HOW TO CALL TOOLS WITHOUT CALLING THE WHOLE MTHEORETICAL PACKAGE

tex_file_relative_path= input('What is the .tex file you would like to extract the equations from? (Add the relative path):')
output_file_relative_path= input('What is the output .txt file you would like to write down the equations at? (Add the relative path):')
#tex_file_path= path.join(path.dirname(__file__), tex_file_relative_path)
#print(path.join(path.dirname(__file__)," .."))
#output_file_path = path.join(path.dirname(__file__), output_file_relative_path)

tex_content = read_tex_file(tex_file_relative_path) #Reads the chosen .tex file given as input.
equations_dict = extract_equations(tex_content) #Extracts the dictionary.
write_dict_to_file(equations_dict, output_file_relative_path) #Pours the dictionary in the .txt file chosen as output in the given input.
print(f"Equations have been extracted and written to {output_file_relative_path}")