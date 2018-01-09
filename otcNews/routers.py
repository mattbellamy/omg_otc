class otcRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        thirdPartyModels = ['otcNews','otcSecurities','norwayTracker']
        if model._meta.app_label in thirdPartyModels:
            return 'omgotc'
        return None

