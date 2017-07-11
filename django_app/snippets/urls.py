from django.conf.urls import url, include
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'snippet', views.SnippetViewSet)
# router.register(r'comment', views.CommentViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),

    # url(r'^$', views.SnippetList.as_view(), name='snippet-list'),
    # url(r'^(?P<pk>\d+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
    # url(r'^(?P<pk>\d+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),

    # url(r'^$',
    #     views.SnippetViewSet.as_view({
    #         'get': 'list',
    #         'post': 'create'
    #     }),
    #     name='snippet-list'),
    # url(r'^(?P<pk>\d+)/$',
    #     views.SnippetViewSet.as_view({
    #         'get': 'retrieve',
    #         'put': 'update',
    #         'patch': 'partial_update',
    #         'delete': 'destroy'
    #     }),
    #     name='snippet-detail'),
    # url(r'^(?P<pk>\d+)/highlight/$',
    #     views.SnippetViewSet.as_view({
    #         'get': 'highlight',
    #     }, renderer_classes=[renderers.StaticHTMLRenderer,]),
    #     name='snippet-highlight'),
]
