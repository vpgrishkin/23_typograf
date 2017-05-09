import unittest

from typograf import typografy_text


class TestTypografFunction(unittest.TestCase):
    def test_single_quotes(self):
        self.assertEqual(typografy_text('correct single \"quotes\"'),
         'correct single «quotes»')
    def test_double_quotes(self):
        self.assertEqual(typografy_text('\"Something \"something\"\"'),
         '«Something \"something\"»')
    def test_replace_hyphen_with_dashe_in_phone_numbers(self):
        self.assertEqual(typografy_text('+7—123—456—78—90'),
         '+7–123–456–78–90')
    def test_replace_dashes_with_hyphen(self):
        self.assertEqual(typografy_text('something - something'),
         'something — something')
    def test_link_conjunction_word_with_no_break_space(self):
        self.assertEqual(typografy_text('at work'),
         'at\u00A0work')
    def test_link_numbers_with_following_words_by_no_break_space(self):
        self.assertEqual(typografy_text('300 monkey'),
         '300\u00A0monkey')
    def test_remove_extra_spaces(self):
        self.assertEqual(typografy_text('remove     extra   spaces'),
         'remove extra spaces')
    def test_remove_extra_line_breaks(self):
        self.assertEqual(typografy_text('something\n\n\nsomething'),
         'something\nsomething')


if __name__ == "__main__":
    unittest.main()