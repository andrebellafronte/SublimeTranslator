import sublime, sublime_plugin
import urllib.parse
import urllib.request

langs = ['af','sq','ar','az','eu','bn','be','bg','ca','hr','cs','da','nl','en','eo','et','tl','fi','fr','gl','ka','de','el','gu','ht','iw','hi','hu','is','id','ga','it','ja','kn','ko','la','lv','lt','mk','ms','mt','no','fa','pl','pt','ro','ru','sr','sk','sl','es','sw','sv','ta','te','th','tr','uk','ur','vi','cy','yi']

class translator(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
                line = self.view.line(region)
                to_translate = self.view.substr(line)
                to_language = to_translate.split()[-1]
                to_translate = to_translate.rpartition(' ')[0]

                for element in langs:
                    if element not in to_translate:
                        pass
                    else:
                        if (len(to_translate)<1):
                            pass
                        else:
                            langage = 'detect'
                            agents = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}
                            before_trans = 'class="t0">'
                            link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (to_language, langage, to_translate.replace(" ", "+"))
                            req = urllib.request.Request(link, headers={'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'})
                            response = urllib.request.urlopen(req)
                            the_page = response.read()
                            page = the_page.decode('utf-8')
                            result = page[page.find(before_trans)+len(before_trans):]
                            output = result.split("<")[0]
                            output = output.replace('\r', '')
                            self.view.replace(edit, line, output)