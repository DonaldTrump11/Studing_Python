class BookIOErrors(Exception):
    pass
        
class PageNotFoundError(BookIOErrors):
    pass

class TooLongTextError(BookIOErrors):
    pass

class PermissionDeniedError(BookIOErrors):
    pass

class NotExistingExtensionError(BookIOErrors):
    pass
    
