from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from users.models import Member
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import MemberForm

# Create your views here.


# generic class based views
class IndexClassView(ListView):
    model = Member
    template_name ='users/index.html'
    context_object_name ='member_list'


class AddMemberClassView(CreateView):
    model = Member
    fields = '__all__'
    template_name='users/add-form.html'
 
    def form_valid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

# class view for editing members
class EditMemberClassView(UpdateView):
    model = Member
    fields = '__all__'
    template_name='users/edit-form.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

# function view for editing members
# def edit(request, id):
#     member = Member.objects.get(id=id)
#     form = MemberForm(request.POST or None, instance=member)

#     if form.is_valid():
#         form.save()
#         return redirect('users:index')

#     return render(request, 'users/edit-form.html', {'form':form, 'member':member})

# class view for deleting members
class DeleteMemberClassView(DeleteView):
    model = Member
    success_url = reverse_lazy('users:index')

# function view for deleting members
# def delete(request, id):
#     member = Member.objects.get(id=id)

#     if request.method == 'POST':
#         member.delete()
#         return redirect('users:index')

#     return render(request, 'users/delete.html',{'member':member})