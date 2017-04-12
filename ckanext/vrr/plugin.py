import ckan.plugins.toolkit as toolkit
import ckan.plugins as p


if p.toolkit.check_ckan_version(min_version='2.5'):
    from ckan.lib.plugins import DefaultTranslation

    class VrrPluginBase(p.SingletonPlugin, DefaultTranslation):
        p.implements(p.ITranslation, inherit=True)
else:
    class VrrPluginBase(p.SingletonPlugin):
        pass

class VrrPlugin(VrrPluginBase):
    p.implements(p.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'vrr')