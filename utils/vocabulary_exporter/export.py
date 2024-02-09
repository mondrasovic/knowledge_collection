from __future__ import annotations

import abc
import re
from typing import TYPE_CHECKING

from .utils import encode_url, get_current_month_name

if TYPE_CHECKING:
    from os import PathLike

    from .data import Translation, Vocabulary, VocabularyItem


class VocabularyExporter(abc.ABC):
    @abc.abstractmethod
    def export(self, vocabulary: Vocabulary) -> None:
        pass


class VSCodeRevealExporter(VocabularyExporter):
    def __init__(self, output_file_path: PathLike) -> None:
        self.output_file_path = output_file_path

    def export(self, vocabulary: Vocabulary) -> None:
        with open(self.output_file_path, "wt") as out_file:
            out_file.write(self.vocabulary_to_markdown(vocabulary))

    @classmethod
    def vocabulary_to_markdown(cls, vocabulary: Vocabulary) -> str:
        title = "English Vocabulary"
        subtitle = f"Personal Collection - {get_current_month_name()} 2024"
        author = "Milan Ondrašovič"

        vocabulary_items_markdown = "---\n".join(
            cls.vocabulary_item_to_markdown(item) for item in vocabulary
        )
        return f"""---
title: {title} - {subtitle}
author: {author}
format: revealjs
theme: moon
highlight-style: base16-tomorrow
defaultTiming: 140
width: 1920
height: 1080
---

<style>
.reveal h2 {{ font-size: 2.0em; }}
.reveal h3 {{ font-size: 1.5em; }}
.reveal h4 {{ font-size: 1.25em; }}

.reveal blockquote {{
    padding: 0px;
}}
</style>

# {title}

## {subtitle}

Created by *{author}*

---

{vocabulary_items_markdown}
"""

    @classmethod
    def vocabulary_item_to_markdown(cls, vocabulary_item: VocabularyItem) -> str:
        synonyms = ", ".join(vocabulary_item.synonyms)
        examples = "\n\n".join(f"> {example}" for example in vocabulary_item.examples)

        youglish_url_us = cls.build_youglish_url(vocabulary_item.word, dialect="us")
        youglish_url_uk = cls.build_youglish_url(vocabulary_item.word, dialect="uk")

        translation_rows = "\n".join(
            cls.translation_to_table_row(translation)
            for translation in vocabulary_item.translations
        )

        return f"""
## Word: "{vocabulary_item.word}"

### General Information

* **definition**: {vocabulary_item.definition}
* **category**: *{vocabulary_item.category}*
* **synonyms**: {synonyms}

### Usage Example

{examples}

**Pronunciation**: [US English]({youglish_url_us}), [UK English]({youglish_url_uk})

| Language | Translation(s) |
| -------- | ------------ |
{translation_rows}

"""

    @staticmethod
    def translation_to_table_row(translation: Translation) -> str:
        items = ", ".join(translation.items)
        translation_row = f"| *{translation.language}* | {items} |"
        return translation_row

    @classmethod
    def build_youglish_url(cls, word: str, dialect: str = "us") -> str:
        conversation_style_word = cls.adapt_word_to_conversation_style(word)
        return encode_url(
            f"https://youglish.com/pronounce/{conversation_style_word}/english/{dialect}"
        )

    @staticmethod
    def adapt_word_to_conversation_style(word: str) -> str:
        return re.sub("^to ", "", word)
