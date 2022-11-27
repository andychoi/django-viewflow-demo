from viewflow.flow.viewset import FlowViewSet

from django.urls import path, re_path, include

from . import views
from .flows import DailyTimesheetApprovalFlow, VacationApprovalFlow

from typing import NamedTuple
class NamedURL(NamedTuple):
    urlconf_module: None
    app_name: None

app_name = "example"
sheet_urls = NamedURL(FlowViewSet(DailyTimesheetApprovalFlow).urls, "example")
vacation_urls = NamedURL(FlowViewSet(VacationApprovalFlow).urls, "example")


urlpatterns = [
    re_path(r'^$', views.home, name='index'),
    re_path(r'^fast_login$', views.fast_login, name='fast_login'),
    re_path(r'^fast_logout$', views.fast_logout, name='fast_logout'),
    re_path(r'^timesheet$', views.DailyTimesheetListView.as_view(),
        name='timesheets'),
    re_path(r'^vacation$', views.VacationListView.as_view(),
        name='vacations'),

    re_path(r'^task/completed/$', views.CompletedTaskListView.as_view(),
        name='tasks_completed'),

    re_path(r'^task/in_progress/$', views.InProgressTaskListView.as_view(),
        name='tasks_in_progress'),

    re_path(r'^task/unassigned/$', views.UnassignedTaskListView.as_view(),
        name='tasks_unassigned'),

    re_path(r'^process$', views.ProcessListView.as_view(),
        name='processes'),
    re_path(r'^process_classes$', views.ProcessClassesListView.as_view(),
        name='process_classes'),

    re_path(r'^daily/', include(sheet_urls, namespace='daily')),
    re_path(r'^vacation/', include(vacation_urls, namespace='vacation')),

]
