import unittest
from unittest.mock import patch, MagicMock

import main


class TestFunctions(unittest.TestCase):
    @patch('builtins.input', side_effect=['2022'])
    def test_year_correct_input(self, mock_input):
        self.assertEqual(main.current_year(), '2022')

    @patch('builtins.input', side_effect=['2025', '2022'])
    def test_year_value_invalid_input(self, mock_input):
        with patch('builtins.print') as mocked_print:
            self.assertEqual(main.current_year(), '2022')
            mocked_print.assert_called_with("Пожалуйста, введите год в диапазоне от 0 до 2024.")

    @patch('builtins.input', side_effect=['adc', '2022'])
    def test_year_invalid_input(self, mock_input):
        with patch('builtins.print') as mocked_print:
            self.assertEqual(main.current_year(), '2022')
            mocked_print.assert_called_with("Пожалуйста, введите допустимое число.")

    @patch('builtins.input', side_effect=['1'])
    def test_id_correct_input(self, mock_input):
        library = MagicMock()
        library.get_last_id.return_value = 10
        self.assertEqual(main.current_id(library), '1')

    @patch('builtins.input', side_effect=['11', '1'])
    def test_id_value_invalid_input(self, mock_input):
        library = MagicMock()
        library.get_last_id.return_value = 10
        with patch('builtins.print') as mocked_print:
            self.assertEqual(main.current_id(library), '1')
            mocked_print.assert_called_with("Пожалуйста, введите правильный id.")

    @patch('builtins.input', side_effect=['asd', '1'])
    def test_id_invalid_input(self, mock_input):
        library = MagicMock()
        library.get_last_id.return_value = 10
        with patch('builtins.print') as mocked_print:
            self.assertEqual(main.current_id(library), '1')
            mocked_print.assert_called_with("Пожалуйста, введите допустимое число.")

    @patch('builtins.input', side_effect=['1'])
    def test_status_correct_input(self, mock_input):
        self.assertEqual(main.current_status(), 1)


if __name__ == '__main__':
    unittest.main()
