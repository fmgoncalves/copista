#!/usr/bin/python
import os
import subprocess

import cherrypy
from cherrypy.lib.static import serve_file

ROOT_PATH='/home/filipe/Desktop/texlib'
DOCUMENT_PATH='{0}/docs'.format(ROOT_PATH)
BIN_PATH='{0}/bin'.format(ROOT_PATH)
BASE_PATH='{0}/base'.format(ROOT_PATH)

class Copista(object):
	index_page = '''
<html>
	<head>
		<title>Copista</title>
	</head>
	<body>
		<h2>Available Documents</h2>
		<ul>
		{}
		</ul>
	</body>
</html>'''

	@cherrypy.expose
	def index(self):
		docs = filter(lambda x: os.path.isdir('{0}/{1}'.format(DOCUMENT_PATH,x)),os.listdir(DOCUMENT_PATH))
		return Copista.index_page.format(''.join(map('<li><a href="docs/{0}.pdf">{0}</a></li>'.format,docs)))

	@cherrypy.expose
	def docs(self, document):
		pdf_file='{0}/{1}'.format(BIN_PATH,document)
		if not os.path.exists(pdf_file):
			document_name=document.strip('.pdf')
			texcmd="TEXINPUTS={0}: pdflatex -output-directory={1} {2}/{3}/{3}.tex".format(BASE_PATH,BIN_PATH,DOCUMENT_PATH,document_name)
			subprocess.call(texcmd,shell=True)
			# TODO check for errors in the generation
		return serve_file(pdf_file, "application/x-download", "attachment")

if __name__ == '__main__':
	cherrypy.quickstart(Copista())
