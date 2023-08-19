from pybtex.database import parse_file
from datetime import datetime
from urllib.parse import quote
import os

def format_authors(authors, target_author="Bao, Y."):
    formatted_authors = []
    for author in authors:
        last_name = " ".join(author.last_names).replace("{", "").replace("}", "")
        first_initial = author.first_names[0][0].replace("{", "").replace("}", "")
        formatted_name = f'{last_name}, {first_initial}.'

        if formatted_name == target_author:
            formatted_name = f"**{formatted_name}**"

        formatted_authors.append(formatted_name)

    if len(formatted_authors) > 1:
        formatted_authors[-2] = ' & '.join(formatted_authors[-2:])
        formatted_authors.pop()
    return ', '.join(formatted_authors)


def bibtex_to_md(input_file, output_dir='../_publications'):
    bib_data = parse_file(input_file, 'bibtex')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for key in bib_data.entries:
        entry = bib_data.entries[key]

        # 将title中的": "替换为":"，否则会报错
        title = entry.fields.get('title', '').replace('{', '').replace('}', '').replace(": ", ":")
        abstract = entry.fields.get('abstract', '').replace(r'\texttimes', '×').replace(r'\%', '%')
        year = entry.fields.get('year', '')
        month = entry.fields.get('month', '')
        date = datetime.strptime(f"{year}-{month}-01", "%Y-%B-%d") if year and month else None
        venue = entry.fields.get('journal', '').replace("{", "").replace("}", "").replace(r'\&', '&')
        doi = entry.fields.get('doi', '')
        author = format_authors(entry.persons['author']) if 'author' in entry.persons else ''

        volume = entry.fields.get("volume", "")
        number = entry.fields.get("number", "")
        pages = entry.fields.get("pages", "").replace("--", "-")
        # 以解决没有卷号和期号的情况
        recommended_citation = f'{author} ({year}). {title}. {venue}, {volume}({number}), {pages}.'
        recommended_citation = f'{author} ({year}). {title}. {venue}'
        if volume:
            recommended_citation += f', {volume}'
            if number:
                recommended_citation += f'({number})'
        recommended_citation += f', {pages}.'

        md = f'''---
title: "{title}"
collection: publications
permalink: /publication/{title}
# excerpt: '{abstract}'
date: {date.strftime("%Y-%m-%d") if date else ""}
venue: '{venue}'
# paperurl: 'http://cugbaoyi.github.io/files/{key}.pdf'
# citation: '{author} ({year}). {title}. {venue}, {volume}({number}), {pages}.'
---
{abstract}

[DOI](https://doi.org/{doi})
[Download paper here](http://cugbaoyi.github.io/files/{key}.pdf)

Recommended citation: {recommended_citation}
'''

        with open(os.path.join(output_dir, f"{title}.md"), 'w') as f:
            f.write(md)

input_file = "mypaper.bib"
bibtex_to_md(input_file)
