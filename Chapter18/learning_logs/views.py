from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TopicForm, EntryForm
from django.http import Http404

# Create your views here.

from learning_logs.models import Topic, Entry

def check_topic_owner(request, topic):
    """check the topic belongs to the login user"""
    if request.user != topic.owner:
        raise Http404

def index(request):
    """The home page for learning log."""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """the topics page"""
    topics = Topic.objects.filter(owner=request.user).order_by('data_added')
    context = {'topics': topics, 'request_vars': vars(request)}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """show the detail of topic"""
    topic = get_object_or_404(Topic, id=topic_id)
    # topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request, topic)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic"""

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data
        form = TopicForm(data=request.POST)
        # print(form)

        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            # print(form, request.user, new_topic)
            new_topic.save()
            return redirect('learning_logs:topics')

    context = {
        'form': form
    }
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """add a new entry"""
    # topic = Topic.objects.get(id=topic_id)
    topic = get_object_or_404(Topic, id=topic_id)

    check_topic_owner(request, topic)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        # form.topic = topic
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {
        'form': form,
        'topic': topic,
    }

    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """edit an entry"""
    entry = get_object_or_404(Entry, id=entry_id)
    # entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(request, topic)
    # print(request.POST, topic, entry)

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {
        'form': form,
        'entry': entry,
        'topic': topic,
    }

    return render(request, 'learning_logs/edit_entry.html', context)

    