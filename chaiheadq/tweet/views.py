from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Count, Q
from .models import Tweet, Like
from .forms import TweetForm, UserRegistrationForm


# ─── Home / Landing ──────────────────────────────────────────────────────────

def index(request):
    if request.user.is_authenticated:
        return redirect('tweet_list')
    return render(request, 'index.html')


# ─── Auth ────────────────────────────────────────────────────────────────────

def register(request):
    if request.user.is_authenticated:
        return redirect('tweet_list')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, f'Welcome to TweetBar, @{user.username}! 🎉')
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('tweet_list')
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, f'Welcome back, @{user.username}!')
            next_url = request.GET.get('next', 'tweet_list')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    return render(request, 'login.html')


def user_logout(request):
    auth_logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('index')


# ─── Tweet Feed ───────────────────────────────────────────────────────────────

def tweet_list(request):
    tweets = Tweet.objects.annotate(
        like_count=Count('likes', distinct=True)
    ).order_by('-created_at')

    liked_ids = set()
    if request.user.is_authenticated:
        liked_ids = set(Like.objects.filter(user=request.user).values_list('tweet_id', flat=True))

    return render(request, 'tweet_list.html', {
        'tweets': tweets,
        'liked_ids': liked_ids,
    })


# ─── Create / Edit / Delete ───────────────────────────────────────────────────

@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()                          # ← bug fix: was form.save()
            messages.success(request, 'Tweet posted! ✅')
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form, 'action': 'Create'})


@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()                          # ← bug fix: was form.save()
            messages.success(request, 'Tweet updated! ✅')
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form, 'action': 'Edit'})


@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        messages.success(request, 'Tweet deleted.')
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})


# ─── Like (toggle) ───────────────────────────────────────────────────────────

@login_required
def tweet_like(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    like, created = Like.objects.get_or_create(user=request.user, tweet=tweet)
    if not created:
        like.delete()
    return redirect(request.META.get('HTTP_REFERER', 'tweet_list'))


# ─── Profile ─────────────────────────────────────────────────────────────────

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return redirect('user_profile', username=request.user.username)


def user_profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    tweets = Tweet.objects.filter(user=profile_user).annotate(
        like_count=Count('likes', distinct=True)
    ).order_by('-created_at')

    liked_ids = set()
    if request.user.is_authenticated:
        liked_ids = set(Like.objects.filter(user=request.user).values_list('tweet_id', flat=True))

    total_likes = Like.objects.filter(tweet__user=profile_user).count()

    return render(request, 'profile.html', {
        'profile_user': profile_user,
        'tweets': tweets,
        'tweet_count': tweets.count(),
        'liked_ids': liked_ids,
        'total_likes': total_likes,
    })


# ─── Search ──────────────────────────────────────────────────────────────────

def tweet_search(request):
    query = request.GET.get('q', '').strip()
    results = Tweet.objects.none()
    if query:
        results = Tweet.objects.filter(
            Q(text__icontains=query) | Q(user__username__icontains=query)
        ).annotate(like_count=Count('likes', distinct=True)).order_by('-created_at')

    liked_ids = set()
    if request.user.is_authenticated:
        liked_ids = set(Like.objects.filter(user=request.user).values_list('tweet_id', flat=True))

    return render(request, 'search_results.html', {
        'results': results,
        'query': query,
        'liked_ids': liked_ids,
    })