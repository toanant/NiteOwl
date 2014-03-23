from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    subcategory = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    publication_year = models.CharField(max_length=255)
    publishers = models.CharField(max_length=255)
    keywords = models.TextField()
    pages = models.IntegerField()
    image_url = models.URLField(blank=True)
    isbn_10 = models.IntegerField(max_length=10, blank=True)
    isbn_13 = models.IntegerField(max_length=13, blank=True)
    binding = models.CharField(max_length=255)
    description = models.TextField()
    # similar books

    def __unicode__(self):
        return self.title

class Price(models.Model):
    book = models.ForeignKey(Book)
    amazon = models.IntegerField(verbose_name="amazon books")
    kindle = models.IntegerField(verbose_name="amazon Kindle ebooks")
    flipkart = models.IntegerField(verbose_name="flipkart paper books")
    flipkart_ebooks = models.IntegerField()

    def minimum_price(self):
        minimum = sorted([self.amazon, self.kindle,
                         self.flipkart, self.flipkart_ebooks])[0]
        return minimum

    def __unicode__(self):
        return str(self.book.title)
