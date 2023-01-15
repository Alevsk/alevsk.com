#!/usr/bin/env python

import os
import re
from bs4 import BeautifulSoup
from html import unescape
from html import escape
from pygments import highlight
from pygments.lexers import guess_lexer
from pygments.formatters import TerminalFormatter

# This script was created with the help of ChatGPT
# It is used to migrate existing WordPress posts in HTML to Markdown posts
# used by the Hugo static web generator

def convert_to_code_block_file(file_path):
    f = open(file_path, 'r')
    text = f.read()
    f.close()
    pattern = r'\[(.*?)\](.*?)\[\/\1\]'
    matches = re.finditer(pattern, text, re.DOTALL)
    for match in matches:
        language, code = match.groups()
        code = code.strip()
        code_block = f'```{language}\n{code}\n```'
        text = text.replace(match.group(), code_block)
    f = open(file_path, 'w')
    f.write(text)
    f.close()


def remove_p_align_center_wrapper(file_path):
    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
    ps = soup.find_all('p', class_='has-text-align-center')
    for p in ps:
        markdown_img = p.text.strip()
        p.replace_with(markdown_img)
    with open(file_path, 'w') as f:
        f.write(str(soup))


def remove_div_wrapper(file_path):
    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
    divs = soup.find_all('div', class_='wp-block-image')
    for div in divs:
        img = div.find('img')
        if img:
            img_src = img['src']
            figcaption = div.find('figcaption', class_='wp-element-caption')
            if figcaption:
                description = figcaption.text.strip()
                markdown_img = f'![{"" if description is None else description}]({img_src})'
            else:
                markdown_img = f'![]({img_src})'
            div.replace_with(markdown_img)
    with open(file_path, 'w') as f:
        f.write(str(soup))


def remove_figure_wrapper(file_path):
    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
    divs = soup.find_all('figure', class_='wp-block-image')
    for div in divs:
        img = div.find('img')
        if img:
            img_src = img['src']
            figcaption = div.find('figcaption')
            if figcaption:
                description = figcaption.text.strip()
                markdown_img = f'![{"" if description is None else description}]({img_src})'
            else:
                markdown_img = f'![]({img_src})'
            div.replace_with(markdown_img)
    with open(file_path, 'w') as f:
        f.write(str(soup))


def remove_angle_brackets(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    urls = re.findall(r'<(https?://.*?)>', content)
    for url in urls:
        content = content.replace('<'+url+'>', url)
    with open(file_path, 'w') as f:
        f.write(content)


def remove_figure_tags(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    content = re.sub(r'<figure.*?>.*?</figure>', '', content)
    with open(file_path, 'w') as f:
        f.write(content)


def convert_tables_to_markdown(file_path):
    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        convert_figure_tags(soup)
        unescaped_content = unescape(str(soup))
        with open(file_path, 'w') as f:
            f.write(unescaped_content)


def convert_figure_tags(soup):
    figures = soup.find_all("figure", class_="wp-block-table")
    for figure in list(figures):
        table_in_figure = figure.find('table')
        if table_in_figure:
            markdown_table = "\n" + table_to_markdown(table_in_figure)
            figure.replace_with(markdown_table)


def table_to_markdown(table):
    headers = []
    rows = []
    for row in table.find_all('tr'):
        cells = row.find_all(['th', 'td'])
        if cells:
            if row.th:
                headers.append(cells)
            else:
                rows.append(cells)
    if headers:
        header_row = ' | '.join(escape(cell.get_text(strip=True))
                                for cell in headers[0])
        separator = '|'.join(['---']*len(headers[0]))
        markdown_table = f"{header_row}\n{separator}\n"
        for row in rows:
            markdown_table += f"{' | '.join(convert_table_code_to_markdown(cell) for cell in row)}\n"
    else:
        first_row = rows.pop(0)
        header_row = ' | '.join(escape(cell.get_text(strip=True))
                                for cell in first_row)
        separator = '|'.join(['---']*len(first_row))
        markdown_table = f"{header_row}\n{separator}\n"
        for row in rows:
            markdown_table += f"{' | '.join(convert_table_code_to_markdown(cell) for cell in row)}\n"
    return markdown_table


def convert_table_code_to_markdown(cell):
    code_tags = cell.find_all('code')
    for tag in code_tags:
        content = tag.get_text(strip=True)
        tag.replace_with(f"`{content}`")
    return escape(cell.get_text(strip=True))


def convert_images_to_markdown(file_path):
    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        images = soup.find_all('img')
        for image in images:
            src = image.get('src')
            alt = "" if image.get('alt') is None else image.get('alt')
            # replace the image tag with markdown format
            image.replace_with("![{}]({})".format(alt, src))
        unescaped_content = unescape(str(soup))
        with open(file_path, 'w') as f:
            f.write(unescaped_content)


def convert_figures_images_to_markdown(file_path):
    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        figures = soup.find_all('figure')
        for figure in figures:
            if figure.find('img'):
                img = figure.img
                src = img.get('src')
                alt = "" if img.get('alt') is None else img.get('alt')
                # replace the image tag with markdown format
                img.replace_with("![{}]({})".format(alt, src))
                figure.unwrap()
        unescaped_content = unescape(str(soup))
        with open(file_path, 'w') as f:
            f.write(unescaped_content)


def convert_div_figure_to_markdown(file_path):
    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
    figures = soup.find_all('div', class_='wp-block-image')
    for figure in figures:
        img = figure.find('figure').find('img')
        if img:
            img_src = img['src']
            img_alt = "" if img['alt'] is None else img['alt']
            markdown_img = f'![{img_alt}]({img_src})'
            figure.replace_with(markdown_img)
    with open(file_path, 'w') as f:
        f.write(str(soup))


def convert_code_to_markdown(file_path):
    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        pre_tags = soup.find_all('pre')
        for pre_tag in pre_tags:
            code = pre_tag.get_text()
            lexer = guess_lexer(code)
            language = lexer.name
            fenced_code = '```' + language + '\n' + code + '\n```'
            pre_tag.replace_with(fenced_code)
        unescaped_content = unescape(str(soup))
        with open(file_path, 'w') as f:
            f.write(unescaped_content)


def convert_links_to_markdown(file_path):
    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            text = link.get_text()
            # replace the link with markdown format
            link.replace_with("[{}]({})".format(text, href))
        unescaped_content = unescape(str(soup))
        with open(file_path, 'w') as f:
            f.write(unescaped_content)


def convert_blockquote_to_markdown(file_path):
    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        blockquotes = soup.find_all('blockquote', {'class': 'wp-block-quote'})
        for blockquote in blockquotes:
            text = blockquote.find('p').get_text().lstrip()
            blockquote.replace_with("\n> " + text + "\n")
        unescaped_content = unescape(str(soup))
        with open(file_path, 'w') as f:
            f.write(unescaped_content)


folder_path = 'content/posts'

for file_name in os.listdir(folder_path):
    if file_name.endswith('.md'):
        file_path = os.path.join(folder_path, file_name)
        # remove angle brackets
        remove_angle_brackets(file_name)
        # remove div wrapper
        remove_div_wrapper(file_name)
        remove_figure_wrapper(file_name)
        # convert images
        convert_div_figure_to_markdown(file_path)
        convert_figures_images_to_markdown(file_path)
        convert_images_to_markdown(file_path)
        # remove p wrapper
        remove_p_align_center_wrapper(file_name)
        # convert blockquote
        convert_blockquote_to_markdown(file_path)
        # convert links
        convert_links_to_markdown(file_path)
        # convert code
        convert_code_to_markdown(file_path)
        # convert brackets to code
        convert_to_code_block_file(file_path)
        # convert tables
        convert_tables_to_markdown(file_path)
        # remove tags
        remove_figure_tags(file_path)
