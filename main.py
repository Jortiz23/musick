import webapp2
import jinja2
import os
from artist_service import artist_info
from song_service import song_info

jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = jinja_current_directory.get_template("templates/welcome.html")
        self.response.write(welcome_template.render())

class ArtistsHandler(webapp2.RequestHandler):
    def get(self):
        artists_template = jinja_current_directory.get_template("templates/artists.html")
        self.response.write(artists_template.render())

class ArtistHandler(webapp2.RequestHandler):
    def post(self):
        name = self.request.get('name')
        artist_template = jinja_current_directory.get_template("templates/artist.html")
        self.response.write(artist_template.render({
            "name": name,
            "image": artist_info[name]['image'],
            "spotify_link": artist_info[name]['spotify_link'],
            "artist_link": artist_info[name]['artist_link'],

app = webapp2.WSGIApplication([
    ('/', WelcomeHandler),
    ('/artists', ArtistsHandler),
    ('/artist', ArtistHandler),
], debug = True)
