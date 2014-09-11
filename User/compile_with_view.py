import sublime, sublime_plugin

class CompileWithView(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.window().run_command("build")
		self.view.window().run_command("jump_to_pdf")
