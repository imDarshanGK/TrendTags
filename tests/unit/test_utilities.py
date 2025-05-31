from src import utilities


class TestRemoveDuplicateTags:
    def test_remove_duplicate_items(self):
        # Given
        duplicates_list = [
            "tag1",
            "tag2",
            "tag3",
            "tag4",
            "tag1",
            "tag5",
            "tag5",
            "tag6",
        ]

        # When
        deduplicated_list = utilities.remove_duplicate_items(duplicates_list)

        # Then
        assert len(deduplicated_list) == 6


    def test_remove_duplicate_items_unique(self):
        # Given
        unique_list = [
            "tag1",
            "tag2",
            "tag3",
            "tag4",
            "tag5",
            "tag6",
        ]

        # When
        deduplicated_list = utilities.remove_duplicate_items(unique_list)

        # Then
        assert deduplicated_list == unique_list
