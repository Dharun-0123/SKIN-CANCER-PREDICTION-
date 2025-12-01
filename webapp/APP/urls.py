from django.urls import path
from . import views

urlpatterns =[
    # Public pages
    path('', views.Landing_1, name='landing'),
    path('test/', views.test_view, name='test'),
    path('simple/', views.simple_test, name='simple'),
    path('minimal/', views.home_minimal, name='minimal'),
    path('register/', views.Register_2, name='register'),
    path('verify-email/', views.verify_email, name='verify_email'),
    path('resend-otp/', views.resend_otp_view, name='resend_otp'),
    path('login/', views.Login_3, name='login'),
    path('admin-login/', views.Admin_Login, name='admin_login'),
    path('logout/', views.Logout, name='logout'),
    
    # Protected pages (require login)
    path('home/', views.Home_4, name='home'),
    path('profile/', views.Profile, name='profile'),
    path('analytics/', views.Analytics, name='analytics'),
    path('compare/', views.Compare, name='compare'),
    path('dermagenie/', views.DermaGenie, name='dermagenie'),
    path('admin-dashboard/', views.AdminDashboard, name='admin_dashboard'),
    path('analyze/', views.Deploy_8, name='analyze'),
    path('history/', views.Out_Database_9, name='history'),
    path('about/', views.Teamates_5, name='about'),
    path('results/', views.Domain_Result_6, name='results'),
    path('problem/', views.Problem_Statement_7, name='problem'),
    
    # API endpoints
    path('compare/data/', views.CompareData, name='compare_data'),
    path('export/pdf/', views.ExportPDF, name='export_pdf'),
    path('export/pdf/<int:prediction_id>/', views.ExportSinglePDF, name='export_single_pdf'),
    path('dermagenie/chat/', views.DermaGenieChat, name='dermagenie_chat'),
    
    # Patient analysis
    path('patient/', views.input, name='patient'),
    path('patient/result/', views.patientResult, name='patient_result'),
    
    # Legacy URLs (for backward compatibility)
    path('Register_2/', views.Register_2, name='Register_2'),
    path('Login_3/', views.Login_3, name='Login_3'),
    path('Home_4/', views.Home_4, name='Home_4'),
    path('Teamates_5/', views.Teamates_5, name='Teamates_5'),
    path('Domain_Result_6/', views.Domain_Result_6, name='Domain_Result_6'),
    path('Problem_Statement_7/', views.Problem_Statement_7, name='Problem_Statement_7'),
    path('Deploy_8/', views.Deploy_8, name='Deploy_8'),
    path('Out_Database_9/', views.Out_Database_9, name='Out_Database_9'),
]