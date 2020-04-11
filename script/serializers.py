from rest_framework import serializers
from .models import Chapter, Verse, Book

class BookSerializer(serializers.HyperlinkedModelSerializer):
    chapters = serializers.HyperlinkedRelatedField(
        view_name='chapter_detail',
        many=True,
        read_only=True
    )
    book_url = serializers.ModelSerializer.serializer_url_field(
        view_name='book_detail'
    )
    class Meta:
        model = Book
        fields = ('id', 'book_url', 'version', 'book_num', 'book', 'description', 'image_url', 'chapters',)

class ChapterSerializer(serializers.HyperlinkedModelSerializer):
    book = serializers.HyperlinkedRelatedField(
        view_name='book_detail',
        read_only=True
    )
    verses = serializers.HyperlinkedRelatedField(
        view_name='verse_detail',
        many=True,
        read_only=True
    )
    chapter_url = serializers.ModelSerializer.serializer_url_field(
        view_name='chapter_detail'
    )
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Chapter
        fields = ('id', 'chapter_url', 'book', 'chapter_num', 'chapter', 'description', 'image_url', 'verses',)

class VerseSerializer(serializers.HyperlinkedModelSerializer):
    chapter = serializers.HyperlinkedRelatedField(
        view_name='chapter_detail',
        read_only=True
    )
    verse_url = serializers.ModelSerializer.serializer_url_field(
        view_name='verse_detail'
    )
    class Meta:
        model = Verse
        fields = ('id', 'verse_url', 'verse_num', 'verse', 'image_url', 'chapter',)


