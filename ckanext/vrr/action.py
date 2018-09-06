import logging

import ckan.lib.dictization
import ckan.logic as logic
import ckan.logic.action
import ckan.logic.schema
import ckan.lib.navl.dictization_functions
import ckan.plugins.toolkit as toolkit

# Define some shortcuts
# Ensure they are module-private so that they don't get loaded as available
# actions in the action API.
_validate = ckan.lib.navl.dictization_functions.validate
_table_dictize = ckan.lib.dictization.table_dictize
_check_access = logic.check_access
NotFound = logic.NotFound
ValidationError = logic.ValidationError
_get_or_bust = logic.get_or_bust


log = logging.getLogger(__name__)


@toolkit.side_effect_free
def user_list(context, data_dict):
    '''We are overwriting the default user_list api action in
    order to make the users list available only
    for system administrators
    '''
    _check_access('sysadmin', context, data_dict)
    return logic.action.get.user_list(context, data_dict)


@toolkit.side_effect_free
def user_show(context, data_dict):
    '''Forbid anonymous access to user info.
    API call works with POST request with authorization header and id
    of desired user supplied.
    '''
    if context.get('user'):
        return logic.action.get.user_show(context, data_dict)
    else:
        raise toolkit.NotAuthorized(
            'You must be logged in to perform this action.')
