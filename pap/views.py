from django.shortcuts import render, get_object_or_404
# from django.utils import timezone
# from .models import Post
# from .forms import PostForm
# from django.shortcuts import redirect

def login(request):
	return render(request, 'pap/login.html', {})


def index(request):
	# posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	# posts = Post.objects.all()
	return render(request, 'pap/index.html', {})

def payment(request):
    return render(request, 'pap/payment.html', {})

def card_pm(request):
    return render(request, 'pap/card_pm.html', {})

def card_pm_ol(request):
    return render(request, 'pap/card_pm_ol.html', {})

def vir_acc(request):
    return render(request, 'pap/vir_acc.html', {})

def acc_tran(request):
    return render(request, 'pap/acc_tran.html', {})

def ceph_pm(request):
    return render(request, 'pap/ceph_pm.html', {})
    
def cash_pm(request):
    return render(request, 'pap/cash_pm.html', {})

def cash_pm_ol(request):
    return render(request, 'pap/cash_pm_ol.html', {})

def card_plm_ip(request):
    return render(request, 'pap/card_plm_ip.html', {})

def card_plm(request):
    return render(request, 'pap/card_plm.html', {})

def refund(request):
    return render(request, 'pap/refund.html', {})

def purchase_case(request):
    return render(request, 'pap/purchase_case.html', {})

def purchase_li(request):
    return render(request, 'pap/purchase_li.html', {})

def purchase_li_file(request):
    return render(request, 'pap/purchase_li_file.html', {})

def purchase_li_rs(request):
    return render(request, 'pap/purchase_li_rs.html', {})

def sch_cal(request):
    return render(request, 'pap/sch_cal.html', {})

def pmdate_li(request):
    return render(request, 'pap/pmdate_li.html', {})

def pmmethod_li(request):
    return render(request, 'pap/pmmethod_li.html', {})

def outsam_li(request):
    return render(request, 'pap/outsam_li.html', {})

def balance_li(request):
    return render(request, 'pap/balance_li.html', {})

def pmpostpone_li(request):
    return render(request, 'pap/pmpostpone_li.html', {})

def taxinvoice_li(request):
    return render(request, 'pap/taxinvoice_li.html', {})

def cardtt_rp(request):
    return render(request, 'pap/cardtt_rp.html', {})

def acctrantt_rp(request):
    return render(request, 'pap/acctrantt_rp.html', {})

def viracctt_rp(request):
    return render(request, 'pap/viracctt_rp.html', {})

def cephpm_rp(request):
    return render(request, 'pap/cephpm_rp.html', {})

def cashpm_rp(request):
    return render(request, 'pap/cashpm_rp.html', {})

def user_li(request):
    return render(request, 'pap/user_li.html', {})

def user_li_new(request):
    return render(request, 'pap/user_li_new.html', {})

def user_li_edit(request):
    return render(request, 'pap/user_li_edit.html', {})

def company_info(request):
    return render(request, 'pap/company_info.html', {})

def client_li(request):
    return render(request, 'pap/client_li.html', {})

def client_li_new(request):
    return render(request, 'pap/client_li_new.html', {})

def client_li_edit(request):
    return render(request, 'pap/client_li_edit.html', {})

def client_user_li(request):
    return render(request, 'pap/client_user_li.html', {})

def card_charge(request):
    return render(request, 'pap/card_charge.html', {})

def cash_charge(request):
    return render(request, 'pap/cash_charge.html', {})

def test(request):
    return render(request, 'pap/test.html', {})

def preparing(request):
    return render(request, 'pap/preparing.html', {})

"""
django test
def post_list(request):
	# posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	posts = Post.objects.all()
	return render(request, 'pap/post_list.html', {'posts' : posts })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'pap/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'pap/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'pap/post_edit.html', {'form': form})

"""