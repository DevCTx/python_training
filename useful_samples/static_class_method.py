class LuxuryWatch:
    watches_created = 0

    @staticmethod
    def validate_engraving(text):
        """ Can be used anywhere because no reference to the class (cls) or to the object (self) allowed"""
        if len(text) > 40 or not text.isalnum():
            raise ValueError("Engraving text must be alphanumeric and not exceed 40 characters.")

    @classmethod
    def get_number_of_watches_created(cls):
        """ Can be used to have access or see a class attribute. Should be used with cls"""
        return cls.watches_created

    @classmethod
    def create_watch_with_engraving(cls, text):
        """ Initialized a engraving text after validating its good format and called the init function"""
        cls.validate_engraving(text)
        watch = cls()
        watch.engraving = text
        return watch

    def __init__(self):
        self.engraving = None
        LuxuryWatch.watches_created += 1


print(LuxuryWatch.get_number_of_watches_created())  # Can be called before the creation of the first object

watch1 = LuxuryWatch()
print(LuxuryWatch.get_number_of_watches_created())

watch2 = LuxuryWatch.create_watch_with_engraving("MyWatch")
print(LuxuryWatch.get_number_of_watches_created())

try:
    watch3 = LuxuryWatch.create_watch_with_engraving("foo@baz.com")
except ValueError as e:
    print(e)
print(LuxuryWatch.get_number_of_watches_created())

print("Number of watches created:", LuxuryWatch.get_number_of_watches_created())
