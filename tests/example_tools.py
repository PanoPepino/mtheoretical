from beanim import extract_citation, extract_equations

# tex_file_relative_path= input('What is the .tex file you would like to extract the equations from? (Add the relative path):')
# output_file_relative_path= input('What is the output .txt file you would like to write down the equations at? (Add the relative path):')

# tex_content = read_tex_file(tex_file_relative_path) #Reads the chosen .tex file given as input. (equation_dictionaries/fake_file.tex)
# equations_dict = extract_equations(tex_content) #Extracts the dictionary.
# write_dict_to_file(equations_dict, output_file_relative_path) #Pours the dictionary in the .txt file chosen as output in the given input. (equation_dictionaries/eq_fake_file.txt)
# print(f"Equations have been extracted and written to {output_file_relative_path}")

extract_citation(
    bib_file="example_refeq/latex/test_ref.bib",
    your_family_name="Panizo",
    initials="DP",
    output_file_name="example_refeq/dictionaries/test_ref.txt",
)

extract_equations(
    tex_file="example_refeq/latex/test_file.tex",
    output_file="example_refeq/dictionaries/eq_test_file.txt",
)
