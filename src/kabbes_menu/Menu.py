from parent_class import ParentClass
from kabbes_menu import CRTI
import py_starter as ps

class Menu( ParentClass ):

    _BASE_OPTIONS = {
    1: ['Open Child','run_Child_user'],
    2: ['','do_nothing'],
    3: ['','do_nothing'],
    4: ['','do_nothing'],
    5: ['','do_nothing'],
    6: ['','do_nothing'],
    7: ['','do_nothing'],
    8: ['Print All Attributes', 'print_all_atts'],
    9: ['Print Important Attributes', 'print_imp_atts'],
    }

    _OVERRIDE_OPTIONS = {}
    _SEARCHABLE_ATTS = []
    _ONE_LINE_ATTS = ['type']

    def __init__( self ):

        ParentClass.__init__( self )
        self._Children = []
        self.RTI = CRTI( self )

        ### Get Options setup
        self.OPTIONS = self._BASE_OPTIONS.copy()
        self.OPTIONS.update( self._OVERRIDE_OPTIONS )

    def __len__( self ):
        return len(self._Children)
    def __iter__( self ):
        self.i = -1
        return self
    def __next__( self ):
        self.i += 1
        if self.i < len(self):
            return self._Children[self.i]
        raise StopIteration

    def display( self ):
        return self.print_one_line_atts( print_off = False )

    def do_nothing( self ):
        pass

    def run_Child_user( self ):
        Child = self.get_Child_user()
        if Child != None:
            Child.run()

    def get_Child_user( self ):
        Child = ps.get_selection_from_list( list(self) )
        return Child

    def run_method_user( self ):
        method = input('method: ')
        print ( self.run_method( method ) )

    def run_RTI_choice( self, choice ):
        choice.run()

    def string_found_in_Children( self, string ):

        viable_Children = []
        for att in self._SEARCHABLE_ATTS:
            if string in str( self.get_attr(att) ).lower():
                viable_Children.append( self )
                break

        for Child in self:
            viable_Children.extend( Child.string_found_in_Children( string ) )

        return viable_Children

    def run( self ):

        while True:

            self.print_one_line_atts()
            ps.print_for_loop( [ Option[0] for Option in self.OPTIONS.values() ] )
            choice, user_input = self.RTI.get_one_input()

            if choice != None:
                self.run_RTI_choice( choice )
                continue

            if user_input == '':
                break

            try:
                user_input = int(user_input)
            except:
                continue

            if user_input in self.OPTIONS:
                self.run_method( self.OPTIONS[user_input][-1] )

        self.exit()

    def exit( self ):
        pass
        