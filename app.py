#!/usr/bin/python

try:
	from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
except:
	from http.server import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
try:
	from urlparse import urlparse
	from urlparse import urlparse, parse_qs
except:
	from urllib.parse import urlparse, parse_qs

import os
port = int(os.environ.get("PORT", 5000))	
PORT_NUMBER = port

#el le asigna un puerto con el enviroment, y si no se asigna el puerto 5000

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
#existente dos metodos el get y post en servidores web, el get se dispara cuando se carga la pagina'''
	
	#Handler for the GET requests
	def do_GET(self):      #salta directamente l metodo get'''
		path=self.path   #es importante por el que el path es parte de la direccion'''
		print(self.path)
		if self.path=="/":  #127.0.0.1:5000/
			self.path="/index.html" #127.0.0.1:5000/index.html
		try:
			#Check the file extension required and
			#set the right mime type

			sendReply = False        #sirve para especificar tipo de respuesta, como [por ejemplo cuando da un mensaje el servidor no rresponde'''
			if self.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype='image/jpg'
				sendReply = True
			if self.path.endswith(".gif"):
				mimetype='image/gif'
				sendReply = True
			if self.path.endswith(".js"):
				mimetype='application/javascript'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True

			if sendReply == True:
				#Open the static file requested and send it
				#f = open(curdir + sep + self.path,'r') 
				self.send_response(200)  #codigo 200 es una respuesta exitosa'''
				self.send_header('Content-type',mimetype)
				self.end_headers()
				
				try:
					self.wfile.write('Soy Dani Alvarez Armen') #envia respuesta de python 2'''
				except:
					self.wfile.write(bytes('Soy Dani Alvarez Armen', 'UTF-8')) #envia respuesta de python 3'''
                    
				
			return


		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path) #cuando hay un error manda el 404'''

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('0.0.0.0', PORT_NUMBER), myHandler) #cuando especifique la direccion estoy diciendo que reciba peticiones de cualquier ip,  127.0.0.0 solo peticiones locale, 
#cuando pongo 0.0.0.0 solo accedo de mi computador
	print ('Started httpserver on port ' , PORT_NUMBER) #el portnombre el sistema asigna un puerto'''
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print ('^C received, shutting down the web server')
	server.socket.close()
	
