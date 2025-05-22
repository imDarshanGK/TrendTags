import pytest
import app


@pytest.fixture(scope="module")
def duplicates_test_list():
    return [
        "tag1",
        "tag2",
        "tag3",
        "tag4",
        "tag1",
        "tag5",
        "tag5",
        "tag6",
    ]


@pytest.fixture(scope="module")
def unique_test_list():
    return [
        "tag1",
        "tag2",
        "tag3",
        "tag4",
        "tag5",
        "tag6",
    ]


def test_remove_duplicate_tags(duplicates_test_list):
    # Given
    tags = app.remove_duplicate_tags(duplicates_test_list)

    # Then
    assert len(duplicates_test_list) == 8
    assert len(tags) == 6


def test_remove_duplicate_tags_unique(unique_test_list):
    # Given
    tags = app.remove_duplicate_tags(unique_test_list)

    # Then
    assert len(unique_test_list) == 6
    assert len(tags) == 6


def test_remove_duplicate_tags_min_size():
    # Given
    tags_original = ["tag1"]
    
    # When
    tags_deduplicated = app.remove_duplicate_tags(tags_original)
    
    # Then
    assert len(tags_original) == 1
    assert len(tags_deduplicated) == 1
    