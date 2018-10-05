from ckan.lib import base
import ckan.plugins.toolkit as toolkit
import logging
from ckan.controllers.user import UserController
import ckan.model as model
import ckan.logic as logic
import ckan.lib.navl.dictization_functions as dictization_functions
from ckan.common import _, c

log = logging.getLogger(__name__)

abort = base.abort
render = base.render

check_access = logic.check_access
get_action = logic.get_action
NotFound = logic.NotFound
NotAuthorized = logic.NotAuthorized
ValidationError = logic.ValidationError
UsernamePasswordError = logic.UsernamePasswordError
DataError = dictization_functions.DataError
unflatten = dictization_functions.unflatten
render = base.render
BaseController = base.BaseController


class VrrController(BaseController):
    def api(self):
        controller = 'ckanext.pages.controller:PagesController'
        action = 'pages_show'
        page = '/api'
        return toolkit.redirect_to(controller=controller, action=action, page=page)
