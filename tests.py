import unittest

from typograf import typografy_text


class TestTypografFunction(unittest.TestCase):
    def test_single_quotes(self):
        self.assertEqual(typografy_text('КБ "ЙЦУКЕН"'),
         'КБ «ЙЦУКЕН»')
    def test_double_quotes(self):
        self.assertEqual(typografy_text('НИИ "КБ "ЙЦУКЕН""'),
         'НИИ «КБ "ЙЦУКЕН"»')
    def test_replace_hyphen_with_dash_in_phone_numbers(self):
        self.assertEqual(typografy_text('+7—123—456—78—90'),
         '+7–123–456–78–90')
    def test_replace_hyphen_with_dash(self):
        self.assertEqual(typografy_text('Тире - один из знаков препинания.'),
         'Тире — один из\u00A0знаков препинания.')
    def test_link_conjunction_word_with_no_break_space(self):
        self.assertEqual(typografy_text('на работе'),
         'на\u00A0работе')
    def test_link_numbers_with_following_words_by_no_break_space(self):
        self.assertEqual(typografy_text('300 обезьян'),
         '300\u00A0обезьян')
    def test_remove_extra_spaces(self):
        self.assertEqual(typografy_text('очень   много   пробелов'),
         'очень много пробелов')
    def test_remove_extra_line_breaks(self):
        self.assertEqual(typografy_text('много пустых\n\n\nстрок'),
         'много пустых\nстрок')


if __name__ == "__main__":
    unittest.main()