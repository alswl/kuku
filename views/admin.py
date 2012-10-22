# coding=utf-8

from views import render

class Index:
    def GET(self):
        return render.foundation()
