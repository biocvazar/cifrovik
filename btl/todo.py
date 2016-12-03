from bottle import (
    app,
    route,
    static_file,
    template,
    url
)


test_app = app()


@test_app.route("/")
def index():
    return template("index.html", url=url)
  

@test_app.route("/static/<filename>", name="static")
def static(filename):
    return static_file(filename, root="static")
    
    
def serve():
    test_app.run( 
        host="localhost",
        port=80,
    )
    
    
if __name__ == "__main__":
    serve()