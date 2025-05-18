from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView,)

urlpatterns = [
    # User
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('me/', UserDetailView.as_view(), name='user_detail'),
    path('user/', UserListAPIView.as_view(), name='user_detail_admin'),
    path('userU/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('EmailUsed/', CheckEmail.as_view(), name='user_detail_admin'),
    path('UsernameUsed/', CheckUsername.as_view(), name='user_detail_admin'),
    path('SendVerifmail/', VerifyConfirmationCodeAPIView.as_view(), name='user_detail_admin'),

    # Worker
    path('Worker/Public/', WorkerListView.as_view(), name='worker-list'),
    path('Worker/New/', WorkerCreateView.as_view(), name='worker-create'),
    path('meWorker/', WorkerdetailView.as_view(), name='worker-retrieve-update-delete'),
    path('Worker/<int:pk>/Update/', WorkerUpdateView.as_view(), name='worker-retrieve-update-delete'),
    path('GettheseWorker/', GettheseWorkersApi),    
    # Rating Profile
    path('WorkerRateUser/<int:rater>/<int:worker>/<int:NewRate>/', RateWorkerApi),
    path('WorkerRateUser/<int:rater>/<int:worker>/', RateWorkerApi),
    path('WorkerRateUser/', RateWorkerApi),
    # Company
    path('Company/Public/', CompanyListView.as_view(), name='Company-list'),
    path('Company/New/', CompanyCreateView.as_view(), name='Company-create'),
    path('meCompany/', CompanydetailView.as_view(), name='Company-retrieve-update-delete'),
    path('Company/<int:pk>/Update/', CompanyUpdateView.as_view(), name='Company-retrieve-update-delete'),
    # LinksProfile
    path('LinksProfile/', LinksProfileListCreateView.as_view(),name='LinksProfile-list'),
    path('LinksProfile/<int:pk>/', LinksProfileRetrieveUpdateDeleteView.as_view(),name='LinksProfile-retrieve-update-delete'),
    # workerMaitrise
    path('workerMaitrise/', workerMaitriseListCreateView.as_view(),name='workerMaitrise-list-Create'),
    path('workerMaitrise/<int:pk>/', workerMaitriseRetrieveUpdateDeleteView.as_view(),name='workerMaitrise-retrieve-update-delete'),
    # Domaine
    path('Domaine/', DomaineListCreateView.as_view(),name='Domaine-list-Create'),
    path('Domaine/<int:pk>/', DomaineRetrieveUpdateDeleteView.as_view(),name='Domaine-retrieve-update-delete'),
    # SubDomain
    path('SubDomain/', SubDomainListCreateView.as_view(),name='SubDomain-list-Create'),
    path('SubDomain/<int:pk>/', SubDomainRetrieveUpdateDeleteView.as_view(),name='SubDomain-retrieve-update-delete'),
    # DomainUser
    path('DomainUser/', DomainUserListCreateView.as_view(),name='DomainUser-list-Create'),
    path('DomainUser/<int:pk>/', DomainUserRetrieveUpdateDeleteView.as_view(),name='DomainUser-retrieve-update-delete'),
    # Notification
    path('Notification/', NotificationListCreateView.as_view(),name='Notification-list-Create'),
    path('Notification/<int:pk>/', NotificationRetrieveUpdateDeleteView.as_view(),name='Notification-retrieve-update-delete'),
    # Notification_to
    path('Notification_to/', Notification_toListCreateView.as_view(),name='Notification_to-list-Create'),
    path('Notification_to/<int:pk>/', Notification_toRetrieveUpdateDeleteView.as_view(),name='Notification_to-retrieve-update-delete'),
    # Search
    path('Search/', SearchListCreateView.as_view(),name='Search-list-Create'),
    path('Search/<int:pk>/', SearchRetrieveUpdateDeleteView.as_view(),name='Search-retrieve-update-delete'),
    path('SearchGet/', SearchListView.as_view(),name='Search-retrieve-update-delete'),
    path('SearchWorker', SearchWorkersApi),
    path('SearchJob', SearchJobsApi),
    # InterestedJobs
    path('InterestedJobs/', InterestedJobsListCreateView.as_view(),name='InterestedJobs-list-Create'),
    path('InterestedJobs/<int:pk>/', InterestedJobsRetrieveUpdateDeleteView.as_view(),name='InterestedJobs-retrieve-update-delete'),
    # RateWorker
    path('RateWorker/', RateWorkerListCreateView.as_view(),name='RateWorker-list-Create'),
    path('RateWorker/<int:pk>/', RateWorkerRetrieveUpdateDeleteView.as_view(),name='RateWorker-retrieve-update-delete'),
    # Apply_For
    path('Apply_For/', Apply_ForListCreateView.as_view(),name='Apply_For-list-Create'),
    path('Apply_For/<int:pk>/', Apply_ForRetrieveUpdateDeleteView.as_view(),name='Apply_For-retrieve-update-delete'),
    # Software
    path('Software/', SoftwareListCreateView.as_view(),name='Software-list-Create'),
    path('Software/<int:pk>/', SoftwareRetrieveUpdateDeleteView.as_view(),name='Software-retrieve-update-delete'),
    path('SoftwareGET/', GETSoftwareApi),
    path('SoftwareGET/<int:id>', GETSoftwareApi),
    path('SoftwareProfile/<int:id>', ProfileSoftwareApi),
    path('IncrworkerSoftware/<int:id>', IncrworkerSoftware),
    # LinksSofware
    path('LinksSofware/', LinksSoftwareListCreateView.as_view(),name='LinksSofware-list-Create'),
    path('LinksSofware/<int:pk>/', LinksSoftwareRetrieveUpdateDeleteView.as_view(),name='LinksSofware-retrieve-update-delete'),
    # Image
    path('Image/', ImageListCreateView.as_view(),name='Image-list-Create'),
    path('Image/<int:pk>/', ImageRetrieveUpdateDeleteView.as_view(),name='Image-retrieve-update-delete'),
    # App_Tags
    path('App_Tags/', App_TagsListCreateView.as_view(),name='App_Tags-list-Create'),
    path('App_Tags/<int:pk>/', App_TagsRetrieveUpdateDeleteView.as_view(),name='App_Tags-retrieve-update-delete'),
    # HistorySoftware
    path('HistorySoftware/', HistorySoftwareListCreateView.as_view(),name='HistorySoftware-list-Create'),
    path('HistorySoftware/<int:pk>/', HistorySoftwareRetrieveUpdateDeleteView.as_view(),name='HistorySoftware-retrieve-update-delete'),
    # Tags
    path('Tags/', TagsListCreateView.as_view(),name='Tags-list-Create'),
    path('Tags/<int:pk>/', TagsRetrieveUpdateDeleteView.as_view(),name='Tags-retrieve-update-delete'),
    # Software_offer
    path('Software_offer/', Software_offerListCreateView.as_view(),name='Software_offer-list-Create'),
    path('Software_offer/<int:pk>/', Software_offerRetrieveUpdateDeleteView.as_view(),name='Software_offer-retrieve-update-delete'),
    # User_Offer
    path('User_Offer/', User_OfferListCreateView.as_view(),name='User_Offer-list-Create'),
    path('User_Offer/<int:pk>/', User_OfferRetrieveUpdateDeleteView.as_view(),name='User_Offer-retrieve-update-delete'),
    # relationships
    path('relationships/', relationshipsListCreateView.as_view(),name='relationships-list-Create'),
    path('relationships/<int:pk>/', relationshipsRetrieveUpdateDeleteView.as_view(),name='relationships-retrieve-update-delete'),
    # Externt_User_Download
    path('Externt_User_Download/', Externt_User_DownloadListCreateView.as_view(),name='Externt_User_Download-list-Create'),
    path('Externt_User_Download/<int:pk>/', Externt_User_DownloadRetrieveUpdateDeleteView.as_view(),name='Externt_User_Download-retrieve-update-delete'),
    # Externt_User_rating
    path('Externt_User_rating/', Externt_User_ratingListCreateView.as_view(),name='Externt_User_rating-list-Create'),
    path('Externt_User_rating/<int:pk>/', Externt_User_ratingRetrieveUpdateDeleteView.as_view(),name='Externt_User_rating-retrieve-update-delete'),
    # Project
    path('Project/', ProjectCreateView.as_view(),name='Project-Create'),
    path('ProjectGET/', ProjectListView.as_view(),name='Project-list'),
    path('Project/<int:pk>/', ProjectRetrieveUpdateDeleteView.as_view(),name='Project-retrieve-update-delete'),
    path('ProjectsWorkGET/<int:id>', WorkerJobsApi),
    # Skill
    path('Skill/', SkillListCreateView.as_view(),name='Skill-list-Create'),
    path('Skill/<int:pk>/', SkillRetrieveUpdateDeleteView.as_view(),name='Skill-retrieve-update-delete'),
    # Jobs
    path('Jobs/', JobsListCreateView.as_view(),name='Jobs-list-Create'),
    path('Jobs/<int:pk>/', JobsRetrieveUpdateDeleteView.as_view(),name='Jobs-retrieve-update-delete'),
    path('InterestedJobs/',InterestedJobsApi),
    path('InterestedJobs/<int:idWorker>/<int:idJob>/',InterestedJobsApi),
    path('PreposeJobs/',PreposeJobsApi),
    path('PreposeJobs/<int:idWorker>/',PreposeJobsApi),
    path('HistJobs/<int:idWorker>/',HistJobsApi),
    path('JobsGET', GETJobsApi),
    path('JobsProjectGET', GETProjefctJobsApi),
    # JobRequired
    path('JobRequired/', JobRequiredListCreateView.as_view(),name='JobRequired-list-Create'),
    path('JobRequired/<int:pk>/', JobRequiredRetrieveUpdateDeleteView.as_view(),name='JobRequired-retrieve-update-delete'),
    # ChatSession 
    path('ChatSession/', ChatSessionListCreateView.as_view(),name='ChatSession-list-Create'),
    path('ChatSession/<int:pk>/', ChatSessionRetrieveUpdateDeleteView.as_view(),name='ChatSession-retrieve-update-delete'),
    path('MyChatSession/', ChatSessionListView.as_view(),name='ChatSession-list-Create'),
    # Message_Bot
    path('Message_Bot/', Message_BotListCreateView.as_view(), name='Message_Bot-list-Create'),
    path('Message_Bot/<int:pk>/', Message_BotRetrieveUpdateDeleteView.as_view(), name='Message_Bot-retrieve-update-delete'),
    path('Message_BotGet/<int:pk>/', Message_BotListAPIView.as_view(), name='Message_Bot-retrieve'),
    # Software_recommandation
    path('Software_recommandation/', Software_recommandationListCreateView.as_view(),name='Software_recommandation-list-Create'),
    path('Software_recommandation/<int:pk>/', Software_recommandationRetrieveUpdateDeleteView.as_view(),name='Software_recommandation-retrieve-update-delete'),
    path('Software_recommandationADD/', SoftwareRecommandationView.as_view(), name='software-recommandation'),
    path('Software_recommandationGET/', SoftwareRecommandationView.as_view(), name='software-recommandation'),
    # User_Softwares
    path('User_Softwares/', User_SoftwaresListCreateView.as_view(),name='User_Softwares-list-Create'),
    path('User_Softwares/<int:pk>/', User_SoftwaresRetrieveUpdateDeleteView.as_view(),name='User_Softwares-retrieve-update-delete'),
    path('User_SoftwaresGet/<int:pk>/', User_SoftwaresListAPIView.as_view(), name='Message_Bot-retrieve'),

    # Dev_Offer
    path('Dev_Offer/', Dev_OfferListCreateView.as_view(),name='Dev_Offer-list-Create'),
    path('Dev_Offer/<int:pk>/', Dev_OfferRetrieveUpdateDeleteView.as_view(),name='Dev_Offer-retrieve-update-delete'),
    # Conversation
    path('Conversation/', ConversationListCreateView.as_view(),name='Conversation-list-Create'),
    path('Conversation/<int:pk>/', ConversationRetrieveUpdateDeleteView.as_view(),name='Conversation-retrieve-update-delete'),
    # Messages
    path('Messages/', MessagesListCreateView.as_view(),name='Messages-list-Create'),
    path('Messages/<int:pk>/', MessagesRetrieveUpdateDeleteView.as_view(),name='Messages-retrieve-update-delete'),

    # Statistics
    path('Stat/',GETStatApi),

    #RecSys
    path('SaveCsv',ExportDAtaCsv),
    path('PredictWorkers/<str:Profession>/', predictWorkers),
    path('PredictJobs/<str:Profession>/', predictJobs)

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
