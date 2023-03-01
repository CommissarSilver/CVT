Synthesizing 10/10 solutions (Duplicates hidden)

=======

def hello(username):
    return f"Hello, {escape(username)}!"

=======

def hello_user(username):
    return f"Hello {escape(username)}!"

=======

def hello(username):
    return "<h1>Hello, " + escape(username) + "!</h1>"

=======

def hello(username):
    return "Hello %s!" % escape(username)

=======

def hello_user(username):
    return 'Hello {}!'.format(escape(username))

=======

def hello_world(username):
    return "<p>Hello, {}!<p>".format(escape(username))
