from jinja2 import Environment, PackageLoader
jinja2 = Environment(loader=PackageLoader('rodeo', 'views'))

class RodeoViewHtml(object):
    
    def __init__(self, context):
        self.view    = None
        self.model   = None
        self.context = context
    
    def __call__(self):
        # can apply caching logic here if needed
        response = self.context.response
        template = jinja2.get_template(self.view)
        
        response.headers.add("content-type", "text/html", charset="utf-8")
        return template.render(self.model)

def RodeoViewEngine(context):
    
    # if you wanted, could switch the renderer 
    # based on the context
    return RodeoViewHtml(context)
