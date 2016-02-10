from uuid import uuid4

class SocialSystem:
    """
    Abstract base class for handling social systems that can change
    when groups are separated from each other. Handles evolution of these systems
    including merging and splitting off into new instances.

    e.g. Christianity (Religion [SocialSystem])
         Catholicism (Sect [SocialSystem])

    e.g. Korean (Culture [SocialSystem])
         South Korean (Culture [SocialSystem])

         Chinese (CultureGroup [SocialSystem])
         Cantonese (Culture  [SocialSystem])

    e.g. German language (Language [SocialSystem])
         High German dialect (Dialect [SocialSystem])
    """

    variation_class = None

    def __init__(self, manager, name, parent=None):
        self.name = name

        self.manager = manager

        self.id = uuid4().hex

        # the parent SocialSystem
        # at the beginning of the simulation, all the SocialSystems will have no parent
        self.parent = parent

        # do people still belong to this group?
        self.inactive = False

        # the amount of prestige points this SocialSystem has
        self.prestige = 0

        # sub-SocialSystems of this SocialSystem
        self.children = []

        # regional variations
        # inactive SocialSystem should have no variants
        self.variations = []

    def create_variation(region):
        """
        Creates a new regional variation of this SocialSystem
        """
        return self.variation_class(self)

    @property
    def siblings(self):
        """
        Returns all siblings of this SocialSystem's parent, if they have one
        Including this same SocialSystem
        """
        if self.parent is None:
            return []
        return self.parent.children

    @property
    def system_name(self):
        """
        Name of the SocialSystem implementation.
        """
        raise NotImplementedError("system_name must be implemented")

    def split(self):
        """
        Splits into two SocialSystems.
        """
        raise NotImplementedError('split method must be implemented')

    def merge_with(self, other):
        """
        Merges with another SocialSubSystem
        """
        raise NotImplementedError('merge_with method must be implemented')

    def __repr__(self):
        raise "<{} id={}>".format(self.system_name, self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __key__(self):
        return self.id

    def __hash__(self):
        return hash(self.__key__())


class SocialSystemVariant:
    """
    Abstract base class for a region-specific variant of a SocialSystem
    """

    def __init__(self, system):
        """
        system = SocialSystem this belongs to
        """
        self.system = system

        # from 0 to 100. The when it reaches 100, a new SocialSystem will created and this value
        # will reset to 0
        self.split_score = 0

    def calculate_split_score(self):
        """
        Calculates the new split score. Specific to each implementation of this class.
        """
        raise NotImplementedError('calculate_split_score method must be implemented')
