"""Custom bibtex style with bold titles."""

from pybtex.style.formatting.unsrt import Style as UnsrtStyle
import re
import unicodedata

from pybtex.richtext import Tag, Text
from pybtex.style import FormattedEntry
from pybtex.style.template import tag

from modality import MODALITIES


class Style(UnsrtStyle):
    """Bibliography style with bold titles."""

    def format_title(self, e, which_field, as_sentence=True):
        """Format title with bold."""
        title = e.fields.get(which_field, '')
        if title:
            title = Tag('strong', title)
        return title


class ModalityStyle(Style):
    """Bold titles, followed by the labels listed in the ``modality`` field."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # pybtex sets format_name on the instance, so a method alone would be ignored.
        self.format_name = self.format_author

    def format_author(self, person, abbr=False):
        formatted = self.name_style.format(person, abbr)
        last_name = unicodedata.normalize('NFKD', ''.join(person.last_names)).lower()
        if re.sub('[^a-z]', '', last_name) == 'ferat':
            return tag('self-author')[formatted]
        return formatted

    def format_entry(self, label, entry, bib_format=None):
        formatted = super().format_entry(label, entry, bib_format)
        keys = [key.strip() for key in entry.fields.get('modality', '').split(',') if key.strip()]
        unknown = set(keys) - set(MODALITIES)
        if unknown:
            raise ValueError(f"Unknown modality {sorted(unknown)} in entry {entry.key}")
        text = [formatted.text]
        for key in keys:
            text += [' ', Tag(f'modality-{key}', key)]
        return FormattedEntry(formatted.key, Text(*text), formatted.label)
