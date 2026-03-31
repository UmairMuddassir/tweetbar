from django.contrib import admin
from .models import Tweet, Like


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'created_at', 'like_count')
    list_filter = ('created_at', 'user')
    search_fields = ('text', 'user__username')
    readonly_fields = ('created_at', 'updated_at')

    def like_count(self, obj):
        return obj.likes.count()
    like_count.short_description = 'Likes'


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'tweet', 'created_at')
    list_filter = ('created_at',)
