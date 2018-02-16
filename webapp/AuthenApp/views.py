from django.shortcuts import render

def registration(request):
    if request.POST:
        form = MemberForm(request, data=request.POST)
        if form.is_valid():
            new_member = form.save(commit=False)
            new_member.expiry_date = new_member.cal_expiry_date()
            new_member.save()
            return redirect('StaticPageApp:landing')
            
    form = MemberForm(request)
    return render(request, 'managementApp/new_member.html', {'form': form})

def login(request):
    return render(request, 'AuthenApp/login.html')
