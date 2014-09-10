import sublime, sublime_plugin
import os
import time

class CompileWithXelatexCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if '/usr/texbin' not in os.environ['PATH']:
		    os.environ['PATH'] += ':/usr/texbin'

		base_fname = self.view.file_name()[:-4]
		base_fname = base_fname + ".tex"
		pdf_fname = base_fname + ".pdf"
		self.view.window().run_command('exec',{'cmd': ['xelatex','-synctex=1','-interaction=nonstopmode',base_fname]})
		# os.system('open ' + pdf_fname)
		tries = 5
		seconds_to_wait = 1
		while tries > 0:
			if os.path.isfile(pdf_fname):
				break
			time.sleep(seconds_to_wait)
			seconds_to_wait *= 2
			tries -= 1

		# print pdf_fname
		os.system('open ' + pdf_fname)
