Synthesizing 9/10 solutions (Duplicates hidden)

=======

def hello(username):
    return f"Hello, {escape(username)}!"

=======

def hello_user(username):
    return "<p>Hello, %s!</p>" % escape(username)

=======

def hello(username):
    return "<p>Hello, %s!</p>" % escape(username)

=======

def hello_user(username):
    return f"Hello, {escape(username)}!"

=======

def hello(username):
    return f"Hello {escape(username)}!"

=======

def hello(username):
    return render_template('hello.html', name=username)
