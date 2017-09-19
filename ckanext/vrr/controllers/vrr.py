from ckan.lib import base
import ckan.plugins.toolkit as toolkit
render = base.render
BaseController = base.BaseController


class VrrController(BaseController):
    def api(self):
        controller = 'ckanext.pages.controller:PagesController'
        action = 'pages_show'
        page = '/api'
        return toolkit.redirect_to(controller=controller, action=action, page=page)
