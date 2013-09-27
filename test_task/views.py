# -*- coding: utf-8 -*-

from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models import ShortLink
from forms import ShortLinkForm

def index(request):
    links = ShortLink.objects.all()[:20]

    if request.method == "POST":
        form = ShortLinkForm(request.POST)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.save()
            return redirect('show', link_name=inst.short_link)
    else:
        form = ShortLinkForm()
    return render_to_response("index.tpl", locals(),
                              context_instance=RequestContext(request))

def link_list(request):
    links = ShortLink.objects.all()
    paginator = Paginator(links, 2)

    page = request.GET.get('page')
    try:
        links = paginator.page(page)
    except PageNotAnInteger:
        links = paginator.page(1)
    except EmptyPage:
        links = paginator.page(paginator.num_pages)

    return render_to_response("list.tpl", locals(),
                              context_instance=RequestContext(request))

def show(request, link_name):
    link = get_object_or_404(ShortLink, short_link=link_name)
    return render_to_response("show.tpl", locals(),
                              context_instance=RequestContext(request))

def delete(request, link_name):
    link = get_object_or_404(ShortLink, short_link=link_name)
    link.delete()
    return redirect("index")

def go_to(request, link_name):
    link = get_object_or_404(ShortLink, short_link=link_name)
    link.inc_views()
    return HttpResponseRedirect(link.original_url)
