from django.db import models

# Create your models here.
class Genre(models.Model):
    # A unique genre name that is internal so the user cannot see it, such as "Rock"
    name = models.CharField(max_length=100, unique=True)

    # The name that is displayed to the user such as "Rock & Roll"
    friendly_name = models.CharField(max_length=100, unique=True)

    # String readable representation of the genre name in Django admin.
    def __str__(self):
        return self.friendly_name

# Meta information for the Genre model.
class Record(models.Model):

    # Unique identifier for each record, such as a SKU or catalog number
    sku = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=200)

    # This allows readable URLs for each record based on its title and artist,
    # e.g., "/records/jeff-mills-the-bells/"
    slug = models.SlugField(max_length=200, unique=True)
    artist = models.CharField(max_length=200)


    # This is the genre of the record, and links the record to the Genre model.
    genre = models.ForeignKey(
        Genre,
        # if the genre is deleted, the record is not deleted as well.
        on_delete=models.PROTECT,
        # the related_name allows the app to access records of a genre using
        # genre.records
        related_name='records'
    )
    label = models.CharField(max_length=200)
    format = models.CharField(max_length=50)
    description = models.TextField()

    # Decimal values have been used for the price to represent currency values.
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # Positive integer field for stock ensures that the number of records in
    # stock cannot be negative.
    stock = models.PositiveIntegerField(default=0)

    # Image field for the record's cover image, allows blank and null values in
    # case a record doesn't have an image. The values will be used to call the
    # image from Amazon AWS S3.
    image = models.ImageField(
        upload_to='records/',
        blank=True,
        null=True
    )
    # Indicates whether the record is active and should be displayed to users.
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.artist} - {self.title}'
