import ckan.plugins.toolkit as toolkit
import ckan.plugins as p
import ckanext.vrr.action
from ckan.config.routing import SubMapper



if p.toolkit.check_ckan_version(min_version='2.5'):
    from ckan.lib.plugins import DefaultTranslation

    class VrrPluginBase(p.SingletonPlugin, DefaultTranslation):
        p.implements(p.ITranslation, inherit=True)
else:
    class VrrPluginBase(p.SingletonPlugin):
        pass

class VrrPlugin(VrrPluginBase):
    p.implements(p.IConfigurer)
    p.implements(p.IRoutes, inherit=True)
    p.implements(p.IActions)


    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'vrr')


        # IRoutes

    def before_map(self, map):
        vrr_controller = \
            'ckanext.vrr.controllers.vrr:VrrController'

        map.connect('vrr_api',
                    '/api',
                    controller=vrr_controller,
                    action='api')
        user_ctrl = 'ckanext.vrr.controllers.vrr:VrrUserController'
        with SubMapper(map, controller=user_ctrl) as m:
            m.connect('register', '/user/_register_partner', action='register')
            map.connect('user_index', '/user',
                        controller=user_ctrl, action='index')
            m.connect('/user/activity/{id}/{offset}', action='activity')
            m.connect('user_activity_stream', '/user/activity/{id}',
                      action='activity', ckan_icon='time')
        return map

    def get_actions(self):
        action_functions = {
            'user_list':
                ckanext.vrr.action.user_list,
            'user_show':
                ckanext.vrr.action.user_show
        }

        return action_functions
