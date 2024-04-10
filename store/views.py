from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction, IntegrityError
from store.models import Album, Artist, Contact, Booking

from .forms import ContactForm, ParagraphErrorList
def index(request):
   
    albums = Album.objects.filter(available=True).order_by('created_at')[:6]
    artists = Artist.objects.all().order_by('name')[:8]
    context = {
        'albums': albums,
        'artists': artists
    }
    return render(request, 'store/index.html', context)

#Affichage de tous les albums
def listing(request):
    #Get all albums
    albums_list = Album.objects.filter(available=True)
    paginator = Paginator(albums_list, 9)
    page = request.GET.get('page')
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        albums = paginator.page(1)
    except EmptyPage:
        albums = paginator.page(paginator.num_pages)
    context = {
        'albums': albums,
        'paginate': True,
        'list_title': "Tous nos disques"
    }
    return render(request, 'store/albumslisting.html', context)
#Affichage de tous les albums
def albumsartists(request):
    #Get all albums
    artists_listing = Artist.objects.all().order_by('name')
    paginator = Paginator(artists_listing, 9)
    page = request.GET.get('page')
    try:
        artists = paginator.page(page)
    except PageNotAnInteger:
        artists = paginator.page(1)
    except EmptyPage:
        artists = paginator.page(paginator.num_pages)
    context = {
        'artists': artists,
        'paginate': True,
        'list_title': "Profils de nos artistes"
    }
    return render(request, 'store/artists.html', context)
#Affichage d'un album par son identifiant avec possibilite de reserver
@transaction.atomic
def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    artists = [artist.name for artist in album.artists.all()]
    artists_name = " ".join(artists)
    context = {
        'album_title': album.title,
        'album_status': album.available,
        'artists_name': artists_name,
        'album_id': album.id,
        'thumbnail': album.picture
    }
    if request.method == 'POST':
        form = ContactForm(request.POST, error_class=ParagraphErrorList)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']

            try:
                with transaction.atomic():
                    contact = Contact.objects.filter(email=email)
                    if not contact.exists():
                        # If a contact is not registered, create a new one.
                        contact = Contact.objects.create(
                            email=email,
                            name=name
                        )
                    else:
                        contact = contact.first()

                    album = get_object_or_404(Album, id=album_id)
                    booking = Booking.objects.create(
                        contact=contact,
                        album=album
                    )
                    album.available = False
                    album.save()
                    context = {
                        'album_title': album.title
                    }
                    return render(request, 'store/merci.html', context)
            except IntegrityError:
                form.errors['internal'] = "Une erreur interne est apparue. Merci de recommencer votre requête."
    else:
        form = ContactForm()

    context['form'] = form
    context['errors'] = form.errors.items()
    return render(request, 'store/detail.html', context)
#icontains: permet de filtrer les albums sans tenir compte de la casse
def search(request):
    query =  request.GET.get('query')
    if not query:
        albums= Album.objects.all()
    else:
        albums = Album.objects.filter(title__icontains = query)
        if not albums.exists():
            albums = Album.objects.filter(artists__name__icontains = query)
 
    title="Résultat trouvé de la recherche sur la requête %s"%query   
    context = {
        'title':title,
        'albums':albums,
        }
    return render(request, 'store/search.html', context)
#Affichage des albums d'un artist pqr son id
def artist(request, artist_id):
    artist_info = get_object_or_404(Artist, pk=artist_id)
    artists_listing = Artist.objects.all()
    albums_listing = Album.objects.filter(artists__id__icontains = artist_id)
    artists_name = artist_info.name
    context = {
        'albums': albums_listing,
        'artists': artists_listing,
        'artist_name': artists_name,
        'list_title': "Tous les disques trouvés de %s" % artists_name
    }
    return render(request, 'store/artist.html', context)
#formulaire de contact
@transaction.atomic
def contact(request):
    context = {
        'title': "Contactez-nous!"
    }
    if request.method == 'POST':
        form = ContactForm(request.POST, error_class=ParagraphErrorList)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']

            try:
                with transaction.atomic():
                    contact = Contact.objects.filter(email=email)
                    if not contact.exists():
                        # If a contact is not registered, create a new one.
                        contactus = Contact.objects.create(
                            email=email,
                            name=name
                        )
                    else:
                        contact = contactus.first()
                    #contactus.save()
                    context = {
                        'title': "Nous contacter",
                        'body': "Merci pour votre message, vous serez contacter bientot!",
                        'contactname': name,
                        'contactemail': email
                    }
                    return render(request, 'store/contact.html', context)
            except IntegrityError:
                form.errors['internal'] = "Une erreur interne est apparue. Merci de recommencer votre requête."
    else:
        form = ContactForm()

    context['form'] = form
    context['errors'] = form.errors.items()
    return render(request, 'store/contact.html', context)
def about(request):
    
    context = {
        'title': "A propos de notre entreprise"
    }
    return render(request, 'store/about.html', context)
def page(request, namepage):
    
    context = {
        'title': namepage
    }
    return render(request, 'store/%s'%namepage%'.html', context)