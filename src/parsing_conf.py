from pydantic import BaseModel, Field, model_validator, field_validator
from typing import Any
import json


class LevelConfig(BaseModel):

    width: int = Field(..., ge=2)
    height: int = Field(..., ge=2)
    level_max_time: int = Field(..., ge=0)
    pacgum: int = Field(default=42, ge=0)
    speed: int = Field(default=2, ge=0)


class Config(BaseModel):

    size_screen: tuple
    highscore_filename: str
    lives: int = Field(..., ge=0)
    points_per_pacgum: int = Field(..., ge=0)
    points_per_super_pacgum: int = Field(..., ge=0)
    points_per_ghost: int = Field(..., ge=0)
    levels: list[LevelConfig] = Field(..., min_length=3)

    @field_validator("levels", mode='before')
    @classmethod
    def create_level_object(cls, levels: list[dict]) -> list[LevelConfig]:
        levels_list: list[LevelConfig] = []
        for level in levels:
            level_object = LevelConfig(**level)
            levels_list.append(level_object)
        return levels_list
    
    @field_validator("size_screen", mode="before")
    @classmethod
    def create_size_screen(cls, size_screen: list[int]) -> tuple[int]:
        """Create tuple for size screen."""
        for size in size_screen:
            if size < 800:
                raise ValueError("size screen greter than (800, 800)")
        return tuple(size_screen)


    @model_validator(mode='after')
    def validation(self) -> Any:
        if (not self.highscore_filename.endswith(".json")
            or not self.highscore_filename.startswith("./")):
            raise ValueError("File score format not valid")
        return self


def parsing_conf(parsing_conf: str) -> dict:
    clean_line: list[str] = []
    config_json: dict[str, Any] = {}
    try:
        with open(parsing_conf, 'r') as f:
            # print(f)
            for all_line in f:
                all_line = all_line.strip()
                if not all_line.startswith("#"):
                    clean_line.append(all_line)
        if not clean_line:
            raise ValueError("config file is empty")
        clean_json: str = "".join(clean_line)
        config_json = json.loads(clean_json)
        config = Config(**config_json)
        return config
    except ValueError as e:
        print(e)
