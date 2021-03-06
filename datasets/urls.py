from django.urls import include, re_path
from datasets.views import *
from freesound_datasets.views import discussion


urlpatterns = [
    re_path(r'^save_contribute_validate_annotations_category/$', save_contribute_validate_annotations_category,
        name='save-contribute-validate-annotations-per-category'),
    re_path(r'^(?P<short_name>[^\/]+)/$', dataset, name='dataset'),
    re_path(r'^(?P<short_name>[^\/]+)/explore/$', dataset_explore, name='dataset-explore'),
    re_path(r'^(?P<short_name>[^\/]+)/download-script/$', download_script, name='download-script'),
    re_path(r'^(?P<short_name>[^\/]+)/discussion/', discussion, name='discussion'),
    re_path(r'^(?P<short_name>[^\/]+)/dataset-sounds/$', dataset_sounds, name='dataset-sounds'),
    re_path(r'^(?P<short_name>[^\/]+)/check_release_progresses/$', check_release_progresses, name='check-release-progresses'),
    re_path(r'^(?P<short_name>[^\/]+)/release/(?P<release_tag>[^\/]+)/$', change_release_type, name='change-release-type'),
    re_path(r'^(?P<short_name>[^\/]+)/release/(?P<release_tag>[^\/]+)/download/$', download_release, name='download-release'),
    re_path(r'^(?P<short_name>[^\/]+)/release/(?P<release_tag>[^\/]+)/delete/$', delete_release, name='delete-release'),
    re_path(r'^(?P<short_name>[^\/]+)/taxonomy_table/$', dataset_taxonomy_table, name='taxonomy-table'),
    re_path(r'^(?P<short_name>[^\/]+)/taxonomy_tree/$', dataset_taxonomy_tree, name='taxonomy-tree'),
    re_path(r'^(?P<short_name>[^\/]+)/releases_table/$', dataset_releases_table, name='releases-table'),
    re_path(r'^(?P<short_name>[^\/]+)/explore/(?P<node_id>[^\/]+)/$', taxonomy_node, name='dataset-explore-taxonomy-node'),
    re_path(r'^(?P<short_name>[^\/]+)/annotate/$', contribute, name='contribute'),
    re_path(r'^(?P<short_name>[^\/]+)/annotate/validate_annotations/$', contribute_validate_annotations,
        name='contribute-validate-annotations'),
    re_path(r'^(?P<short_name>[^\/]+)/annotate/validate_annotations/(?P<node_id>[^\/]+)/$',
        contribute_validate_annotations_category, name='contribute-validate-annotations-category'),
    re_path(r'^(?P<short_name>[^\/]+)/annotate/validate_annotations_beginner/$',
        contribute_validate_annotations_easy, name='contribute-validate-annotations-category-beginner'),
    re_path(r'^(?P<short_name>[^\/]+)/annotate/choose_category/$', choose_category, name='choose_category'),
    re_path(r'^(?P<short_name>[^\/]+)/annotate/choose_category_table/$', dataset_taxonomy_table_choose,
        name='dataset_taxonomy_table_choose'),
    re_path(r'^(?P<short_name>[^\/]+)/annotate/choose_category_table_search/$', dataset_taxonomy_table_search,
        name='taxonomy-table-search'),
    re_path(r'^(?P<short_name>[^\/]+)/annotate/validate_annotations_all/$', contribute_validate_annotations_all,
        name='contribute-validate-annotations-all'),
    re_path(r'^(?P<short_name>[^\/]+)/annotate/choose_category_table_search_all/$', dataset_taxonomy_table_search_all,
        name='taxonomy-table-search-all'),
    re_path(r'^(?P<short_name>[^\/]+)/mini-node-info/(?P<node_id>[^\/]+)/$', get_mini_node_info, name='get-mini-node-info'),
]
