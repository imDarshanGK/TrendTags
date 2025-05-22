import app


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
        deduplicated_list = app.remove_duplicate_items(duplicates_list)

        # Then
        assert len(duplicates_list) == 8
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
        deduplicated_list = app.remove_duplicate_items(unique_list)

        # Then
        assert len(unique_list) == 6
        assert len(deduplicated_list) == 6
