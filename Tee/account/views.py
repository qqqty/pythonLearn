from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from account.models import Account, Vote, VoteItem, VoteAccount
import time
#form

class AccForm(forms.Form):
    username = forms.CharField(label='name', max_length=20)
    password = forms.CharField(label='pw', max_length=20, widget=forms.PasswordInput)

class AddVoteForm(forms.Form):
    title = forms.CharField(max_length=30)
    content = forms.CharField(max_length=100)
    start_time = forms.DateTimeField()
    end_time = forms.DateTimeField()

    op_1 = forms.CharField(label='xuan 1', max_length=20)
    op_2 = forms.CharField(label='xuan 2', max_length=20, required=False)
    op_3 = forms.CharField(label='xuan 3', max_length=20, required=False)




def test(request):
    #arr = Account.objects.all()
    #id = 1
    #arr = Account.objects.get(id = id)
    arr = VoteAccount.objects.all()

    return render(request, 'account/test.html', {'arr':arr})


#wei md5 password
def reg(request):
    if request.method == 'POST':
        uf = AccForm(request.POST)
        if uf.is_valid():
            # data
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']

            # find
            user = Account.objects.filter(username__exact=username)

            if user:
                return HttpResponse('account name exist')
            else:
                res = Account.objects.create(username=username, password=password)
                if res:
                    return HttpResponse('success')
                else:
                    return HttpResponse('reg fail')
    else:
        uf = AccForm()

    return render_to_response('account/reg.html', {'uf':uf}, context_instance=RequestContext(request))

#wei md5 password
def login(request):
    if request.method == 'POST':
        uf = AccForm(request.POST)
        if uf.is_valid():
            #data
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #find
            user = Account.objects.filter(username__exact=username, password=password)

            if user:
                res = HttpResponseRedirect('/account/')
                res.set_cookie('username', username)
                return res
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = AccForm()

    return render_to_response('account/login.html', {'uf':uf}, context_instance=RequestContext(request))



#account
def account(request):
    username = request.COOKIES.get('username', '')
    if username:
        voteList = Vote.objects.all().filter(auth=username)


        return render(request, 'account/account.html', {'username':username, 'voteList':voteList})
    else:
        return HttpResponseRedirect('/login/')

#logout
def logout(request):
    res = HttpResponse('logout')
    res.delete_cookie('username')
    return res
    #return HttpResponseRedirect('/login/')

#addVote
def addVote(request):
    if request.method == 'POST':
        uf = AddVoteForm(request.POST)
        #shi wu
        if uf.is_valid():
            #data
            vote = Vote()
            vote.auth = request.COOKIES.get('username', '')
            vote.title = uf.cleaned_data['title']
            vote.content = uf.cleaned_data['content']
            vote.create_time = time.strftime('%Y-%m-%d %H:%I:%S', time.localtime())
            vote.start_time = time.strftime('%Y-%m-%d %H:%I:%S', time.localtime())
            vote.end_time = time.strftime('%Y-%m-%d %H:%I:%S', time.localtime(time.time()+6*3600))

            #id
            if Vote.objects.filter(title__exact=vote.title):
                return HttpResponse('title exist')

            vote.save()
            # res = vote.save()
            # if res:
            #     pass
            # else:
            #     return HttpResponse('fail')

            res = Vote.objects.get(title=vote.title)

            for i in range(1, 4):
                item = uf.cleaned_data['op_' + str(i)]
                if item:
                    voteItem = VoteItem()
                    voteItem.vote_id = res.id
                    voteItem.item = item
                    voteItem.save()

            return HttpResponse('add success')
    else:
        uf = AddVoteForm()

    return render_to_response('account/addVote.html', {'uf':uf}, context_instance=RequestContext(request))



def vote(request, vId):
    username = request.COOKIES.get('username', '')
    accInfo = Account.objects.get(username=username)
    if request.method == "POST":

        voteAccount = VoteAccount()
        voteAccount.acc_id = accInfo.id
        voteAccount.vote_id = request.POST.get('vote_id')
        voteAccount.item_id = request.POST.get('item_id')

        if not voteAccount.vote_id or not voteAccount.item_id:
            return HttpResponse('data error')

        res = voteAccount.save()

        return HttpResponse('success')

    else:
        if username:
            pass
        else:
            return HttpResponseRedirect('/login/')
        # voted
        if VoteAccount.objects.filter(vote_id=vId, acc_id=accInfo.id):
            return HttpResponse('voted')

        baseInfo = Vote.objects.get(id = vId)
        optionArr = VoteItem.objects.all().filter(vote_id = vId)
        return render_to_response('account/vote.html', {'baseInfo':baseInfo, 'optionArr':optionArr}, context_instance=RequestContext(request))





