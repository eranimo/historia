from historia.culture import SocialSystem, SocialSystemVariant

class CultureVariant(SocialSystemVariant):
    """
    The Culture of a specific area.

    e.g. Chinese in Henan Province
    """
    pass

class Culture(SocialSystem):
    """
    Culture

    e.g. Chinese
    """

    variation_class = CultureVariant

    @property
    def system_name(self):
        """
        Cultures are subgroupings of CultureGroups
        """
        if self.inactive:
            return "CultureGroup"
        return "Culture"

    def split(self):
        """
        Split this culture into a new one.
        The current Culture will become a CultureGroup
        """
