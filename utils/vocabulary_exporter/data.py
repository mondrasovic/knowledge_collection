from __future__ import annotations

import dataclasses
import enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterator, Sequence
    from typing import Any, Type, TypeAlias, TypeVar

    VocabDict: TypeAlias = dict[str, Any]
    T = TypeVar("T", bound="EnumInitFromStrMixin")


class EnumInitFromStrMixin:
    @classmethod
    def from_str(cls: Type[T], value: str) -> T:
        value_lower = value.lower()
        for member in cls:
            if member.value.lower() == value_lower:
                return member
        raise ValueError(f"could not find member with value `{value}`")


class StrEnumMixin:
    def __str__(self) -> str:
        return self.value


class Language(EnumInitFromStrMixin, StrEnumMixin, enum.Enum):
    SLOVAK = "Slovak"


class WordCategory(EnumInitFromStrMixin, StrEnumMixin, enum.Enum):
    NOUN = "noun"
    VERB = "verb"
    ADJECTIVE = "adjective"
    IDIOM = "idiom"


@dataclasses.dataclass(frozen=True, eq=True)
class Translation:
    language: Language
    items: Sequence[str]

    @classmethod
    def from_dict(cls, data_dict: VocabDict) -> Translation:
        return cls(language=Language.from_str(data_dict["language"]), items=data_dict["items"])


@dataclasses.dataclass(frozen=True)
class VocabularyItem:
    word: str
    definition: str
    category: WordCategory
    synonyms: Sequence[str]
    examples: Sequence[str]
    translations: Sequence[Translation]

    @classmethod
    def from_dict(cls, data_dict: VocabDict) -> VocabularyItem:
        return cls(
            word=data_dict["word"],
            definition=data_dict["definition"],
            category=WordCategory.from_str(data_dict["category"]),
            synonyms=data_dict["synonyms"],
            examples=data_dict["examples"],
            translations=[
                Translation.from_dict(translation) for translation in data_dict["translations"]
            ],
        )


@dataclasses.dataclass(frozen=True)
class Vocabulary:
    items: Sequence[VocabularyItem]

    def __len__(self) -> int:
        return len(self.items)

    def __iter__(self) -> Iterator[VocabularyItem]:
        yield from iter(self.items)

    def __getitem__(self, index: int | slice) -> VocabularyItem:
        return self.items[index]

    @classmethod
    def from_dict(cls, data_dict: VocabDict) -> Vocabulary:
        return cls(items=[VocabularyItem.from_dict(item) for item in data_dict])
