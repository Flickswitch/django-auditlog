class PostgresRouter(object):
    """
    A router to control all database operations on models for use with tests
    pertaining to the postgres test database.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read postgres models go to postgres db.
        """
        if model._meta.model_name.startswith('postgres'):
            return 'postgres'

        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write postgres models go to postgres db.
        """
        if model._meta.model_name.startswith('postgres'):
            return 'postgres'

        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the postgres app is involved.
        """
        obj1_starts_with_postgres = obj1._meta.model_name.startswith('postgres')
        obj2_starts_with_postgres = obj2._meta.model_name.startswith('postgres')

        if obj1_starts_with_postgres or obj2_starts_with_postgres:
            return True

        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the postgres app only appears in the 'postgres db'
        database.
        """
        if model_name.startswith('postgres'):
            return db == 'postgres'

        return None
