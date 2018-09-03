
import xadmin as admin
from myApp.models import Tag, Category, Novels, RollSet, Chapter
from xadmin import views



class BaseSettings:
    enable_themes = True
    ues_bootswatch = True
    menu_style = 'accordion'


class GlobalSettings:
    site_title = '小说'
    site_footer = '小说大联盟'
    menu_style = 'accordion'
    search_models = [Tag]
    apps_label_title = {
        'art': '文章管理'   # 应用名：'应用标题'
    }
    apps_icons = {
        'art': 'glyphicon glyphicon-book'
    }
    global_models_icon = {
        Tag: 'glyphicon glyphicon-tags'
    }


admin.site.register(views.BaseAdminView, BaseSettings)


admin.site.register(views.CommAdminView, GlobalSettings)


class TagAdmin:
    list_display = ('name', 'describe', 'add_time') # 列表展示
    list_per_page = 10
    search_fields = ('name', 'describe')


admin.site.register(Tag, TagAdmin)


class CategoryAdmin:
    list_display = ('title', 'add_time') # 列表展示
    list_per_page = 10


admin.site.register(Category, CategoryAdmin)


class NovelAdmin:
    list_display = ('n_title', 'author', 'content', 'icon') # 列表展示
    list_per_page = 10


admin.site.register(Novels, NovelAdmin)


class RollSetAdmin:
    list_display = ('name', 'free_level') # 列表展示
    list_per_page = 10


admin.site.register(RollSet, RollSetAdmin)


class ChapterAdmin:
    list_display = ('name', 'content', 'publish_time') # 列表展示
    list_per_page = 10
    #设置制定字段的样式
    style_fields = {'content': 'ueditor'}


admin.site.register(Chapter, ChapterAdmin)



