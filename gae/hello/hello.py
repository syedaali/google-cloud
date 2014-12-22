__author__ = 'syedaali'

import webapp2

MAIN_PAGE = 'Hello Google!'

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write(MAIN_PAGE)

application = webapp2.WSGIApplication([
  ('/',MainPage),
  ], debug=True)
