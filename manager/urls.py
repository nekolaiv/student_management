from django.urls import path
from .views import (
    TableAndItemView, TableCreateView, ItemCreateView, ItemUpdateView, ItemDeleteView, TableDeleteView, TableUpdateView, TruncateItemsView, TruncateTablesView
)

urlpatterns = [
    path("", TableAndItemView.as_view(), name="table_view"),

    # Table URLs
    path("tables/new/", TableCreateView.as_view(), name="table_create"),
    path("tables/<int:pk>/table/edit/",
         TableUpdateView.as_view(), name="table_update"),
    path("tables/<int:pk>/table/delete/",
         TableDeleteView.as_view(), name="table_delete"),

    # Item URLs (within a specific table)
    path("tables/<int:table_id>/items/add/",
         ItemCreateView.as_view(), name="item_create"),
    path("tables/<int:table_id>/items/<int:pk>/edit/",
         ItemUpdateView.as_view(), name="item_update"),
    path("tables/<int:table_id>/items/<int:pk>/delete/",
         ItemDeleteView.as_view(), name="item_delete"),

    # Truncate (bulk delete) URLs
    path("tables/tables/truncate/", TruncateTablesView.as_view(),
         name="truncate_tables"),  # Delete all tables
    path("tables/<int:table_id>/items/truncate/", TruncateItemsView.as_view(),
         name="truncate_items"),  # Delete all items in a table
]
