from manager.models import Table, Student
from django.views import View
from django.urls import reverse
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Student, Table
from .forms import StudentForm, TableForm

# Create your views here.


# -------------------- TABLE VIEWS --------------------


class TableAndStudentView(ListView):
    model = Table
    template_name = "table_view.html"
    context_object_name = "tables"

    def get_queryset(self):
        return Table.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        table_id = self.request.GET.get("table_id")
        selected_table = get_object_or_404(
            Table, id=table_id) if table_id else None
        students = selected_table.students.all() if selected_table else None

        context["selected_table"] = selected_table
        context["students"] = students
        return context

    def get(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            table_id = request.GET.get('table_id')
            query = request.GET.get('q', '').strip()

            selected_table = get_object_or_404(Table, id=table_id)
            students = selected_table.students.all()

            if query:
                students = students.filter(name__icontains=query)

            students_list = list(students.values('student_id', 'first_name', 'last_name', 'email', 'date_of_birth', 'course', 'enrollment_date'))
            return JsonResponse({'students': students_list})

        return super().get(request, *args, **kwargs)


class TableCreateView(CreateView):
    model = Table
    form_class = TableForm
    template_name = "table_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tables"] = Table.objects.all()
        return context

    def get_success_url(self):
        return reverse("table_view") + f"?table_id={self.object.id}"


class TableUpdateView(UpdateView):
    model = Table
    form_class = TableForm
    template_name = "table_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tables"] = Table.objects.all()
        context["selected_table"] = get_object_or_404(
            Table, id=self.kwargs["pk"])
        return context

    def get_success_url(self):
        return reverse("table_view") + f"?table_id={self.object.id}"


class TableDeleteView(DeleteView):
    model = Table
    template_name = "confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tables"] = Table.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            table_id = self.kwargs.get("table_id", self.get_object().id)
            return redirect(reverse("table_view") + f"?table_id={table_id}")

        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("table_view")

# -------------------- STUDENT VIEWS --------------------


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"

    def form_valid(self, form):
        table_id = self.kwargs.get("table_id")
        print("POST Data:", self.request.POST)  # Debugging
        print("Table ID:", table_id)  # Debugging
        if not table_id:
            return self.form_invalid(form)  # Handle error gracefully

        form.instance.table = get_object_or_404(Table, id=table_id)
        print(f"DEBUG: Retrieved Table Instance → {form.instance.table}")
        print("DEBUG: Table instance set on form →", form.instance.table)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("DEBUG: Form validation failed. Errors →", form.errors)  # Check for issues
        return super().form_invalid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table_id = self.kwargs.get("table_id")
        if table_id:
            context["selected_table"] = get_object_or_404(Table, id=table_id)
        else:
            context["selected_table"] = None
        context["tables"] = Table.objects.all()
        return context


    def get_success_url(self):
        return reverse("table_view") + f"?table_id={self.kwargs['table_id']}"


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"

    def form_valid(self, form):
        form.instance.table = get_object_or_404(
            Table, id=self.kwargs["table_id"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tables"] = Table.objects.all()
        context["selected_table"] = get_object_or_404(
            Table, id=self.kwargs["table_id"])
        return context

    def get_success_url(self):
        return reverse("table_view") + f"?table_id={self.kwargs['table_id']}"


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tables"] = Table.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            table_id = self.kwargs.get("table_id", self.get_object().table.id)
            return redirect(reverse("table_view") + f"?table_id={table_id}")

        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("table_view") + f"?table_id={self.kwargs['table_id']}"


# -------------------- TRUNCATE VIEWS --------------------


class TruncateTablesView(View):
    template_name = "confirm_truncate.html"
    success_url = reverse_lazy("table_view")

    def get(self, request, *args, **kwargs):
        context = {
            "object_type": "tables",
            "tables": Table.objects.all()
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect(self.success_url)

        Table.objects.all().delete()
        return redirect(self.success_url)


class TruncateStudentsView(View):
    template_name = "confirm_truncate.html"

    def get(self, request, *args, **kwargs):
        table_id = self.kwargs["table_id"]
        table = get_object_or_404(Table, id=table_id)
        context = {
            "object_type": "students",
            "table": table,
            "students": table.students.all()
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        table_id = self.kwargs["table_id"]
        table = get_object_or_404(Table, id=table_id)

        if "cancel" in request.POST:
            return redirect(reverse("table_view") + f"?table_id={table_id}")

        if "students" in request.POST:
            table.students.all().delete()
            return redirect(reverse("table_view") + f"?table_id={table_id}")

        return redirect(reverse("table_view") + f"?table_id={table_id}")
