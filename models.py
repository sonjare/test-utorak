

class Comment(object):

	def __init__(self, text, date):
		self.text = text
		self.date = date

	def __repr__(self):
		return "text:{}, date:{}".format(self.text, self.date)

	
COMMENTS = [
Comment("hello", "2018-01-01"),
Comment("world", "2018-01-02"),
Comment("test", "2018-01-03")
]
	
	def table(self):
		comments = COMMENTS.split(',')
	  	table_str ="<table>"


      