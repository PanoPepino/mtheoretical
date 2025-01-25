import re #Some fancy libraries to find patterns. It seems so.
import json #For good format of .txt when creating the resulting dictionary.
from os import path

#The following code has been crafted with help of AI. Modifications introduced by not so intelligent human.

def read_tex_file(file_path): #This reads the desired .tex file. I guess it cannot read inputs in the texfile.
    """Function to read the input .tex file.

    Args:
        - file_path to the file you would like to read to extract the equations from.

    Returns:
       - the content, loaded to be manipulated by the rest of the functions.
    """

    with open(file_path, 'r') as file:
        content = file.read()

    return content

def extract_equations(tex_content): # The patterns to look for.
    """Main function to extract equations and their labels from the chosen .tex file.

    Args:
        - tex_content: The .tex file to read. 
    Returns:
        - dictionary: The set of equations with their keys (the labels of each equation in the .tex file)
    
    - An **Example **::

        tex_content = read_tex_file(tex_file_relative_path) #Reads the chosen .tex file given as input. (equation_dictionaries/fake_tex_file.tex)
        equations_dict = extract_equations(tex_content) #Extracts the dictionary.
        write_dict_to_file(equations_dict, output_file_relative_path) #Pours the dictionary in the .txt file chosen as output in the given input. (equation_dictionaries/eq_fake_file.txt)
        print(f"Equations have been extracted and written to {output_file_relative_path}")

    .. attention::

        - The current state of the function is not capable of identifying multi_eq, split or other commands for a more elegant display in the .pdf file.
        - This should be improved in the future.
    
    """

    equation_pattern = r'\\begin\{equation\}(.*?)\\end\{equation\}' #(.*?) means to look for whatever is sandwiched by \begin and \end eq.
    label_pattern = r'\\label\{(.*?)\}'

    equations = {}
    matches = re.finditer(equation_pattern, tex_content, re.DOTALL)
    #print(equation_pattern)

    for match in matches:
        equation_block = match.group(1)
        label_match = re.search(label_pattern, equation_block) #This looks for each of the labels that follow the label_pattern
        if label_match:
            label = label_match.group(1)
            equation = re.sub(label_pattern, '', equation_block).strip()
            equations[label] = equation #This creates the relation bewtween key and piece of the dictionary.
    return equations

def write_dict_to_file(dictionary, output_file_name):
    """This function takes the extracted dictionary and pours it down in .txt file.

    Args:
        - dictionary: it eats equations, the dictionary of the previous function.
        - output_file_name: it spits out a .txt file with the dictionary written in the right way.
    """

    with open(output_file_name, 'w') as file:
        file.write('{\n')
        for i, (key, value) in enumerate(dictionary.items()):
            # Properly format and escape the key and value
            formatted_key = json.dumps(str(key)) #It seems that json already does the conversion of \ to \\ and similar.
            formatted_equation = json.dumps(str(value))
            formatted_equation = formatted_equation.replace(".", "") #Majority of eqs. in papers end with stop or colon; In this way we get rid of them to display in slides.
            formatted_equation = formatted_equation.replace(",", "")
            
            # Write the formatted key-value pair
            file.write(f"    {formatted_key}: {formatted_equation}")
            
            # Add comma for all items except the last one
            if i < len(dictionary) - 1:
                file.write(',')
            
            file.write('\n')
        file.write('}\n')

######################################################################

# Main execution

#tex_file_relative_path= input('What is the .tex file you would like to extract the equations from? (Add the relative path):')
#output_file_relative_path= input('What is the output .txt file you would like to write down the equations at? (Add the relative path):')
#tex_file_path= path.join(path.dirname(__file__), tex_file_relative_path)
#output_file_path = path.join(path.dirname(__file__), output_file_relative_path)

#tex_content = read_tex_file(tex_file_path) #Reads the chosen .tex file given as input.
#equations_dict = extract_equations(tex_content) #Extracts the dictionary.
#write_dict_to_file(equations_dict, output_file_path) #Pours the dictionary in the .txt file chosen as output in the given input.
#print(f"Equations have been extracted and written to {output_file_path}")
