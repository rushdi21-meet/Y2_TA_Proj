from sqlalchemy.testing import db
from flask import Flask, jsonify, request, render_template, redirect, url_for
from sqlalchemy.sql import exists

from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# replace lecture.db with your own database file
engine = create_engine('sqlite:///Members_DB.db', connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def query_all():
    """
    Print all the volunteers
    in the database.
    """
    members = session.query(Member).all()
    return members


def add_member(email, password, success=0):
    """
    Add a volunteer to the database, given
    their name, year, and whether they have
    finished the lab.
    """
    if query_by_email(email) == false:
        new_member = Member(email=email, password=password)
        session.add(new_member)
        session.commit()
        success = 1
        print("new member added!")
        return success
    else:
        print("email exists!")
        return success


def query_by_email(email):
    try:
        member = session.query(Member).filter_by(email=email).first()
        return member.id
    except:
        print("no such member")
        return false


def query_by_password(password):
    try:
        member = session.query(Member).filter_by(password=password).first()
        return member.id
    except:
        print("no such password")
        return false


def login(email, password):
    if query_by_email(email) == query_by_password(password):
        if query_by_email(email) != false:
            return true
        else:
            return false
    else:
        return false
