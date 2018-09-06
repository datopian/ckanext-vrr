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


class VrrUserController(UserController):

    def index(self):
        '''We are overwriting the default index action in
        order to make the users list available only
        for system administrators
        '''

        context = {'return_query': True, 'user': c.user,
                   'auth_user_obj': c.userobj}

        data_dict = {'q': c.q,
                     'order_by': c.order_by}

        try:
            check_access('sysadmin', context, data_dict)
        except NotAuthorized:
            abort(403, _('Not authorized to see this page'))

        return super(VrrUserController, self).index()

    def activity(self, id, offset=0):
        '''Render this user's public activity stream page.'''

        context = {'model': model, 'session': model.Session,
                   'user': c.user, 'auth_user_obj': c.userobj,
                   'for_view': True}
        data_dict = {'id': id, 'user_obj': c.userobj,
                     'include_num_followers': True}
        try:
            toolkit.check_access('sysadmin', context, data_dict)
        except NotAuthorized:
            abort(403, _('Not authorized to see this page'))

        self._setup_template_variables(context, data_dict)

        try:
            c.user_activity_stream = get_action('user_activity_list_html')(
                context, {'id': c.user_dict['id'], 'offset': offset})
        except ValidationError:
            base.abort(400)

        return render('user/activity_stream.html')
