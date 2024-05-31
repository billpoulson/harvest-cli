import pytest
from util import parse_hours

class TestUtil:

    @pytest.mark.parametrize("input_time, expected_output", [
        ("1:30", 1.5),
        ("0:45", 0.75),
        ("2:00", 2.0),
        ("10:15", 10.25)
    ])
    def test_parse_hours_valid_input(self, input_time, expected_output):
        assert parse_hours(input_time) == expected_output

    @pytest.mark.parametrize("invalid_input", ["abc", "1.30", "1:", ":30"])
    def test_parse_hours_invalid_input(self, invalid_input):
        with pytest.raises(ValueError, match="Invalid time format. Use H:MM format."):
            parse_hours(invalid_input)

    def test_parse_hours_edge_cases(self):
        assert parse_hours("0:00") == 0.0
        assert parse_hours("23:59") == 23 + 59 / 60.0
