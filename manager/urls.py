from django.urls import path
from .views import (
    TableAndStudentView, TableCreateView, StudentCreateView, StudentUpdateView, StudentDeleteView, TableDeleteView, TableUpdateView, TruncateStudentsView, TruncateTablesView
)

urlpatterns = [
    path("", TableAndStudentView.as_view(), name="table_view"),

    # Table URLs
    path("tables/new/", TableCreateView.as_view(), name="table_create"),
    path("tables/<int:pk>/table/edit/",
         TableUpdateView.as_view(), name="table_update"),
    path("tables/<int:pk>/table/delete/",
         TableDeleteView.as_view(), name="table_delete"),

    # Student URLs (within a specific table)
    path("tables/<int:table_id>/students/add/",
         StudentCreateView.as_view(), name="student_create"),
    path("tables/<int:table_id>/students/<int:pk>/edit/",
         StudentUpdateView.as_view(), name="student_update"),
    path("tables/<int:table_id>/students/<int:pk>/delete/",
         StudentDeleteView.as_view(), name="student_delete"),

    # Truncate (bulk delete) URLs
    path("tables/tables/truncate/", TruncateTablesView.as_view(),
         name="truncate_tables"),
    path("tables/<int:table_id>/students/truncate/", TruncateStudentsView.as_view(),
         name="truncate_students"),
]
