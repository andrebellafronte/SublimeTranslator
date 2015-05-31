import sublime_plugin
import urllib.parse
import urllib.request

langs = ['af', 'sq', 'ar', 'az', 'eu', 'bn', 'be', 'bg', 'ca', 'hr', 'cs',
         'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'gl', 'ka', 'de',
         'el', 'gu', 'ht', 'iw', 'hi', 'hu', 'is', 'id', 'ga', 'it', 'ja',
         'kn', 'ko', 'la', 'lv', 'lt', 'mk', 'ms', 'mt', 'no', 'fa', 'pl',
         'pt', 'ro', 'ru', 'sr', 'sk', 'sl', 'es', 'sw', 'sv', 'ta', 'te',
         'th', 'tr', 'uk', 'ur', 'vi', 'cy', 'yi']


def translate(from_lan, to_lan, text):
    before_trans = 'class="t0">'

    link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" \
        % (to_lan,
           from_lan,
           text.replace(" ", "+"))

    req = urllib.request.Request(
        link, headers={'User-Agent':
                       'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'})

    response = urllib.request.urlopen(req)
    the_page = response.read()
    page = the_page.decode('utf-8')
    result = page[page.find(before_trans) + len(before_trans):]
    output = result.split("<")[0]
    output = output.replace('\r', '')
    return output


class translator(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
                line = self.view.line(region)
                to_translate = self.view.substr(line)
                to_language = to_translate.split()[-1]
                to_translate = to_translate.rpartition(' ')[0]

                if to_language not in langs:
                    pass
                else:
                    if (len(to_translate) < 1):
                        pass
                    else:
                        from_language = 'detect'
                        output = translate(from_language, to_language,
                                           to_translate)
                        self.view.replace(edit, line, output)
