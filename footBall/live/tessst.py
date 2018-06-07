{% extends "live/base.html" %}
{% load static %}
{% block title %}Category{% endblock %}

{% block content %}


<nav id="list_category">
    {% for match in matchs_today %}
    <a href="{{match.get_absolute_url }}">{{match.home_team_1 }} </a>
    {% endfor %}
</nav>

<section id="center">
    match matchs_yesterday:
    {%for match in matchs_yesterday %}
    <h3><a href="{{lig.get_absolute_url }}">{{match.home_team_1}} vs {{match.guest_team_2}}</a> </h3><br>
    {% endfor%}
    match today:
    {%for match in matchs_today %}
    <h3><a href="{{lig.get_absolute_url }}">{{match.home_team_1}} vs {{match.guest_team_2}}</a> </h3><br>
    {% endfor%}
    match matchs_tomorrow:
    {%for match in matchs_tomorrow %}
    <h3><a href="{{lig.get_absolute_url }}">{{match.home_team_1}} vs {{match.guest_team_2}}</a> </h3><br>
    {% endfor%}


