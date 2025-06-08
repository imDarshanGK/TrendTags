import pytest

from src import errors, tag_processing


@pytest.mark.parametrize(
    "input_tags,expected_output",
    [
        (
            ["#pythonLessons", "PythonPractice!", "#pythonsnakes"],
            ["pythonlessons", "pythonpractice", "pythonsnakes"],
        ),
        (["", "python", "java"], ["python"]),
        (["123", "#@$pythonista", "!@#", ""], ["pythonista"]),
        ([], []),
        (
            ["#Python_Rocks!", "@LearnPythonNow", "~python.dev~", "*Python*Powers*"],
            ["python_rocks", "learnpythonnow", "python dev", "python powers"],
        ),
    ],
)
def test_keep_valid_tags(input_tags, expected_output):
    topic = "python"
    assert tag_processing.filter_tags_by_topic(input_tags, topic) == expected_output


@pytest.mark.parametrize("topic", [" ", ""])
def test_empty_topics(topic):
    with pytest.raises(errors.MissingInputValueError):
        tag_processing.filter_tags_by_topic(
            ["#pythonLessons", "PythonPractice!", "#pythonsnakes"],
            topic=topic,
        )
