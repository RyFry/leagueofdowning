from haystack.utils import Highlighter
from django.utils.html import strip_tags

class BoldHighlighter(Highlighter):
    def highlight(self, text_block):
        self.text_block = strip_tags(text_block)
        highlight_locations = self.find_highlightable_words()
        start_offset, end_offset = self.find_window(highlight_locations)

        # this is my only edit here, but you'll have to experiment
        start_offset = 0
        return self.render_html(highlight_locations, start_offset, end_offset)

    def render_html(self, highlight_locations=None, start_offset=None, end_offset=None):
        highlighted_chunk = self.text_block[start_offset:end_offset]

        for word in self.query_words:
            highlighted_chunk = highlighted_chunk.replace(word, '<b>' + word + '</b>')

        return highlighted_chunk
