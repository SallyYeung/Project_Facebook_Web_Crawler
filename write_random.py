# -*- coding: utf8 -*-

#Reference:

# Mayavi Example Code:Gael Varoquaux <gael.varoquaux@normalesup.org>
# Mayavi Example Link:https://github.com/enthought/mayavi/blob/master/examples/mayavi/mlab/tvtk_in_mayavi.py
# BeautifulSoup Tutorial: https://www.youtube.com/watch?v=3xQTJi2tqgk&t=1362s


from mayavi import mlab
import requests
from bs4 import BeautifulSoup
import sys
from tvtk.api import tvtk
from tvtk.common import configure_input_data
import random
import time

# change the size and color of the canvas
v = mlab.figure(bgcolor=(0,0,0), size=(800, 600))

# Make an animation of each words that we scraped
# By using the animate(delay)
# Change the number in delay will change the speed of the animation
@mlab.show
@mlab.animate(delay=500)
def write():

# Web crawler(BeautifulSoup)
    url = "https://www.facebook.com/johncampea"
    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html.parser")
    links = soup.find_all("a")
    # Find the a tag and div tag
    information = soup.find_all("div", {"class": "_5h60 _iez _3-8o"})
    # Put the content into the class "information"


    for item in information:
        a = item.text.encode('utf-8')
        z = a.split()
        reload(sys)
        sys.setdefaultencoding('utf-8')
        my_string = a
        n = len(my_string.split())
        # Use a for-loop to count the number of words in "information"

    i = 0
    a = 0
    b = 0
    # Set up the integer to 0 at the beginning of the program
    while i < n:
        #print the word in 3D until it reach the maximum number of 'n'
        vtext2 = tvtk.VectorText()
        for item in information:
            m = item.text.encode('utf-8')
            z = m.split()
            reload(sys)
            sys.setdefaultencoding('utf-8')
            vtext2.text = z[b]
        text_mapper = tvtk.PolyDataMapper()
        configure_input_data(text_mapper, vtext2.get_output())
        vtext2.update()
        #----word color-----
        p2 = tvtk.Property(color=(random.random(), random.random(), random.random()))
        #----End-----
        text_actor = tvtk.Follower(mapper=text_mapper, property=p2)
        text_actor.position = (0,a,random.randint(0,5))
        v.scene.add_actor(text_actor)
        i += 1
        a += 2
        b += 1
        # use yield as a loop to print and count the number in integer
        yield
    mlab.show()

mlab.view(85, -17, 15, [3.5, -0.3, -0.8])
write()
