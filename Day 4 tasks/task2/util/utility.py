import os

def unique_name_check( name_list ):
    """
        parameter: unique_name_check( list )
        checks if the list constain any duplicate entries
    """
    return len( name_list ) == len( set(name_list) )


def path_join( directory_list ):
    """
        parameter: path_join( list )
    """
    return os.path.join(*directory_list)