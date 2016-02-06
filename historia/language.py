from historia.culture import SocialSystem, SocialSystemVariant

class LanguageVariant(SocialSystemVariant):
    """
    The Language of a specific area.

    e.g. German in Berlin
    """
    pass


class Language(SocialSystem):
    """
    Language

    e.g. Chinese
         North
    """

    variation_class = LanguageVariant

    @property
    def system_name(self):
        """
        Dialects are subgroupings of Languages
        """
        if self.inactive:
            return "Language"
        return "Dialect"
