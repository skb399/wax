from django.test import TestCase
from records.models import Genre, Record
# Import IntegrityError to test database constraints.
from django.db import IntegrityError

#-----------------------------------------------------------------------------
# GENRE MODEL TESTS
#-----------------------------------------------------------------------------
class GenreModelTest(TestCase):
    """Tests for the Genre model."""

    def test_genre_string_representation(self):
        """Test that a genre displays its friendly name."""

        genre = Genre.objects.create(
            name='deep-house',
            friendly_name='Deep House'
        )

        self.assertEqual(str(genre), 'Deep House')

    def test_genre_name_must_be_unique(self):
        """Test that two genres cannot have the same name."""
        # In this test case, the two genres have different friendly_name
        # values. This shows that the uniqueness constraint applies only to
        # name but not to friendly_name.
        Genre.objects.create(
            name='techno',
            friendly_name='Techno'
        )

        with self.assertRaises(IntegrityError):
            Genre.objects.create(
                name='techno',
                friendly_name='Techno Music'
            )
#-----------------------------------------------------------------------------
# RECORD MODEL TESTS
#-----------------------------------------------------------------------------
class RecordModelTest(TestCase):
    """Tests for the Record model."""

    def test_record_string_representation(self):
        """Test that a record displays its artist and title."""

        # Arrange: Create a genre to associate with the record.
        genre = Genre.objects.create(
            name='deep-house',
            friendly_name='Deep House'
        )

        # Act: Create a record associated with the genre.
        record = Record.objects.create(
            sku='WAX-0001',
            title='Atmosphere',
            slug='kerri-chandler-atmosphere',
            artist='Kerri Chandler',
            genre=genre,
            label='Madhouse Records',
            format='12-inch',
            description='Deep house vinyl record.',
            price='14.99',
            stock=5
        )

        # Assert: that the string representation of the record is correct.
        self.assertEqual(
            str(record),
            'Kerri Chandler - Atmosphere'
        )

    def test_record_default_values(self):
        """Test that new records have the correct default values."""

        # Arrange: Create a genre to associate with the record.
        genre = Genre.objects.create(
            name='techno',
            friendly_name='Techno'
        )
        # Act: Create a record without specifying stock or is_active.
        # This allows us to test the default values.
        record = Record.objects.create(
            sku='WAX-0002',
            title='Test Record',
            slug='test-record',
            artist='Test Artist',
            genre=genre,
            label='Test Label',
            format='12-inch',
            description='A test vinyl record.',
            price='12.99'
        )
        # Assert: that the default values for stock and is_active are correct.
        self.assertEqual(record.stock, 0)
        self.assertTrue(record.is_active)

    def test_record_sku_must_be_unique(self):
        """Test that two records cannot have the same SKU."""
        # This test creates two different records with the same SKU. Because
        # sku has unique=True, the database should reject the second record

        # Arrange: Create a genre to associate with the records.
        genre = Genre.objects.create(
            name='techno',
            friendly_name='Techno'
        )

        # Act: Create the first record with a specific SKU.
        Record.objects.create(
            sku='WAX-0001',
            title='First Record',
            slug='first-record',
            artist='Test Artist',
            genre=genre,
            label='Test Label',
            format='12-inch',
            description='First test record.',
            price='14.99'
        )
        # Assert: that creating a second record with the same SKU raises an
        # IntegrityError.
        with self.assertRaises(IntegrityError):
            Record.objects.create(
                sku='WAX-0001',
                title='Second Record',
                slug='second-record',
                artist='Another Artist',
                genre=genre,
                label='Another Label',
                format='12-inch',
                description='Second test record.',
                price='16.99'
            )

    def test_record_slug_must_be_unique(self):
        """Test that two records cannot have the same slug."""
        # Arrange: Create a genre to associate with the records.
        genre = Genre.objects.create(
            name='house',
            friendly_name='House'
        )

        # Act: Create the first record with a specific slug.
        Record.objects.create(
            sku='WAX-0001',
            title='First Record',
            slug='duplicate-slug',
            artist='First Artist',
            genre=genre,
            label='Test Label',
            format='12-inch',
            description='First test record.',
            price='14.99'
        )

        # Assert: that creating a second record with the same slug raises
        # an IntegrityError.
        with self.assertRaises(IntegrityError):
            Record.objects.create(
                sku='WAX-0002',
                title='Second Record',
                slug='duplicate-slug',
                artist='Second Artist',
                genre=genre,
                label='Test Label',
                format='12-inch',
                description='Second test record.',
                price='16.99'
            )