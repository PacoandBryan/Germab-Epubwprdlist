# The Platinum German Vocabulary Builder

This project contains the source code and content for "The Platinum German Vocabulary Builder".

## Files

*   `Foundation.csv`: Source vocabulary list (3000 words, 150 sessions).
*   `foundation_book.md`: The generated Markdown book (generated content).
*   `German_Foundation_Vocabulary.epub`: The final EPUB book.
*   `write_manual_content.py`: Python script to generate high-quality, manually curated content blocks.
*   `create_epub.py`: Python script to convert Markdown to EPUB.

## Generation Process

The content is created manually in chunks to ensure high linguistic quality (correct grammar, context-aware translation, and sophisticated B2 example sentences). The `write_manual_content.py` script serves as the builder for these curated sessions.

## Re-generating the Book

To regenerate the book:

1.  Ensure dependencies are installed:
    ```bash
    pip install ebooklib
    ```

2.  Run the manual content builder:
    ```bash
    python3 write_manual_content.py
    ```

3.  Create the EPUB:
    ```bash
    python3 create_epub.py foundation_book.md
    ```

## Copyright

Copyright © 2024 by Leonardo Torres Hernández.
