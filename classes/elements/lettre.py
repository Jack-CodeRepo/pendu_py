#!/usr/bin/env python
# coding: utf-8
# ==================================================================================================


# ==================================================================================================
#   IMPORT
# ==================================================================================================



# ==================================================================================================
#   CLASSES
# ==================================================================================================



class class_lettre():
    def __init__(self, lettre=None):
        """
            class gérant la lettre en tant qu'objet

            :param lettre: valeure de la lettre, defaults to None
            :type lettre: str, optional
        """
        
        self.lettre = lettre

    def get_name(self):
        return self.lettre


    def set_name(self, value):
        self.lettre = str(value)