import re #Some fancy libraries to find patterns. It seems so.

#The following code has been crafted with help of AI. Modifications introduced by not so intelligent human.

__all__= ['extract_equations']

import re

def extract_equations(tex_file, output_file):
    """

    Extract labeled equations from .tex file and save as {'label': 'equation'} dictionary
    
    Args::

        - tex_file (str): Path to input .tex file
        - output_file (str): Path for output .txt file

    Returns::

        A .txt file with a colllection of equations in the form a dictionary. Labels are the keys.

    - **Example**::

        from beanim import *
        extract_equation('path/to/file', 'output_file_name')

    """
    with open(tex_file, 'r', encoding='utf-8') as f:
        content = f.read()

    equation_dict = {}
    
    # Match equation environments (including starred versions)
    pattern = r'\\begin{equation\*?}(.*?)\\end{equation\*?}'
    
    for match in re.finditer(pattern, content, re.DOTALL):
        eq_content = match.group(1)
        
        # Filter out equations containing align environments
        if re.search(r'\\begin{align\b', eq_content):
            continue
            
        # Extract labels
        labels = re.findall(r'\\label{([^}]+)}', eq_content)
        if not labels:
            continue
            
        # Clean equation content
        cleaned = re.sub(r'\\(label|tag){[^}]+}|%.*', '', eq_content)
        cleaned = ' '.join(cleaned.strip().split())
        
        equation_dict[labels[0]] = cleaned
    
    # Save to text file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('{\n')
        for label, eq in equation_dict.items():
            #Majority of eqs. in papers end with stop or colon; In this way we get rid of them to display in slides.
            eq = eq.replace(",", "").replace("\\","\\\\")
              
            f.write("'"+ label + "'" + ': '+ "'"+ eq + "'"+  ",\n")
        f.write('}\n')



