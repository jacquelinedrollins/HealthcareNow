from django.urls import reverse, resolve

def test_home_page():
    path = reverse('index')
    assert resolve(path).view_name == 'index'

def test_about_page():
    path = reverse('about')
    assert resolve(path).view_name == 'about'

def test_chooseplan_page():
    path = reverse('chooseplan')
    assert resolve(path).view_name == 'chooseplan'

def test_choosepl():
    path = reverse('show_chooseplan')
    assert resolve(path).view_name == 'show_chooseplan'
