#!/usr/bin/env python

__author__ = 'Joey with help from coaches and google'

import requests
import json
import time
import turtle

def get_all_astro():
    memebers = requests.get("http://api.open-notify.org/astros.json")
    text_members = memebers.text
    as_dict = json.loads(text_members)
    astros = []
    for astro in as_dict['people']:
        astros.append(astro['name'])
    return astros

def iss_location(x):
    loc = requests.get("http://api.open-notify.org/iss-now.json")
    loc_dict = json.loads(loc.text)
    current_loc = loc_dict["iss_position"]
    stamp = time.ctime(loc_dict["timestamp"])
    people_str = ", ".join(x)[:-2]
    print ("The astronauts {} are at:\nlongitude: {} \nlatitude: {}, at the time of ({})".format(people_str, current_loc["longitude"], current_loc["latitude"], stamp))
    return(float(current_loc["longitude"]), float(current_loc["latitude"]))

def turtle_club(iss_position, next_pass):
    screen = turtle.Screen()
    screen.bgpic('./map.gif')
    screen.addshape('iss.gif')
    screen.setup(width=720, height=360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    new_var = turtle.Turtle()
    new_var.shape('iss.gif')
    new_var.penup()
    new_var.goto(iss_position)
    indy_dot = turtle.Turtle()
    indy_dot.shape('circle')
    indy_dot.color('yellow')
    indy_dot.penup()
    indy_dot.goto(-86.1349, 40)
    msg = turtle.Turtle()
    msg.color('white')
    msg.write(next_pass, True, align='center')
    screen.exitonclick()


def over_indy():
    r = requests.get("http://api.open-notify.org/iss-pass.json?lat=40&lon=-86.1349")
    dictionary = r.text
    dictionary = json.loads(dictionary)
    next_pass = dictionary["response"][0]
    return("The next pass over Indianapolis is {}".format(time.ctime(next_pass["risetime"])))


pos = iss_location(get_all_astro())
turtle_club(pos, over_indy())

def main():
    pass




if __name__ == '__main__':
    main()
