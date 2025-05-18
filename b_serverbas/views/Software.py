from rest_framework.permissions import IsAuthenticated
from ..permissions import *
from ..serializers import *
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import JSONParser
from django.db.models import Q
from django.core.paginator import Paginator

# Software
class SoftwareListCreateView(ListCreateAPIView):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

class SoftwareRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

# LinksSoftware
class LinksSoftwareListCreateView(ListCreateAPIView):
    queryset = LinksSoftware.objects.all()
    serializer_class = LinksSoftwareSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

class LinksSoftwareRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = LinksSoftware.objects.all()
    serializer_class = LinksSoftwareSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

 # Image
class ImageListCreateView(ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

class ImageRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]
# App_Tags
class App_TagsListCreateView(ListCreateAPIView):
    queryset = App_Tags.objects.all()
    serializer_class = App_TagsSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

class App_TagsRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = App_Tags.objects.all()
    serializer_class = App_TagsSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]
# HistorySoftware
class HistorySoftwareListCreateView(ListCreateAPIView):
    queryset = HistorySoftware.objects.all()
    serializer_class = HistorySoftwareSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

class HistorySoftwareRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = HistorySoftware.objects.all()
    serializer_class = HistorySoftwareSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]
# Tags
class TagsListCreateView(ListCreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

class TagsRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]
# Software_offer
class Software_offerListCreateView(ListCreateAPIView):
    queryset = Software_offer.objects.all()
    serializer_class = Software_offerSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

class Software_offerRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Software_offer.objects.all()
    serializer_class = Software_offerSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]
# User_Offer
class User_OfferListCreateView(ListCreateAPIView):
    queryset = User_Offer.objects.all()
    serializer_class = User_OfferSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

class User_OfferRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = User_Offer.objects.all()
    serializer_class = User_OfferSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]
# relationships
class relationshipsListCreateView(ListCreateAPIView):
    queryset = relationships.objects.all()
    serializer_class = relationshipsSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

class relationshipsRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = relationships.objects.all()
    serializer_class = relationshipsSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]
# Externt_User_Download
class Externt_User_DownloadListCreateView(ListCreateAPIView):
    queryset = Externt_User_Download.objects.all()
    serializer_class = Externt_User_DownloadSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

class Externt_User_DownloadRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Externt_User_Download.objects.all()
    serializer_class = Externt_User_DownloadSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]
# Externt_User_rating
class Externt_User_ratingListCreateView(ListCreateAPIView):
    queryset = Externt_User_rating.objects.all()
    serializer_class = Externt_User_ratingSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

class Externt_User_ratingRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Externt_User_rating.objects.all()
    serializer_class = Externt_User_ratingSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]  


@csrf_exempt
def GETSoftwareApi(request, id=0):
    if request.method == 'GET':
        try:
            Soft = Software.objects.get(id=id)
            serializer = SoftwareSerializerPlus(Soft)
            similar_Softwares = get_similar_Softwares(Soft)
            serializer_similar_Softwares = SoftwareSerializerMoin(similar_Softwares, many=True)

            Images = Image.objects.filter(Software=id)
            serializerImages = ImageSerializer(Images, many=True)
            Links = LinksSoftware.objects.filter(Software=id)
            serializerLinks = LinksSoftwareSerializer(Links, many=True)
            History = HistorySoftware.objects.filter(Software=id,Rating__gt=0)
            rating_counts = [0, 0, 0, 0, 0]
            for i in range(1, 6):
                count = History.filter(Rating=i).count()
                rating_counts[i-1] = count
            reviews = HistorySoftware.objects.filter(Software=id,Rating__gt=0).exclude(Content='').order_by('-date')[:5]
            serializerreviews = HistorySoftwareSerializerPlus(reviews, many=True)
            tags = Tags.objects.filter(Software=id)
            serializerTags = TagsSerializerPlus(tags, many=True)
            offer = Software_offer.objects.filter(Software=id)
            serializeroffers = Software_offerSerializer(offer, many=True)
            return JsonResponse({"data": serializer.data,
                                 "Images":serializerImages.data,
                                 "LinksSoftware":serializerLinks.data,
                                 "rating_counts":rating_counts,
                                 "reviews":serializerreviews.data,
                                 "Tags":serializerTags.data,
                                 "offers":serializeroffers.data,
                                 "similar_Softwares": serializer_similar_Softwares.data,  # Include similar Softwares
                                 "found": True})
        except ObjectDoesNotExist:
            return JsonResponse({"found": False, "message": "Software not found"})
    if request.method == 'Software':
        data = JSONParser().parse(request)
        Softwares_required = Software.objects.all().order_by('-Rating', '-date')
        search = data.get('search', '')
        CtegorieList = data.get('CtegorieList', [])
        TypeList = data.get('TypeList', [])
        SepecialList = data.get('SepecialList', [])
        page_number = data.get('Page', 1)

        if search:
            Softwares_required = Softwares_required.filter(
                Q(Title__icontains=search) |
                Q(Description__icontains=search) |
                Q(Type__icontains=search) |
                Q(Categorie__icontains=search) |
                Q(Special__icontains=search)
            )
        if CtegorieList:
            categorie_filters = Q()
            for category in CtegorieList:
                categorie_filters |= Q(Categorie__icontains=category.strip())
            Softwares_required = Softwares_required.filter(categorie_filters)

        if TypeList:
            type_filters = Q()
            for Software_type in TypeList:
                type_filters |= Q(Type__icontains=Software_type.strip())
            Softwares_required = Softwares_required.filter(type_filters)
        if SepecialList:
            Special_filters = Q()
            for Software_Special in SepecialList:
                Special_filters |= Q(Special__icontains=Software_Special.strip())
            Softwares_required = Softwares_required.filter(Special_filters)

        Softwares_per_page = 9
        paginator = Paginator(Softwares_required, Softwares_per_page)
        try:
            page_number = int(page_number)
        except ValueError:
            page_number = 1

        page_Softwares = paginator.get_page(page_number)
        serializer = SoftwareSerializerMoin(page_Softwares, many=True)

        return JsonResponse({
            'page_number': page_Softwares.number,
            'total_pages': paginator.num_pages,
            'Softwares': serializer.data
        })   

def get_similar_Softwares(Software):
    similar_Softwares = Software.objects.filter(
        Q(Categorie__icontains=Software.Categorie) | 
        Q(Type__icontains=Software.Type)  
    ).exclude(id=Software.id).order_by('-Rating')[:5] 
    return similar_Softwares
@csrf_exempt
def IncrworkerSoftware(request,id):
    worker = Worker.objects.get(id=id)
    worker.Nbr_Software += 1
    worker.save()
    return JsonResponse('updated', safe=False)
@csrf_exempt
def ProfileSoftwareApi(request, id=0):
    if request.method == 'GET':
        Softwares = Software.objects.filter(By=id).order_by('-Rating', '-date')
        serializer = SoftwareSerializer(Softwares, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def HistSoftwareApi(request): # Software
    if request.method == 'Software':
        data = JSONParser().parse(request)

        rater_user = User.objects.get(id=data['User'])
        Software = Software.objects.get(id=data['Software'])
        Save = data['Save']
        Rating = data['Rate']
        Content = data['Content']
        date = data['date']
        HistSoftware, created = HistorySoftware.objects.get_or_create(User=rater_user, Software=Software)
        if created:
            HistSoftware.Save = False
            HistSoftware.Rating=0
            if Save == 1:
                HistSoftware.Save = True
            if Rating !=0:
                Software.Rating = ((Software.Rating * Software.Nbr_Rating) + Rating) / (Software.Nbr_Rating + 1)
                Software.Nbr_Rating += 1
                HistSoftware.Content = Content
                HistSoftware.Rating = Rating
                HistSoftware.date = date
        else:
            if Save == 1:
                HistSoftware.Save = (not HistSoftware.Save)
            if Rating !=0:
                if HistSoftware.Rating==0:
                    print((Software))
                    print(( Rating))
                    print((Software.Nbr_Rating + 1))
                    Software.Rating = ((Software.Rating * Software.Nbr_Rating) + Rating) / (Software.Nbr_Rating + 1)
                    Software.Nbr_Rating += 1
                else:
                    print((Software.Rating*Software.Nbr_Rating))
                    print(Rating-HistSoftware.Rating)
                    print((Software.Nbr_Rating))
                    Software.Rating = ((Software.Rating*Software.Nbr_Rating)+Rating-HistSoftware.Rating)/(Software.Nbr_Rating)
                HistSoftware.Content = Content
                HistSoftware.Rating = Rating
                HistSoftware.date = date
        HistSoftware.save()
        Software.Rating = round(Software.Rating, 1)
        Software.save()
        serializerHistSoftware = HistorySoftwareSerializerPlus(HistSoftware)
        serializerSoftware = SoftwareSerializerPlus(Software)

        rating_counts = [0, 0, 0, 0, 0]
        reviews = []
        offer = Software_offer.objects.filter(Software = data['Software'])
        User_offer = User_Offer.objects.filter(offers__in=offer,User = data['User'])
        serializerUser_offer = User_OfferSerializer(User_offer, many=True)
        if Rating !=0:
            History = HistorySoftware.objects.filter(Software=data['Software'],Rating__gt=0)
            for i in range(1, 6):
                count = History.filter(Rating=i).count()
                rating_counts[i-1] = count
            reviews = HistorySoftware.objects.filter(Software=data['Software'],Rating__gt=0).exclude(Content='').order_by('-date')[:5]
            serializerreviews = HistorySoftwareSerializerPlus(reviews, many=True)
            reviews = serializerreviews.data

        return JsonResponse({"UserRate":serializerHistSoftware.data,
                             "User_offer":serializerUser_offer.data,
                             "Software":serializerSoftware.data,
                             "rating_counts":rating_counts,
                             "reviews":reviews,})
