from django.contrib import admin

# Register your models here.

from .models import Tweet#,Choice

from import_export.admin import ImportExportModelAdmin

admin.site.site_header=" Admin Clasificacion de tweets"
admin.site.site_title=" Admin de tweets"
admin.site.index_header="Bienvenido Admin Clasificacion de tweets"





    


@admin.register(Tweet)


#admin.site.register(Tweet)
#admin.site.register(Choice)

class TweetAdmin(ImportExportModelAdmin):
    pass


#admin.site.register(Tweet, TweetAdmin)
