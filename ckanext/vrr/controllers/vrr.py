from ckan.lib import base
render = base.render
BaseController = base.BaseController


class VrrController(BaseController):
    def api(self):
        return render('api.html')
