from django.http import HttpResponse
from django.shortcuts import render, redirect

from chooseplan.forms import chooseplanform

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

def index(request):
    stmt = 'Select * From public."chooseplan_demographics" Order By id DESC LIMIT 1'
    result_proxy = connection.execute(stmt)
    results = result_proxy.fetchall()
    return render(request, 'algorithm/results.html', {'results' : results} )
