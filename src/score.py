"""Store score game."""


class ScoreGamer:
    """Store score game."""

    def __init__(self) -> None:
        """Init Score Game."""
        self.score_gamer: list[ScorePlayer] = 0


class ScorePlayer(ScoreGamer):
    """Store score player."""

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.score: int = 0
        self.level: int = 0
        self.time: float = 0

    def add_s_pacgum_score(self) -> None:
        """Adition super pacgum score."""
        self.score += 50

    def add_pacgum_score(self) -> None:
        """Adition pacgum score."""
        self.score += 10
