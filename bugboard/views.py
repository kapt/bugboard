from django.views import generic
from django.db.models import Max
from bugboard.models import Task
from bugboard.models import Project


class UnnassignedView(generic.ListView):
    template_name = 'bugboard/task_list.html'
    queryset = Task.objects.filter(assignee=None).order_by('-created_at')
    paginate_by = 100

    def get_ordering(self):
        return self.request.GET.get('order', '-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_tasks"] = Task.objects.all().count()
        context["total_projects"] = Project.objects.all().count()
        return context


class ByMemberView(generic.ListView):
    template_name = 'bugboard/task_list.html'
    paginate_by = 100

    def get_ordering(self):
        return self.request.GET.get('order', '-created_at')

    def get_queryset(self):
        # ordering is called inside this function, so call it here
        ordering = self.get_ordering()
        # get correct kapt email from id
        email = str(self.request.GET.get('id', 'ad')) + "@kapt.mobi"

        # return custom queryset
        return Task.objects.filter(assignee__email=email).order_by(ordering)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_tasks"] = Task.objects.all().count()
        context["total_projects"] = Project.objects.all().count()
        return context


class CommentedView(generic.ListView):
    template_name = 'bugboard/task_list.html'
    paginate_by = 100

    queryset = Task.objects.exclude(
        comment=None
    ).annotate(
        last_com=Max(
            'comment__created_at'
        )
    ).order_by(
        '-last_com'
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_tasks"] = Task.objects.all().count()
        context["total_projects"] = Project.objects.all().count()
        return context


class CreatedView(generic.ListView):
    template_name = 'bugboard/task_list.html'
    queryset = Task.objects.all()
    paginate_by = 100

    # set ordering based on the ?order=PARAM parameter, set -created_at if there is no get
    def get_ordering(self):
        return self.request.GET.get('order', '-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_tasks"] = Task.objects.all().count()
        context["total_projects"] = Project.objects.all().count()
        return context


class AllView(generic.ListView):
    queryset = Task.objects.all()

    def get_ordering(self):
        return self.request.GET.get('order', '-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_tasks"] = Task.objects.all().count()
        context["total_projects"] = Project.objects.all().count()
        return context
