import real_time_input

class CRTI( real_time_input.RealTimeInput ):

    def __init__( self, calling_from, **kwargs ):

        real_time_input.RealTimeInput.__init__( self, **kwargs )
        self.Aself = calling_from

    def search( self, **kwargs ):

        self.suggestions = []
        if len(self.string) > 1:
            self.suggestions = self.Aself.string_found_in_Children( self.string.lower() )
       
    def prepare_autocomplete( self, **kwargs ):

        if len(self.string) > 1:
            if len(self.suggestions) == 0:
                self.display = self.string + ' - (0)'

            else:
                self.suggestion = self.suggestions[ self.suggestion_index ]

                self.display = '{string} - ({i}/{n}) - {suggestion_display}'.format(
                    string = self.string,
                    i = self.suggestion_index+1,
                    n = len(self.suggestions),
                    suggestion_display = self.suggestion.display() )

        else:
            self.display = self.string