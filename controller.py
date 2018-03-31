import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/template.html", title="HomePage")


class MyFormHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/form.html", title="My Form")

    def post(self):
        self.set_header("Content-Type", "text/plain")
        requested_amount = self.get_body_argument("requested_amount")
        try:
            requested_amount = int(requested_amount)
        except ValueError:
            requested_amount = None
        
        if requested_amount == None:
            decision = 'Please fill a requested amount in the application process'
        elif requested_amount > 50000:
            decision = 'Your loan was Declined'
        elif requested_amount == 50000:
            decision = 'Your loan was Undecided'
        elif requested_amount < 50000:
            decision = 'Your loan was Approved'
        self.set_header("Content-Type", "text/html")
        self.render(
            "templates/template.html",
            title="My Results",
            decision=decision
            )
