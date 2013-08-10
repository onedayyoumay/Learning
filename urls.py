from django.conf.urls.defaults import patterns, include, url
from django.contrib.comments.views.comments import post_comment, comment_done
import settings
from urlmiddleware.conf import middleware, mpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
middlewarepatterns = mpatterns('',
    middleware(r'^students/', 'mysite.students.middlewares.CoolMiddleware',),
)
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    (r'^$', 'mysite.core.views.index'),
    url(r'^blog/view/(?P<slug>[^\.]+).html', 'mysite.core.views.view_post', name='view_blog_post'),
    url(r'^blog/category/(?P<slug>[^\.]+).html', 'mysite.core.views.view_category', name='view_blog_category'),
    url(r'^comments/post/$', post_comment, name='comments-post-comment'),
    url(r'^comments/posted/$', comment_done, name='comments-comment-done'),
    url(r'^tasks/$', 'mysite.todo.views.task', name='task1'),
    url(r'^tasks/add/', 'mysite.todo.views.addtask', name='addtask1'),
    url(r'^tasks/finish/', 'mysite.todo.views.finishtask', name='finishtask1'),
    url(r'^students/$', 'mysite.students.views.groups', name='groups'),
    url(r'^students/getgroup/$', 'mysite.students.views.group_info', name='group_info'),
    url(r'^login/$', 'mysite.students.views.auth', name='auth'),
    url(r'^students/delete/$', 'mysite.students.views.delete', name='delete'),
    url(r'^students/add_group/', 'mysite.students.views.new_group', name='new_group'),
    url(r'^students/add_student/', 'mysite.students.views.new_student', name='new_student'),
    url(r'^students/getgroup/m_student/$', 'mysite.students.views.manage_student', name='m_student'),
    url(r'^students/m_group/$', 'mysite.students.views.manage_group', name='m_group'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True}),
)