import pytest

from tdd_toy_example import rot13


def test_transform_empty_string():
    assert rot13.transform("") == "", "Empty string should return empty string"


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("a", "n"),
        ("n", "a"),
        ("abcdefghijklmnopqrstuvwxyz", "nopqrstuvwxyzabcdefghijklm"),
    ],
    ids=["forward", "backward", "string"],
)
def test_transform_lowercase_letters(test_input, expected):
    assert rot13.transform(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("A", "N"),
        ("N", "A"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NOPQRSTUVWXYZABCDEFGHIJKLM"),
    ],
    ids=["forward", "backward", "string"],
)
def test_transform_uppercase_letters(test_input, expected):
    assert rot13.transform(test_input) == expected


@pytest.mark.parametrize("test_input", ["`", "{", "@", "[", "`{@["])
def test_transform_symbols(test_input):
    assert rot13.transform(test_input) == test_input


def test_transform_numbers():
    assert rot13.transform("0123456789") == "0123456789"


@pytest.mark.parametrize("test_input", ["äöüßéñç", "ÄÖÜẞÉÑÇ"])
def test_transform_non_english_letters(test_input):
    assert rot13.transform(test_input) == test_input


@pytest.mark.parametrize("test_input", ["👍", "💁", "👌", "😍"])
def test_transform_emoji_string(test_input):
    assert rot13.transform(test_input) == test_input


def test_transform_no_parameter():
    with pytest.raises(TypeError, match="Expected string parameter"):
        rot13.transform()


def test_transform_wrong_parameter_type():
    with pytest.raises(TypeError, match="Expected string parameter"):
        rot13.transform(1)
