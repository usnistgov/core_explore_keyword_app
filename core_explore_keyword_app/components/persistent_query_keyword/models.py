""" Persistent Query Keyword model
"""
from mongoengine import errors as mongoengine_errors

from core_explore_common_app.components.abstract_persistent_query.models import (
    AbstractPersistentQuery,
)
from core_main_app.commons import exceptions


class PersistentQueryKeyword(AbstractPersistentQuery):
    """Persistent Query Keyword"""

    @staticmethod
    def get_by_id(query_id):
        """Get a persistent query Keyword

        Args:
            query_id:

        Returns:

        """
        try:
            return PersistentQueryKeyword.objects().get(pk=query_id)
        except mongoengine_errors.DoesNotExist as e:
            raise exceptions.DoesNotExist(str(e))
        except Exception as e:
            raise exceptions.ModelError(str(e))

    @staticmethod
    def get_by_name(query_name):
        """Get a persistent query Keyword

        Args:
            query_name:

        Returns:

        """
        try:
            return PersistentQueryKeyword.objects().get(name=query_name)
        except mongoengine_errors.DoesNotExist as e:
            raise exceptions.DoesNotExist(str(e))
        except Exception as e:
            raise exceptions.ModelError(str(e))
