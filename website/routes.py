
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user 
from  . import db
from auth.services import *
from sqlalchemy.sql import func


routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('website/home.html')

@routes.route('/chat')
def chat():
    return render_template('website/chat.html')

@routes.route('/book')
def book():
    return render_template('website/book.html')