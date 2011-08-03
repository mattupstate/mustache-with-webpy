import web

urls = (
    r'/examples', 'controllers.examples.ExamplesIndex',
    r'/examples/', 'controllers.examples.ExamplesIndex',
    r'/examples/?([^/.]*)', 'controllers.examples.ExamplesShow',
    r'/examples/?([^/.]*)/', 'controllers.examples.ExamplesShow',
    r'/', 'controllers.main.MainIndex'
)

app = web.application(urls, globals())
if __name__ == '__main__': app.run()