"""Custom bibtex style with bold titles."""

from pybtex.style.formatting.unsrt import Style as UnsrtStyle
from pybtex.richtext import Tag


class Style(UnsrtStyle):
    """Bibliography style with bold titles."""

    def format_title(self, e, which_field, as_sentence=True):
        """Format title with bold."""
        title = e.fields.get(which_field, '')
        if title:
            title = Tag('strong', title)
        return title
