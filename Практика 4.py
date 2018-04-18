import urllib.request
import html.parser

class MyHTMLParser(html.parser.HTMLParser):
    def __init__(self, site_address, *args, **kwargs):
        self.links = []
        self.site_address = site_address
        super().__init__(*args, **kwargs)
        self.feed(self.read_site_content())
        self.write_to_file()

    def read_site_content(self):
        return str(urllib.request.urlopen(self.site_address).read())

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    if self.validate(attr[0]):
                        self.links.append(attr[1])

    def validate(self, link):
        return link not in self.links and \
               '#' not in link and \
               'javascript:' not in link

    def write_to_file(self):
        with open('link.txt','w') as file:
            if self.links:
                file.write('\n'.join(self.links))
            else:
                file.write('Nothing found. Sorry :(')
def main():
    addr = input('Введите сайт, который хотите спарсить:')
    site = MyHTMLParser(addr)

if __name__ == '__main__':
    main()
