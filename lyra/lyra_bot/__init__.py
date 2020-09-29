from flask import request

class LyraBot:
  def __init__(self, app=None):
    if app is not None:
      self.init_app(app)

  def init_app(self, app):
    @app.route('/lyra/', methods=['GET', 'POST'])
    def handle():
      print(request.__dict__)
      print(request.json)
      return ''
