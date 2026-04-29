from django.shortcuts import render


def landing_page(request):
    return render(request, 'architectura_landing_page.html')


def about_us(request):
    return render(request, 'about_us.html')


def services_overview(request):
    return render(request, 'services_overview.html')


def projects_catalog(request):
    return render(request, 'projects_catalog.html')


def project_detail_villa_nordica(request):
    return render(request, 'project_detail_villa_nordica.html')


def project_comparison(request):
    return render(request, 'project_comparison.html')


def portfolio_project_zenith(request):
    return render(request, 'portfolio_project_zenith.html')


def portfolio_map_view(request):
    return render(request, 'portfolio_map_view.html')


def individual_design(request):
    return render(request, 'individual_design.html')


def mortgage_financing(request):
    return render(request, 'mortgage_financing.html')


def educational_house_area_explained(request):
    return render(request, 'educational_house_area_explained.html')


def careers(request):
    return render(request, 'careers.html')


def contact_us(request):
    return render(request, 'contact_us.html')
