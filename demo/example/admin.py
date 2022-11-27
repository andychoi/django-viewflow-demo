from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(DailyTimesheetApproval)
class DailyTimesheetApprovalAdmin(admin.ModelAdmin):
    pass

@admin.register(DailyTimesheet)
class DailyTimesheetAdmin(admin.ModelAdmin):
    pass


@admin.register(Vacation)
class VacationAdmin(admin.ModelAdmin):
    pass

@admin.register(VacationApproval)
class VacationApprovalAdmin(admin.ModelAdmin):
    pass
