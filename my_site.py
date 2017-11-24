from bottle import run, route, static_file, get


def main(nhost='localhost', nport=8000):
    
    # static routes
    @get('/css/<filepath:re:.*\.css>')
    def css(filepath):
        return static_file(filepath, root='./css')

    @get('/fonts/<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>')
    def fonts(filepath):
        return static_file(filepath, root='./fonts')

    @get('/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>')
    def img(filepath):
        return static_file(filepath, root='./img')

    @get('/js/<filepath:re:.*\.js>')
    def js(filepath):
        return static_file(filepath, root='./js')

    @get('/documents/<filepath:re:.*\.(txt|doc|docx|xlsx)>')
    def documents(filepath):
        return static_file(filepath, root='./documents')
    # end of static routes

    # index page
    @route('/')
    def index():
        return static_file('index.html', root='./')
    
	# info page
    @route('/info')
    def info():
        return static_file('info.html', root='./')


    run(host=nhost, port=nport, debug=False)


