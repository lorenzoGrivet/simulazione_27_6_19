from dataclasses import dataclass

@dataclass
class Artist:
    artist_id: int
    name: str

    def __hash__(self):
        return hash(self.artist_id)

    def __str__(self):
        return f"{self.name}"