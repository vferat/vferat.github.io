"""Colored modality labels, written as {modality}`eeg` in Markdown pages."""

from docutils import nodes
from pybtex_docutils import Backend

MODALITIES = {
    "eeg": "EEG",
    "fmri": "fMRI",
    "meg": "MEG",
    "neuromod": "neuromod",
}


def modality_label(key, rawtext=""):
    return nodes.inline(rawtext, MODALITIES[key], classes=["vf-tag", f"vf-tag--{key}"])


class ModalityBackend(Backend):
    """Renders the pybtex tags for modality labels and for my name in author lists."""

    def format_tag(self, tag_name, text):
        if tag_name.startswith("modality-"):
            return [modality_label(tag_name.removeprefix("modality-"))]
        if tag_name == "self-author":
            return [nodes.inline("", "", *text, classes=["vf-self"])]
        return super().format_tag(tag_name, text)


def modality_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    key = text.strip().lower()
    if key not in MODALITIES:
        message = inliner.reporter.error(
            f"Unknown modality {text!r}, expected one of: {', '.join(MODALITIES)}",
            line=lineno,
        )
        return [inliner.problematic(rawtext, rawtext, message)], [message]
    return [modality_label(key, rawtext)], []


def setup(app):
    app.add_role("modality", modality_role)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
