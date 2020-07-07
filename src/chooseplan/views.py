from django.shortcuts import render, redirect
from django.http import HttpResponse
import json

from .forms import chooseplanform
from .models import demographics

# python local setting
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import psycopg2
import re
import pprint
from itertools import chain

engine = create_engine("postgres+psycopg2://postgres:12221992@localhost:5432")
connection = engine.connect()
metadata = MetaData()

def chooseplan(request):

    if request.method == 'POST':
        form = chooseplanform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/results")
    else:
        form = chooseplanform()
    return render(request, 'chooseplan/chooseplan.html', {'form': form })

def get_demographic_data(self):
    stmt = 'Select * From public."chooseplan_demographics" Order By id DESC LIMIT 1'
    result_proxy = connection.execute(stmt)
    results = result_proxy.fetchall()
    return results

def get_healthplan_data(self):
    stmt = 'Select * From public."healthplanportal_healthplan" Order By id DESC LIMIT 1'
    result_proxy = connection.execute(stmt)
    results = result_proxy.fetchall()
    return results

def get_hospital_data(self):
    stmt = 'Select * From public."hospital_services_portal_hospital" Order By id DESC LIMIT 1'
    result_proxy = connection.execute(stmt)
    results = result_proxy.fetchall()
    return results

def get_hospital_services_data(self):
    stmt = 'Select * From public."hospital_services_portal_service" Order By id DESC LIMIT 1'
    result_proxy = connection.execute(stmt)
    results = result_proxy.fetchall()
    return results