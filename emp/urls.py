from django.urls import path
from . import views
urlpatterns = [
    # Authentication Routes
    path('', views.admin_login, name='admin_login'),
    path('logout/', views.admin_logout, name='admin_logout'),






    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Employee Management
    path('add/', views.add_employee, name='add_employee'),
    path('all-employees/', views.all_employees, name='all_employees'),
    path('edit/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),

    # Attendance
    path('scan/', views.scan_view, name='scan'),
    path('view/<int:employee_id>/', views.view_employee_attendance, name='view_employee_attendance'),

    # Advance Payment
    path('payment/<int:employee_id>/', views.advance_payment, name='advance_payment'),
    path('merge-advances/<int:employee_id>/', views.merge_advances, name='merge_advances'),


    # Download
    path("download-attendance/", views.download_attendance, name="download_attendance"),
]
