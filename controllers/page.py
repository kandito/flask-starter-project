from flask import Blueprint, render_template, abort
from flask import Flask, session, redirect, url_for, escape, request, flash, get_flashed_messages
from jinja2 import TemplateNotFound
from models import *

page = Blueprint('page', __name__, template_folder='application/templates')

@page.route('/index')
@page.route('/')
def index():
    try:
        return render_template('home.html')
    except TemplateNotFound:
        abort(404)

@page.route('/page', defaults={'page': 'index'})
@page.route('/page/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)