import kabbes_menu
import kabbes_user_client
import py_starter as ps

class Client( kabbes_menu.Menu ):

    BASE_CONFIG_DICT = {
        "_Dir": kabbes_menu._Dir
    }

    def __init__( self, dict={}, **kwargs ):

        dict = ps.merge_dicts( Client.BASE_CONFIG_DICT, dict )
        self.cfg_menu = kabbes_user_client.Client( dict=dict, **kwargs ).cfg

        cfg_options_node = self.cfg_menu[ kabbes_menu.Menu._OPTIONS_CFG_KEY ]
        cfg_options_node.load_dict( self._OVERRIDE_OPTIONS )

        kabbes_menu.Menu.__init__( self )
