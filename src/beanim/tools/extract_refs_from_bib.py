# The following code has been crafted with help of AI. Modifications introduced by not so intelligent human.

from pybtex.database import *  # libraries to manipulate references

__all__ = ["extract_citation"]


def extract_citation(bib_file, your_family_name, initials, output_file_name):
    """Extract family name of authors from a given .bib file into a dictionary.

    - Args::

        - bib_file: Path to .bib file.
        - your_name: To be substituted by the initials.
        - initials: As custom, your initials in the form of string.
        - output_file_name: the .txt file name where you want the dictionary.

    - Returns::

        Dictionary with entry arxiv numbers as keys and lists of
        author names as values.

    - **Example**::

        from beanim import *
        extract_citation('path/to/file', 'your_family_name', 'initials', 'output_file_name')

    .. attention::

        It will only add the eprint number. In case it does not have, you will have to add it manually. Hence, it is recommended to ensure the paper you want to cite has a bib entry with eprint.

    """
    bib_data = parse_file(bib_file)
    author_dict = {}

    for entry_key, entry in bib_data.entries.items():
        authors = []
        for person in entry.persons.get("author", []):
            # Handle last names
            if person.last_names == [your_family_name]:
                family = " ".join([initials])

            else:
                family = " ".join(person.last_names)
            authors.append(family)
        if entry.fields.get("eprint", []) == []:
            authors.append("add manually")
            # This requires some changes to add an alternative if no eprint.
        else:
            authors.append(f"{entry.fields.get('eprint', [])}".strip())
        authors = str(authors).replace("'", "")  # To remove '' in each name
        entry_key = str("'" + entry_key + "'")  # To add, so it can be called as string

        author_dict[entry_key] = str("'" + authors + "'")  # To make [...] readable.

    with open(output_file_name, "w") as f:
        f.write("{\n")
        for ref_id, authors in author_dict.items():
            f.write(f"{ref_id}: {authors}, \n")
        f.write("}\n")
