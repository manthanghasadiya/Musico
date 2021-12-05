import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import userInfo, Song
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import userForm, userInfoForm, songForm
from twilio.rest import Client


# Spotify Secrets
cid = 'Spotify_cid'
secret = 'Spotify_secret'

# Twilio Secrets
account_sid = 'Twilio_screts'
auth_token = 'Twilio_token'


def home(request):
    return render(request, 'home.html')


def index(request):
    if request.method == 'POST':
        query = request.POST.get('search')

        client_credentials_manager = SpotifyClientCredentials(
            client_id=cid, client_secret=secret)

        sp = spotipy.Spotify(
            client_credentials_manager=client_credentials_manager)

        track_results = sp.search(q=query, type='track', limit=10)

        songs = []
        song_names = []
        release_dates = []
        artist_names = []
        images = []
       
        for i in range(10):
            songs.append(track_results['tracks']['items'][i]['preview_url'])
            song_names.append(track_results['tracks']['items'][i]['album']['name'])
            release_dates.append(track_results['tracks']['items'][i]['album']['release_date'])
            images.append(track_results['tracks']['items'][i]['album']['images'][0]['url'])

            artist = []
            number_artist = len(track_results['tracks']['items'][i]['album']['artists'])

            for j in range(number_artist):
                artist.append(track_results['tracks']['items'][i]['album']['artists'][j]['name'])

            artist_names.append(artist)
            
        songs = zip(songs, song_names, release_dates, artist_names, images)
        songs = list(songs)

        public_songs = []

        pubsong=Song.objects.all().filter(audio_type="Public")
        context = {
            'songs':songs,
        }

        return render(request, 'user/index.html', context)

    return render(request, 'index.html')


def signup(request):

    if request.method == 'POST':
        user_form = userForm(request.POST)
        user_info_form = userInfoForm(request.POST, request.FILES)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user
            user_info.save()

            login(request, user)

            return redirect('index')

        else:
            context = {
                'user_form.errors': user_form.errors, 'user_info_form.errors': user_info_form.errors,
                'user_form': user_form, 'user_info_form': user_info_form
            }
            return render(request, 'user/signup.html', context)

    else:
        user_form = userForm()
        user_info_form = userInfoForm()

        context = {'user_form': user_form, 'user_info_form': user_info_form}
        return render(request, 'user/signup.html', context)


def signin(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)

            user = request.user
            user = userInfo.objects.get(user=user)

            mobile_number = user.mobile_number

            client = Client(account_sid, auth_token)
            message = client.messages.create(  
                              body='Hello {}, you are successfully loggedin to Musicbuzz.'.format(username),
                              from_='+14582365794',
                              to='+91{}'.format(mobile_number)
            )

            return redirect('index')
        else:
            return redirect('signin')

    else:
        return render(request, 'login.html')


@login_required(login_url='error')
def signout(request):
    logout(request)
    return redirect('index')


@login_required(login_url='error')
def add_song(request):
    song_form = songForm()

    users = User.objects.all()

    user = request.user
    user = userInfo.objects.get(user=user)

    chk = user.verified

    if request.method == "POST":
        song_form = songForm(request.POST, request.FILES)


        if song_form.is_valid():
            song_form.user = request.user
            song_form.save()

            return redirect('index')

        else:
            context = {
                'song_form': song_form, 'song_form.errors': song_form.errors, 'chk': chk
            }

            return render(request, 'song/add_song.html', context)

    context = {'song_form': song_form, 'chk':chk}
    return render(request, 'song/add_song.html', context)

def public_song(request):

    pub_song=Song.objects.filter(audio_type='Public').order_by('-audio_file')
    context={'pub_song': pub_song}
    return render(request,"song/public_song.html",context)

def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def elements(request):
    return render(request, 'elements.html')


def track(request):
    return render(request, 'track.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

# def indexout(request):
#     return render(request, 'index.html')


def loginnew(request):
    return render(request, 'login.html')


def albumsstore(request):
    return render(request, 'albumsstore.html')

def error(request):
    return render(request, 'error.html')


@login_required(login_url='error')
def my_song(request):
    my_songs = Song.objects.filter(user=request.user)

    context = {
        'my_songs':my_songs
    }

    return render(request, 'song/my_song.html', context)


@login_required(login_url='error')
def verify(request):

    user = request.user
    user = userInfo.objects.get(user=user)

    mobile_number = user.mobile_number

    if request.method == 'POST':
        call = request.POST.get('call')
        sms = request.POST.get('sms')
        client = Client(account_sid, auth_token)

        if call:
            verification = client.verify \
                .services('Service_number') \
                .verifications \
                .create(to='+91 {}'.format(mobile_number), channel='call')

        else:
            verification = client.verify \
                .services('Service_number') \
                .verifications \
                .create(to='+91 {}'.format(mobile_number), channel='sms')

        return redirect('check_otp')
    context = {
        'mobile_number': mobile_number[8:]
    }

    return render(request, 'verify.html', context)


@login_required(login_url='error')
def check_otp(request):

    user = request.user
    user = userInfo.objects.get(user=user)

    

    mobile_number = user.mobile_number

    if request.method == 'POST':
        otp = request.POST.get('otp')
        client = Client(account_sid, auth_token)

        verification_check = client.verify \
            .services('Service_number') \
            .verification_checks \
            .create(to='+91 {}'.format(mobile_number), code=otp)


        if verification_check.status == 'approved':
            user.verified = True
            user.save()
            return render(request, 'success.html')

    return render(request, 'check_otp.html')