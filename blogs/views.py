from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from django.views.generic import CreateView, ListView, DetailView, UpdateView, \
    DeleteView
from pytils.translit import slugify

from blogs.forms import BlogForm, ReleaseForm
from blogs.models import Blog, Release
from order.services import send_order_email, send_max_count_email


# Create your views here.
class BlogCreateView(CreateView, LoginRequiredMixin):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blogs:list')

    def form_valid(self, form):
        post = form.save()
        user = self.request.user
        post.author = user
        post.save()
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ReleaseFormset = inlineformset_factory(Blog, Release, form=ReleaseForm,
                                               extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ReleaseFormset(self.request.POST,
                                                     instance=self.object, )
        else:
            context_data['formset'] = ReleaseFormset(instance=self.object, )
        return context_data

    def form_valid(self, form):
        # if form.is_valid():
        #     new_post = form.save()
        #     new_post.slug = slugify(new_post.title)
        #     new_post.save()
        context_data = self.get_context_data()
        formset = context_data['formset']

        if formset.is_valid() and form.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form,
                                                                 formset=formset))

    def get_success_url(self):
        return reverse('blogs:view', args=[self.kwargs.get('pk')])


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        if self.object.views_count == 15:
            send_max_count_email(self.object)
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs:list')
