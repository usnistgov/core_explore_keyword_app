""" Url router for administration views
"""
from django.contrib import admin
from django.urls import re_path

from core_explore_keyword_app.views.admin import views as admin_views
from core_explore_keyword_app.views.admin import ajax as admin_ajax

admin_urls = [
    re_path(r"^operators/$",
            admin_views.ListSearchOperatorsView.as_view(),
            name="core_explore_keyword_app_list_search_operators"),
    re_path(r"^operators/edit$",
            admin_ajax.SearchOperatorConfigModalView.as_view(),
            name="core_explore_keyword_app_search_operator_config_modal"),
    re_path(r"^operators/delete$",
            admin_ajax.SearchOperatorDeleteModalView.as_view(),
            name="core_explore_keyword_app_search_operator_delete_modal")
]

urls = admin.site.get_urls()
admin.site.get_urls = lambda: admin_urls + urls
