import ebooklib
from ebooklib import epub
import re
import os
import sys

INPUT_MD = sys.argv[1] if len(sys.argv) > 1 else 'foundation_book.md'
OUTPUT_EPUB = 'German_Foundation_Vocabulary.epub'

def create_epub():
    book = epub.EpubBook()

    # Metadata
    book.set_identifier('id123456')
    book.set_title('The Platinum German Vocabulary Builder')
    book.set_language('de')
    book.add_author('Leonardo Torres Hernández')

    # CSS
    style = '''
    @namespace epub "http://www.idpf.org/2007/ops";
    body {
        font-family: Cambria, Liberation Serif, Bitstream Vera Serif, Georgia, Times, Times New Roman, serif;
    }
    h1 {
        text-align: left;
        text-transform: uppercase;
        font-weight: 200;
    }
    ul {
        list-style-type: none;
        padding: 0;
    }
    li {
        margin-bottom: 1em;
    }
    '''
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
    book.add_item(nav_css)

    # Chapters
    chapters = []

    # Read MD file
    if not os.path.exists(INPUT_MD):
        print(f"Error: {INPUT_MD} not found.")
        # Try to concatenate parts if they exist?
        # But for now assume input file is ready.
        return

    with open(INPUT_MD, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by Sessions
    # Regex for # Session X
    # Use re.split but keep delimiter? No, split by header.
    parts = re.split(r'(# Session \d+)', content)

    # parts[0] is preamble (Title, Copyright)
    # parts[1] is Header 1, parts[2] is Content 1, etc.

    # Process Preamble/Copyright
    preamble = parts[0]
    # Simple HTML conversion for preamble
    preamble_html = f"<h1>Title Page</h1><p>{preamble.replace(chr(10), '<br/>')}</p>"
    c_page = epub.EpubHtml(title='Title Page', file_name='title.xhtml', lang='en')
    c_page.content = preamble_html
    c_page.add_item(nav_css)
    book.add_item(c_page)
    chapters.append(c_page)

    # Process Sessions
    for i in range(1, len(parts), 2):
        header = parts[i].strip() # "# Session 1"
        body = parts[i+1].strip()

        session_id = header.replace("# ", "")
        title = session_id

        # Convert body markdown to HTML
        # List items: * **Key:** Value
        html_body = f"<h1>{title}</h1>"
        html_body += "<ul>"

        lines = body.split('\n')
        for line in lines:
            line = line.strip()
            if not line: continue

            # Convert * **Key:** Value -> <li><strong>Key:</strong> Value</li>
            # Regex: \* \*\*(.*?)\*\* (.*)
            match = re.match(r'\*   \*\*(.*?)\*\* (.*)', line)
            if match:
                key = match.group(1)
                val = match.group(2)
                html_body += f"<li><strong>{key}</strong> {val}</li>"
            else:
                # Maybe continuation or plain text?
                html_body += f"<li>{line}</li>"

        html_body += "</ul>"

        chapter = epub.EpubHtml(title=title, file_name=f'session_{session_id.replace(" ", "_")}.xhtml', lang='de')
        chapter.content = html_body
        chapter.add_item(nav_css)
        book.add_item(chapter)
        chapters.append(chapter)

    # TOC and Spine
    book.toc = tuple(chapters)
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    book.spine = ['nav'] + chapters

    epub.write_epub(OUTPUT_EPUB, book, {})
    print(f"EPUB created: {OUTPUT_EPUB}")

if __name__ == "__main__":
    create_epub()
