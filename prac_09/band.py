class Band:
    """Represent a musical band containing multiple musicians."""

    def __init__(self, name= ""):
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a readable string describing the band and its musicians."""
        musician_strings = [str(musician) for musician in self.musicians]
        return f"{self.name} ({', '.join(musician_strings)})"

    def play(self):
        """Return a list of each member on their instrument."""
        play_strings = [musician.play() for musician in self.musicians]
        return '\n'.join(play_strings)

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)